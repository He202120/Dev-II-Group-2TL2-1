# Librairies

from datetime import datetime
import os
from geopy.geocoders import Nominatim
import folium

# définitions

etatProg = True  # Définit l'état du programme
nextEnqueteId = 100  # L'identifiant de la prochaine enquête ajoutée
idPrs = 10100  # L'identifiant de la prochaine personne ajoutée
idPreu = 50100  # L'identifiant de la prochaine preuve ajoutée

"""Cette fonction définit niveau de gravité d'une enquête, allant du niveau le plus bas 1 au niveau le plus haut 9."""


def typeInit(value):
    if value >= 7:
        return "Crime"  # Les crimes ont une gravité de 7 à 9
    elif value >= 4:
        return "Délit"  # Les délits ont une gravité de 4 à 6
    else:
        return "Infraction"  # Les infractions ont une gravité 1 à 3


"""permet de trier les tables correspondantes"""


def trieEnquete(table):
    if table == []:
        print("Il n'y a aucune enquête en cours.")
    else:
        table_trieGrav = sorted(table, key=lambda enquete: enquete.nivGravit, reverse=True)
        table_trieDate = sorted(table_trieGrav, key=lambda enquete: enquete.date, reverse=True)
        return table_trieDate[0]


"""Cette fonction ajoute un nouvelle objet enquête basé sur la classe entityEnq"""


def ajouter():
    global nextEnqueteId
    vNom = input("Introduire un nom pour l'enquête.\n")  # Variable du nom
    if vNom == "":
        raise ParamVideException
    vGra = input(
        "Introduire le niveau de 1 à 9 de la gravité du problème. 1 ==> Le plus bas / 9 ==> Le plus haut\n")  # Variable du niveau de gravité
    if int(vGra) > 9 or int(vGra) < 1:
        print(ValueError)
        return 0
    vDate = input(
        "Introduire une date d'initialisation. Inscrivez la dans un format 'Jour-Mois-Année Heure:Minute:Seconde'\n")
    if vDate == "":
        listeEnq[nextEnqueteId] = [entityEnq(nextEnqueteId, vNom, int(vGra))]  # Tableau de l'enquête
    else:
        listeEnq[nextEnqueteId] = [entityEnq(nextEnqueteId, vNom, int(vGra), vDate)]  # Tableau de l'enquête
    listeEnq[nextEnqueteId].append(
        lieu("Pas encodé", "Pas encodé", "Pas encodé"))  # Tableau du lieu (données non-encodées)
    listeEnq[nextEnqueteId].append([])  # Tableau préventif pour y introduire des ids de personnes
    listeEnq[nextEnqueteId].append([])  # Tableau préventif pour y introduire des dictionnaires de preuves
    nextEnqueteId += 1
    os.system("cls")  # Fonction qui envoie une commande clear au terminal
    print("Enquête rajoutée avec succès.\n")


"""Cette fonction efface une enquête enregistré ultérieurement"""


def enlever():
    vR = int(input("Introduire l'id de l'enquête à supprimer.\n"))  # Variable de l'id à supprimer
    if listeEnq == {}:
        os.system("cls")
        print("Il n'y a encore aucune enquête encoder.\n")
        return 0
    if vR in listeEnq.keys():  # L'on cherche l'id dans le dictionnaire d'enquête
        del listeEnq[vR]
        os.system("cls")
        print("Enquête retirée avec succès.\n")
        return 0
    os.system("cls")
    print("L'id donnée n'existe pas dans la table.\n")


"""Cette fonction regroupe des appelles d'autres fonctions permettant de modifier divers données."""


def modifier(num=0):
    mod = input(
        "Modifier les données d'une enquête. (enquete (id. d'enquête) - lieu (id. d'enquête) - personne (id. de personne) - preuve (id. d'enquête))\n")
    if mod == "enquete":
        enqueteMod(int(num))  # Modification des données principale d'une enquête
    elif mod == "lieu":
        lieuMod(int(num))  # Modification du lieu de l'enquête
    elif mod == "personne":
        newPers(int(num))  # Modification des personnes
    elif mod == "preuve":
        newPreuve(int(num))  # Modification des preuves d'une enquêtes
    else:
        os.system("cls")
        print("Modification annulé.\n")


"""Cette fonction modifie les données principale d'une enquête (1er tableau du dictionnaire listEnq)"""


def enqueteMod(num):
    if num not in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
        os.system("cls")
        print("Cette enquête n'existe pas.\n")
        return 0
    mod = input(
        "Paramètres globale ==> Nom - 1 / Niveau de gravité - 2 / Date - 3\n")  # L'on demande le paramètre à modifier
    if mod == "1":
        mod = input("Introduire un nouveau nom. Tapez n'importe quoi d'autre pour annuler\n")  # Modification du nom
        if mod == "0":
            os.system("cls")
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["nom", mod]
        os.system("cls")
        print("Modification réussite.\n")
    elif mod == "2":
        mod = input(
            "Introduire un niveau de gravitez de 1 - 9 (1 est le moins important). Tapez 0 pour annuler\n")  # Modification de la gravité des faits
        if mod == "0":
            os.system("cls")
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["gravite", mod]
        os.system("cls")
        print("Modification réussite.\n")
    elif mod == "3":
        mod = input(
            "Introduire une nouvelle date (Jour-Mois-Année Heure-Minute-Seconde). Tapez 0 pour annuler\n")  # Modification de la date
        if mod == "0":
            os.system("cls")
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["date", mod]
        os.system("cls")
        print("Modification réussite.\n")
    else:
        os.system("cls")
        print("Modification annulé.\n")


"""Cette fonction change les données représentant le lieu de l'enquête"""


def lieuMod(num):
    if num not in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
        os.system("cls")
        print("Cette enquête n'existe pas.\n")
        return 0
    print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
    vVille = input("Introduire une ville.\n")  # Variable du nom de la ville
    if vVille == "ANNULER":
        os.system("cls")
        print("Les modification ont été annuler.\n")
        return 0
    if vVille == "PASSER":
        vVille = "UNKNOWN"
    vCode = input("Introduire le code postal.\n")  # Variable du code postal de la ville
    if vCode == "ANNULER":
        os.system("cls")
        print("Les modification ont été annuler.\n")
        return 0
    if vCode == "PASSER":
        vCode = 0
    else:
        vCode = int(vCode)
    vRN = input("Introduire la rue (et le numéro).\n")  # Variable de la rue et le numéro du lieu
    if vRN == "ANNULER":
        os.system("cls")
        print("Les modification ont été annuler.\n")
        return 0
    if vRN == "PASSER":
        vRN = "UNKNOWN"
    listeEnq[num][1].getVille = vVille
    listeEnq[num][1].getCodePostal = vCode
    listeEnq[num][1].getRue = vRN
    os.system("cls")
    print("Nouvelle donnée enregistré.\n")


"""Cette fonction gère les personnes dans le dictionnaire des personnes"""


def newPers(num):
    tabD = []
    global idPrs
    mod = input(
        "Nouvelle enregistrement - 1 / Effacer un enregistrement - 2 / Associer un enregistrement - 3 / Désassocier une personne - 4\n")  # On choisit une option pour la personne

    # Le mod "1" crée une nouvelle personne

    if mod == "1":
        ph = ["Nom ?\n", "Prenom ?\n", "Age ?\n", "Adresse domicile ?\n", "Téléphone ?\n", "Nationalité ?\n",
              "Numéro d'identité ?\n"]  # Variable phrase contenant des phrases à afficher
        print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
        for i in range(7):
            tabD.append(input(ph[i]))
            if tabD[i] == "ANNULER":
                print("Les modification ont été annuler.\n")
            if tabD[i] == "PASSER":
                tabD[i] = "UNKNOWN"
        listePrs[idPrs] = personne(idPrs, tabD[0], tabD[1], tabD[2], tabD[3], tabD[4], tabD[5], tabD[6])
        idPrs += 1
        os.system("cls")
        print("Enregistrement complet!\n")

    # Le mod "2" efface une personne créée ultérieurement

    elif mod == "2":
        if num not in listePrs.keys():  # On regarde si l'id se trouve dans le dictionnaire de personne
            os.system("cls")
            print("Cette personne n'existe pas.\n")
            return 0
        chx = input(
            f"Etes-vous sûr de supprimer la personne id : {num}, Tapez YES pour continuer, n'importe quoi d'autre pour annuler.\n")  # Variable qui prend le choix de l'utilisateur
        if chx == "YES":
            del listePrs[num]  # On efface la personne
            for i in listeEnq.keys():
                if num in listeEnq[i][2]:
                    del listeEnq[i][2][listeEnq[i][2].index(
                        num)]  # On efface pour toute enquête, la case dans le tableau 2 ayant l'id de la personne sélectionné
            os.system("cls")
            print("Personne effacer avec succès.\n")
            return 0
        os.system("cls")
        print("Modification annulée.\n")

    # Le mod "3" associe une personne à une enquête

    elif mod == "3":
        numEnq = input(
            f"Sélectionnez l'id de l'enquête à associer avec la personne id : {num}. Tapez ANNULER pour annuler.\n")  # Variable qui contient (normalement) l'id de l'enquête sélectionné
        if numEnq == "ANNULER":
            print("Action annulée.\n")
            return 0
        if int(numEnq) not in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
            os.system("cls")
            print("Cette enquête n'existe pas.\n")
            return 0
        ts = int(numEnq)
        listeEnq[ts][2].append(num)
        os.system("cls")
        print(f"Personne associé avec l'enquête {ts}")

    # Le mod "4" désassocie une personne d'une enquête

    elif mod == "4":
        numEnq = input(
            "Introduire l'enquête à désassocier de la personne. Tapez ANNULER pour annuler.\n")  # Variable qui contient (normalement) l'id de l'enquête sélectionné
        if numEnq == "ANNULER":
            print("Action annulée.\n")
            return 0
        if int(numEnq) not in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
            os.system("cls")
            print("Cette enquête n'existe pas.\n")
            return 0
        ts = int(numEnq)
        for j in range(len(listeEnq[ts][2])):
            if listeEnq[ts][2][j] == num:
                listeEnq[ts][2].pop(int(j))  # On enlève l'id de la personne du tableau
        os.system("cls")
        print("Personne désassocier.\n")
    else:
        os.system("cls")
        print("Modification annulez.\n")


"""Cette fonction gère les preuves d'une enquête"""


def newPreuve(num):
    tabP = []
    global idPreu
    mod = input(
        "Ajouter une preuve - 1 / Effacer une preuve - 2 / Réinitialiser - 3\n")  # On enregistre la sélection dans une variable

    # Le mod "1" ajoute une nouvelle preuve

    if mod == "1":
        ph = ["Type de preuve ?\n", "Pseudo ?\n",
              "Date (Jour-Mois-Année Heure:Minute:Seconde)?\n"]  # Variable phrase contenant des phrases à afficher
        print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
        for i in range(3):
            tabP.append(input(ph[i]))
            if tabP[i] == "ANNULER":
                print("Les modification ont été annuler.\n")
            if tabP[i] == "PASSER":
                tabP[i] = "UNKNOWN"
        listeEnq[num][3].append({idPreu: preuve(idPreu, tabP[0], tabP[1], tabP[
            2])})  # On enregistre la preuve dans un dictionnaire qui prendra la place d'une case dans le dernier tableau
        idPreu += 1
        os.system("cls")
        print("Enregistrement complet!\n")

    # Le mod "2" efface une preuve existante

    elif mod == "2":
        idEnq = input(
            "Tapez l'id de la preuve à supprimer. Tapez ANNULER pour annuler.\n")  # La variable avec l'id de la preuve à effacer
        if idEnq == "ANNULER":
            print("Modification annulée.\n")
            return 0
        ts = int(idEnq)
        for i in range(len(listeEnq[num][3])):
            kr = listeEnq[num][3][i].keys()
            for j in kr:
                if j == ts:
                    kr = listeEnq[num][3].pop(i)
        os.system("cls")
        print("Preuve effacer.")

    # Le mod "3" réinitialise le tableau des preuves

    elif mod == "3":
        ts = input(
            "Etes-vous sûr de vouloir effacer toute les preuves de cette enquête? Tapez YES pour confirmer et n'importe quoi d'autre pour annuler.\n")
        if ts != "YES":
            print("Action annulée.\n")
            return 0
        listeEnq[num][3] = []
        os.system("cls")
        print(f"Le tableau des preuves à été vidée.")
    else:
        os.system("cls")
        print("Modification annulez.\n")


"""Cette fonction donne des options affichage d'enquête et de personnes"""


def afficher():
    chx = input("Affichez la liste des enquêtes - 1 / Affichez la liste des personnes - 2\n")
    if chx == "1":
        affEnq()
    elif chx == "2":
        affPers()
    else:
        os.system("cls")
        print("Retour au menu principale.\n")


"""Cette fonction affiche la liste des enquêtes, une id supplémentaire demander permet d'afficher le lieu, les ids des personnes impliquées ainsi que les preuves"""


def affEnq():
    if listeEnq == {}:
        print("Liste d'enquête vide.\n")
        return 0
    for i in listeEnq.keys():
        print(listeEnq[i][0])  # Affiche la liste des enquête
    chx = input(
        "Introduisez l'id d'une enquête pour obtenir plus d'information. Tapez SORTIR pour revenir au menu principale.\n")
    if chx == "SORTIR":
        os.system("cls")
        print("Retour au menu principale.\n")
        return 0
    else:
        chx = int(chx)
        if chx not in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
            os.system("cls")
            print("Cette enquête n'existe pas.\n")
            return 0
        print(f"\n{listeEnq[chx][1]}")
        print(f"\nIdentifiant des personnes concernées : {listeEnq[chx][2]}\n")
        print("Liste des preuves :")
        for i in listeEnq[chx][3]:
            for j in i.keys():
                print(f"{i[j]}\n")
        slp = input("Continuer ?")  # Variable pour attendre un retour au menu principale
        os.system("cls")
        return 0


"""Affiche la liste des personnes"""


def affPers():
    if listePrs == {}:  # On regarde si la liste est vide
        print("Liste des personnes vide.\n")
        return 0
    for i in listePrs.keys():
        print(listePrs[i])


def menuPrincipale():
    global etatProg
    print("// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //")
    print("//                      Unnamed software version 1.0                                   //")
    print("//                                                                                     //")
    print("// 'ajouter' : Permet d'enregistrer une nouvelle enquête de données vide               //")
    print("//                                                                                     //")
    print("// 'enlever' : Permet d'éffacer une enquête ainsi que ses données                      //")
    print("//                                                                                     //")
    print("// 'modifier' : Permet de modifier les données d'une enquête                           //")
    print("//  Certaines fonctions nécessite d'introduire l'id d'une enquête ou d'une personne    //")
    print("//                                                                                     //")
    print("// 'afficher' : Afficher les données d'une catégorie (enquête, personne, etc)          //")
    print("//                                                                                     //")
    print("// 'OFF' : Arrêter le programme                                                        //")
    print("//                                                                                     //")
    print("// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //")
    opt = input("Option\n")
    if opt == "ajouter":
        ajouter()
    elif opt == "enlever":
        enlever()
    elif opt == "modifier":
        opt = input(
            "Introduire une id d'enquête (Si vous intéragissez avec une entité personne, encoder l'id de cette dernière).\n")
        modifier(opt)
    elif opt == "afficher":
        afficher()
    elif opt == "OFF":
        etatProg = False
    else:
        os.system("cls")
        return 0


# classes

"""Cette classe définit un nouveau lieu"""

class ParamVideException(Exception):
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
        return f"Ville : {self.__ville} \nCode postal : {self.__codePostal} \nRue et numéro : {self.__rueNum} \n"

    @property
    def getVille(self):
        return self.__ville

    @property
    def getCodePostal(self):
        return self.__codePostal

    @property
    def getRue(self):
        return self.__rueNum

    @getVille.setter
    def getVille(self, valeur):
        if isinstance(valeur, str):
            self.__ville = valeur
        else:
            print(ValueError)

    @getCodePostal.setter
    def getCodePostal(self, valeur):
        if isinstance(valeur, int):
            self.__codePostal = valeur
        else:
            print(ValueError)

    @getRue.setter
    def getRue(self, valeur):
        self.__rueNum = valeur

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

    def getmap(self, person):
        if self.__latitude != "":
            # Coordonné GPS (latitude, longitude) de l'emplacement souhaité
            latitude = self.__latitude
            longitude = self.__longitude

            # Création de la carte
            ma_carte = folium.Map(location=[latitude, longitude], zoom_start=14)

            # Ajout d'un marqueur
            folium.Marker([latitude, longitude], popup='Mon Marqueur').add_to(ma_carte)

            # Sauvegarde de la carte au format HTML
            ma_carte.save(f"lieux-personnes/{person}.html")

        else:
            print("aucune latitude ou longitude n'ont été renseigné")

"""Cette classe définit une personne (Suspect, inspecteur, etc.)"""


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


"""Cette classe définit une preuve"""


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


"""Cette classe définit les données principale d'une enquête (Un identifiant, un pseudo / nom, un niveau de gravité des faits et la date)"""


class entityEnq():  # Création d'une classe entité d'enquête qui va regroupé les liens et informations sur une enquêtes
    def __init__(self, idEnq, enqNom, nivGravit, dateEnq=datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__enqNom = enqNom  # Nom de l'enquête, un pseudo donné pour y avoir une idée
        self.__dateEnq = dateEnq  # Date précise du délit commit
        self.__nivGravit = nivGravit  # Niveau de gravité des faits
        self.__typeEnq = typeInit(nivGravit)  # Type de gravité des faits (Crime, délit et infraction)
        self.__enqueteId = idEnq  # Identifiant de l'enquête

    def __str__(self):
        return f"Nom de l'enquête : {self.__enqNom} \n Identifiant : {self.__enqueteId} \n Date : {self.__dateEnq} \n Gravité des faits : {self.__typeEnq} Nv.{self.__nivGravit}\n"

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


# Dictionnaires

listeEnq = {}  # Dictionnaire des enquêtes, la valeur d'une clé est un tableau divisé en 4 tableaux (l'enquête crée, son lieu, l'id des personnes impliquées, un tableau de dictionnaire de preuve).
listePrs = {}  # Dictionnaire des personnes, leurs ids sont peuvent être lié à une enquête.

# Corps principale

lo = lieu("Tubize","Rue de la déportation","273")
la = personne("id4","greg", "wa",lo)

la.getmap
print(la)

