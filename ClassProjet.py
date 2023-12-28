# Librairies

from datetime import datetime
import os
from geopy.geocoders import Nominatim
import folium


class ParamVideException(Exception):
    pass


class NomVideException(Exception):
    pass


class GraviteVideException(Exception):
    pass


class MauvaisIdException(Exception):
    pass


class MauvaisDateException(Exception):
    pass


class ListeVideException(Exception):
    pass


class MauvaiseValeurException(Exception):
    pass


class lieu():
    def __init__(self, codePostal="", ville="", rueNum="", nbrmaison=""):
        self.__ville = ville
        self.__codePostal = codePostal
        self.__rueNum = rueNum
        self.__nbrmaison = nbrmaison
        self.__latitude = self.lat()
        self.__longitude = self.long()

    def __str__(self):
        return f"Ville : {self.__ville} \nCode postal : {self.__codePostal} \nRue et numéro : {self.__rueNum} {self.__nbrmaison}"

    @property
    def getVille(self):
        return self.__ville

    @property
    def getCodePostal(self):
        return self.__codePostal

    @property
    def getRue(self):
        return self.__rueNum

    @property
    def getNum(self):
        return self.__nbrmaison

    @property
    def set_Lat_Long(self):
        self.__latitude = self.lat()
        self.__longitude = self.long()

    @getVille.setter
    def getVille(self, valeur):
        if isinstance(valeur, str):
            self.__ville = valeur
        else:
            print(ValueError)

    @getCodePostal.setter
    def getCodePostal(self, valeur):
            self.__codePostal = str(valeur)


    @getRue.setter
    def getRue(self, valeur):
        self.__rueNum = valeur

    @getNum.setter
    def getNum(self, valeur):
        self.__nbrmaison = valeur

    def lat(self):
        # Initialiser le géocodeur Nominatim
        geolocator = Nominatim(user_agent="mon_script",scheme="https")

        nom_ville = self.__ville
        nom_rue = self.__rueNum
        numero_maison = self.__nbrmaison

        try:
            # Concaténer le nom de la ville, de la rue et le numéro de maison pour la recherche
            adresse_complete = f"{numero_maison} {nom_rue}, {nom_ville}"

            # Obtenir les coordonnées à partir de l'adresse complète
            location = geolocator.geocode(adresse_complete)

            if location:
                # Afficher les coordonnées
                return location.latitude
            else:
                return ""

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def long(self):
        # Initialiser le géocodeur Nominatim
        geolocator = Nominatim(user_agent="mon_script",scheme="https")

        nom_ville = self.__ville
        nom_rue = self.__rueNum
        numero_maison = self.__nbrmaison

        try:
            # Concaténer le nom de la ville, de la rue et le numéro de maison pour la recherche
            adresse_complete = f"{numero_maison} {nom_rue}, {nom_ville}"

            # Obtenir les coordonnées à partir de l'adresse complète
            location = geolocator.geocode(adresse_complete)

            if location:
                # Afficher les coordonnées
                return location.longitude
            else:
                return ""

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def getmapEnq(self, id):
        if self.__latitude != "":
            # Coordonné GPS (latitude, longitude) de l'emplacement souhaité
            latitude = self.__latitude
            longitude = self.__longitude

            # Création de la carte
            ma_carte = folium.Map(location=[latitude, longitude], zoom_start=14)

            # Ajout d'un marqueur
            folium.Marker([latitude, longitude], popup='Mon Marqueur').add_to(ma_carte)

            # Sauvegarde de la carte au format HTML
            ma_carte.save(f"lieux-enquetes/{id}.html")
            print("La map a bien été crée")
        else:
            print("aucune latitude ou longitude n'ont été renseigné")

    def getmapPers(self, id):
        if self.__latitude != "":
            # Coordonné GPS (latitude, longitude) de l'emplacement souhaité
            latitude = self.__latitude
            longitude = self.__longitude

            # Création de la carte
            ma_carte = folium.Map(location=[latitude, longitude], zoom_start=14)

            # Ajout d'un marqueur
            folium.Marker([latitude, longitude], popup='Mon Marqueur').add_to(ma_carte)

            # Sauvegarde de la carte au format HTML
            ma_carte.save(f"lieux-personnes/{id}.html")
            print("La map a bien été crée")
        else:
            print("aucune latitude ou longitude n'ont été renseigné")


class Dates:
    def __init__(self):
        self.__annee = 0
        self.__mois = 0
        self.__jour = 0

    def __str__(self):
        return f"{self.__jour}-{self.__mois}-{self.__annee}"

    @property
    def get_annee(self):
        return self.__annee

    @property
    def get_mois(self):
        return self.__mois

    @property
    def get_jour(self):
        return self.__jour

    @get_annee.setter
    def get_annee(self, arg):
        self.__annee = arg

    @get_mois.setter
    def get_mois(self, arg):
        self.__mois = arg

    @get_jour.setter
    def get_jour(self, arg):
        self.__jour = arg


class personne(Dates):

    def __init__(self, nom="", prenom="", addr=lieu(), age=0, tel="", nationalite="", idNationalite=""):
        super().__init__()
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__addr = addr  # Adresse de la personne
        self.__tel = tel
        self.__nation = nationalite  # Nom de la nationalité
        self.__identityCode = idNationalite  # numéro de registre de la carte d'identité
        self.__id = 0

    def __str__(self):
        return f"Profil : {self.__id} / {self.__nom} {self.__prenom}\nAge : {self.__age}\nAdresse domicile : {self.__addr.getVille}\nTel. : {self.__tel}\nNationalité et code d'identité : {self.__nation} {self.__identityCode}\n"

    def __eq__(self, autre):
        return self.__addr.getVille == autre.getAdrr.getVille

    @property
    def getNom(self):
        return self.__nom

    @property
    def getPrenom(self):
        return self.__prenom


    @property
    def getmap(self):
        try:
            self.__addr.getmapPers(self.__id)
        except ParamVideException:
            print("aucune latitude et longitude renseigné")

    @property
    def getAdrr(self):
        return self.__addr

    @property
    def get_age(self):
        """
               Calcule l'âge de la personne en utilisant la date actuelle et sa date de naissance.

               PRE:
                   - Aucun
               POST:
                   - Renvoie un entier représentant l'âge de la personne calculé en années en utilisant les attributs Jour, Mois, Année et dateactuel stocké dans l'objet dateobj
               RAISES:
                   - Renvoie une erreur ValueError si la date de naissance de la personne est dans le futur.
               """
        today = datetime.today()
        annee_courante = today.strftime('%Y')
        return int(annee_courante) - self.get_annee

    @property
    def getTel(self):
        return self.__tel

    @property
    def getNat(self):
        return self.__nation

    @property
    def getIdC(self):
        return self.__id


    @getNom.setter
    def getNom(self, valeur):
        if isinstance(valeur, str):
            self.__nom = valeur


    @getAdrr.setter
    def getAdrr(self,valeur):
        if isinstance(valeur, object):
            self.__addr = valeur
        else:
            raise ValueError("addresse renseignée n'est pas un objet")

    @getPrenom.setter
    def getPrenom(self, valeur):
        if isinstance(valeur, str):
            self.__prenom = valeur

    def set_age(self, valeur):
        """
        Modifie la date de naissance d'une personne qui se trouve dans les attributs Jour, Mois, Année interne à l'objet dateobj de classe Date.

        PRE:
            -
        POST:
            - Modifie l'attribut dateobj qui est un objet de classe Date stocké dans l'objet courant par les paramètre de cette fonction jour_annif, mois_annif, annee_annif.
        RAISES:
            - Renvoie une erreur ParamExceptionError si les attributs ne respectent pas les conditions ou que la date se trouve dans le futur.
        """
        today = datetime.today()
        annee_courante = today.strftime('%Y')
        try:
            dates = datetime.strptime(valeur, "%d-%m-%Y")
        except ValueError:
            raise MauvaisDateException
        except TypeError:
            raise MauvaisDateException
        if dates.year > int(annee_courante):
            raise MauvaisDateException
        self.get_annee = dates.year
        self.get_mois = dates.month
        self.get_jour = dates.day

    @getTel.setter
    def getTel(self, valeur):
        self.__Tel = valeur

    @getNat.setter
    def getNat(self, valeur):
        if isinstance(valeur, str):
            self.__nation = valeur

    @getIdC.setter
    def getIdC(self, valeur):
        self.__id = valeur



class Enqueteur(personne):
    compteur = 1

    def __init__(self, nom, prenom):
        super().__init__()
        self.__id = Enqueteur.compteur
        Enqueteur.compteur += 1
        self.__nom = nom
        self.__prenom = prenom

    def __str__(self):
        return f"Id : {self.__id}\nNom : {self.__nom}\nPrénom : {self.__prenom}"

    @property
    def getId(self):
        return self.__id

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_prenom(self):
        return self.__prenom

    @get_prenom.setter
    def get_prenom(self, arg):
        self.__prenom = arg

    @get_nom.setter
    def get_nom(self, arg):
        self.__nom = arg


class Suspect(personne):
    compteur = 1

    def __init__(self, nom, prenom, alibi):
        super().__init__()
        self.__id = Suspect.compteur
        Suspect.compteur += 1
        self.__nom = nom
        self.__prenom = prenom
        self.__alibi = alibi

    def __str__(self):
        return f"Id : {self.__id}\nNom : {self.__nom}\nPrénom : {self.__prenom}\nAlibi : {self.__alibi}"

    @property
    def getId(self):
        return self.__id

    @property
    def get_nom(self):
        return self.__nom

    @property
    def get_prenom(self):
        return self.__prenom

    @property
    def get_alibi(self):
        return self.__alibi

    @get_prenom.setter
    def get_prenom(self, arg):
        self.__prenom = arg

    @get_nom.setter
    def get_nom(self, arg):
        self.__nom = arg

    @get_alibi.setter
    def get_alibi(self, arg):
        self.__alibi = arg


class preuve():
    def __init__(self, id, type="", pseudo="", ddate=datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__type = type  # Arme à feu / Arme blanche / outils / ...
        self.__pseudo = pseudo
        self.__date = ddate
        self.__pId = id

    def __str__(self):
        return f"Identifiant : {self.__pId} \nType : {self.__type}\nPseudo : {self.__pseudo}\nDate d'acquisition : {self.__date}\n"

    @property
    def getType(self):
        return self.__type

    @property
    def getPseudo(self):
        return self.__pseudo

    @property
    def getDate(self):
        return self.__date

    @getType.setter
    def getType(self, valeur):
        self.__type = valeur

    @getPseudo.setter
    def getPseudo(self, valeur):
        self.__pseudo = valeur

    @getDate.setter
    def getDate(self, valeur):
        self.__date = valeur


class entityEnq():  # Création d'une classe entité d'enquête qui va regrouper les liens et informations sur une enquête
    compteur = 1

    def __init__(self, enqNom, nivGravit=0, dateEnq=datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__enqNom = enqNom  # Nom de l'enquête, un pseudo donné pour y avoir une idée
        self.__dateEnq = dateEnq  # Date précise du délit commit
        self.__nivGravit = nivGravit  # Niveau de gravité des faits
        self.__typeEnq = self.typeInit()  # Type de gravité des faits (Crime, délit et infraction)
        self.__enqueteId = entityEnq.compteur  # Identifiant de l'enquête
        entityEnq.compteur += 1

    def __str__(self):
        return f"Id: {self.__enqueteId}\nNom: {self.__enqNom}\nDate: {self.__dateEnq}\nGravité des faites: {self.__typeEnq} de Nv {self.__nivGravit}"

    def __eq__(self, autre):
        return self.__enqueteId == autre.get_id_enq

    @property
    def dataPr(self):
        return [self.__enqNom, self.__enqueteId, self.__dateEnq, self.__nivGravit]

    @dataPr.setter
    def dataPr(self, tab):
        att = tab[0]
        valeur = tab[1]
        if att == "date":
            self.__dateEnq = valeur
        elif att == "gravite":
            self.__nivGravit = valeur
        elif att == "nom":
            self.__enqNom = valeur
        else:
            print(ValueError)

    def typeInit(self):
        value = self.__nivGravit
        if value >= 7:
            return "Crime"  # Les crimes ont une gravité de 7 à 9
        elif value >= 4:
            return "Délit"  # Les délits ont une gravité de 4 à 6
        else:
            return "Infraction"  # Les infractions ont une gravité 1 à 3


    @property
    def get_id_enq(self):
        return self.__enqueteId

    @property
    def get_enq_nom(self):
        return self.__enqNom

    @property
    def get_niv_gravit(self):
        return self.__nivGravit

    @property
    def get_enq_date(self):
        return self.__dateEnq

    @get_id_enq.setter
    def get_id_enq(self, id):
        self.__enqueteId = id

    @get_enq_nom.setter
    def get_enq_nom(self, nom):
        self.__enqNom = nom

    @get_niv_gravit.setter
    def get_niv_gravit(self, nbr):
        self.__nivGravit = nbr

    @get_enq_date.setter
    def get_enq_date(self,arg):
        self.__dateEnq = arg


listeEnq = {}
listePrs = {}
listeSus = {}

ma = personne()
ma.set_age("26-02-2021")
print(ma.get_age)
print(ma.get_annee)