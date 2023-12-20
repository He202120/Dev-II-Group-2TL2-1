#Librairies

from datetime import datetime
import os
from geopy.geocoders import Nominatim
import folium

#Classes
class entityEnq():  # Création d'une classe entité d'enquête qui va regroupé les liens et informations sur une enquêtes
    def __init__(self, idEnq, enqNom, nivGravit = 0, dateEnq=datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__enqNom = enqNom  # Nom de l'enquête, un pseudo donné pour y avoir une idée
        self.__dateEnq = dateEnq  # Date précise du délit commit
        self.__nivGravit = nivGravit  # Niveau de gravité des faits
        self.__typeEnq = self.typeInit()  # Type de gravité des faits (Crime, délit et infraction)
        self.__enqueteId = idEnq  # Identifiant de l'enquête

    def __str__(self):
        return f"{self.__enqNom}       {self.__enqueteId}           {self.__dateEnq}   {self.__typeEnq} de Nv {self.__nivGravit}"

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
            self.__nivGravit = int(valeur)
            self.__typeEnq = self.typeInit()
        elif att == "nom":
            self.__enqNom = valeur
        else:
            print(ValueError)
    
    def typeInit(self):
        """
        Cette fonction définit niveau de gravité d'une enquête, allant du niveau le plus bas 1 au niveau le plus haut 9.
        
        PRE: Il s'appelle en paramètre
        POST: Renvoie un type en fonction du niveau de gravité
        """
        value = self.__nivGravit
        if value >= 7:
            return "Crime"  # Les crimes ont une gravité de 7 à 9
        elif value >= 4:
            return "Délit"  # Les délits ont une gravité de 4 à 6
        else:
            return "Infraction"  # Les infractions ont une gravité 1 à 3

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

class lieu():
    def __init__(self, codePostal="", ville="", rueNum="", nbrmaison=""):
        self.__ville = ville
        self.__codePostal = codePostal
        self.__rueNum = rueNum
        self.__nbrmaison = nbrmaison
        self.__latitude = self.lat()
        self.__longitude = self.long()

    def __str__(self):
        return f"Ville : {self.__ville} \nCode postal : {self.__codePostal} \nRue et numéro : {self.__rueNum} {self.__nbrmaison} \n"

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
        if isinstance(valeur, str):
            self.__codePostal = valeur
        else:
            print(ValueError)

    @getRue.setter
    def getRue(self, valeur):
        self.__rueNum = valeur

    @getNum.setter
    def getNum(self, valeur):
        self.__nbrmaison = valeur
    
    def lat(self):
        # Initialiser le géocodeur Nominatim
        geolocator = Nominatim(user_agent="mon_script")

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
        geolocator = Nominatim(user_agent="mon_script")

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

    def getmap(self, id):
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

        else:
            print("aucune latitude ou longitude n'ont été renseigné")

class personne:
    def __init__(self, id, nom="", prenom="", addr=lieu(), age=0, tel="", nationalite="", idNationalite=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__addr = addr  # Adresse de la personnes
        self.__tel = tel
        self.__nation = nationalite  # Nom de la nationalité
        self.__identityCode = idNationalite  # numéro de registre de la carte d'identité
        self.__id = id

    def __str__(self):
        return f"Profil : {self.__id} / {self.__nom} {self.__prenom}\nAge : {self.__age}\nAdresse domicile : {self.__addr.getVille}\nTel. : {self.__tel}\nNationalité et code d'identité : {self.__nation} {self.__identityCode}\n"

    @property
    def getNom(self):
        return self.__nom

    @property
    def getPrenom(self):
        return self.__prenom

    @property
    def getmap(self):
        try:
            self.__addr.getmap(self.__id)
        except ParamVideException:
            print("aucune latitude et longitude renseigné")

    @property
    def getAdrr(self):
        return self.__addr

    @property
    def getAge(self):
        return self.__age

    @property
    def getTel(self):
        return self.__tel

    @property
    def getNat(self):
        return self.__nation

    @property
    def getIdC(self):
        return self.__identityCode

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

    @getAge.setter
    def getAge(self, valeur):
        if isinstance(valeur, int):
            self.__age = valeur

    @getTel.setter
    def getTel(self, valeur):
        self.__Tel = valeur

    @getNat.setter
    def getNat(self, valeur):
        if isinstance(valeur, str):
            self.__nation = valeur

    @getIdC.setter
    def getIdC(self, valeur):
        self.__identityCode = valeur

class ParamVideException(Exception):
    pass

class NomVideException(Exception):
    pass

class GraviteVideException(Exception):
    pass

class ListeVideException(Exception):
    pass