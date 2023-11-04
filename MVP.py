#Librairies
from datetime import datetime

#définitions
nextEnqueteId = 100 #L'identifiant de la prochaine enquête ajoutée
idPrs = 10100 #L'identifiant de la prochaine personne ajoutée
idPreu = 50100 #L'identifiant de la prochaine preuve ajoutée

def typeInit(value):
        if value >= 7:
            return "Crime"
        elif value >= 4:
            return "Délit"
        else:
            return "Infraction"

def trieEnquete(table):
    if table == []:
        print("Il n'y a aucune enquête en cours.")
    else:
        table_trieGrav = sorted(table, key=lambda enquete: enquete.nivGravit,reverse=True)
        table_trieDate = sorted(table_trieGrav, key=lambda enquete: enquete.date,reverse=True)
        return table_trieDate[0]

def ajouter():
    global nextEnqueteId
    vNom = input("Introduire un nom pour l'enquête.\n")
    vGra = input("Introduire le niveau de 1 à 9 de la gravité du problème. 1 ==> Le plus bas / 9 ==> Le plus haut\n")
    if  int(vGra) > 9 or int(vGra) < 1:
        print(ValueError)
        return 0
    vDate = input("Introduire une date d'initialisation. Inscrivez la dans un format 'Jour-Mois-Année Heure-Minute-Seconde'\n")
    listeEnq[nextEnqueteId] = [entityEnq(nextEnqueteId,vNom,int(vGra),vDate)]
    listeEnq[nextEnqueteId].append(lieu("Pas encodé","Pas encodé","Pas encodé"))
    listeEnq[nextEnqueteId].append([])
    listeEnq[nextEnqueteId].append([])
    nextEnqueteId += 1

def enlever():
    vR = int(input("Introduire l'id de l'enquête à supprimer.\n"))
    del listeEnq[vR]

def modifier(num = 0):
    mod = input("Modifier les données d'une enquête. (enquete (Num. d'enquête) - lieu (Num. d'enquête) - personne (Num. de personne) - preuve (Num. d'enquête))\n")
    if mod == "enquete":
        enqueteMod(int(num))
    elif mod == "lieu":
        lieuMod(int(num))
    elif mod == "personne":
        newPers(int(num))
    elif mod == "preuve":
        newPreuve(int(num))
    else:
        print("Modification annulé.\n")

def enqueteMod(num):
    mod = input("Paramètres globale ==> Nom - 1 / Niveau de gravité - 2 / Date - 3\n")
    if mod == "1":
        mod = input("Introduire un nouveau nom. Tapez 0 pour annuler\n")
        if mod == "0":
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["nom",mod]
    elif mod == "2":
        mod = input("Introduire un niveau de gravitez de 1 - 9 (1 est le moins important). Tapez 0 pour annuler\n")
        if mod == "0":
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["gravite",mod]
    elif mod == "3":
        mod = input("Introduire une nouvelle date (Jour-Mois-Année Heure-Minute-Seconde). Tapez 0 pour annuler\n")
        if mod == "0":
            print("Modification annulée.\n")
            return 0
        listeEnq[num][0].dataPr = ["date",mod]
    else:
        print("Modification annulé.\n")

def lieuMod(num):
    print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
    vVille = input("Introduire une ville.\n")
    if vVille == "ANNULER":
        print("Les modification ont été annuler.\n")
        return 0
    if vVille == "PASSER":
        vVille = "UNKNOWN"
    vCode = input("Introduire le code postal.\n")
    if vCode == "ANNULER":
        print("Les modification ont été annuler.\n")
        return 0
    if vCode == "PASSER":
        vCode = 0
    else:
        vCode = int(vCode)
    vRN = input("Introduire la rue (et le numéro).\n")
    if vRN == "ANNULER":
        print("Les modification ont été annuler.\n")
        return 0
    if vRN == "PASSER":
        vRN = "UNKNOWN"
    listeEnq[num][1].getVille = vVille
    listeEnq[num][1].getCodePostal = vCode
    listeEnq[num][1].getRue = vRN
    print("Nouvelle donnée enregistré.\n")

def newPers(num):
    tabD = []
    global idPrs
    mod = input("Nouvelle enregistrement - 1 / Effacer un enregistrement - 2 / Associer un enregistrement - 3 / Désassocier une personne - 4\n")
    if mod == "1":
        ph = ["Nom ?\n","Prenom ?\n","Age ?\n","Adresse domicile ?\n","Téléphone ?\n","Nationalité ?\n","Numéro d'identité ?\n"]
        print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
        for i in range(7):
            tabD.append(input(ph[i]))
            if tabD[i] == "ANNULER":
                print("Les modification ont été annuler.\n")
            if tabD[i] == "PASSER":
                tabD[i] = "UNKNOWN"
        listePrs[idPrs] = personne(idPrs,tabD[0],tabD[1],tabD[2],tabD[3],tabD[4],tabD[5],tabD[6])
        idPrs += 1
        print("Enregistrement complet!\n")
    elif mod == "2":
        ts = input(f"Etes-vous sûr de supprimer la personne id : {num}, Tapez YES pour continuer, n'importe quoi d'autre pour annuler.\n")
        if ts == "YES":
            del listePrs[num]
            print("Personne effacer avec succès.\n")
            return 0
        print("Modification annulée.\n")
    elif mod == "3":
        ts = input(f"Sélectionnez l'id de l'enquête à associer avec la personne id : {num}. Tapez ANNULER pour annuler.\n")
        if ts == "ANNULER":
            print("Action annulée.\n")
            return 0
        ts = int(ts)
        listeEnq[ts][2].append(num)
        print(f"Personne associé avec l'enquête {ts}")
    elif mod == "4":
        ts = input("Introduire l'enquête à désassocier de la personne. Tapez ANNULER pour annuler.\n")
        if ts == "ANNULER":
            print("Action annulée.\n")
            return 0
        ts = int(ts)
        for j in range(len(listeEnq[ts][2])):
            if listeEnq[ts][2][j] == num:
                listeEnq[ts][2].pop(int(j))
        print("Personne désassocier.\n")
    else:
        print("Modification annulez.\n")

def newPreuve(num):
    tabP = []
    global idPreu
    mod = input("Ajouter une preuve - 1 / Effacer une preuve - 2 / Réinitialiser - 3\n")
    if mod == "1":
        ph = ["Type de preuve ?\n","Pseudo ?\n","Date (Jour-Mois-Année Heure-Minute-Seconde)?\n"]
        print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
        for i in range(3):
            tabP.append(input(ph[i]))
            if tabP[i] == "ANNULER":
                print("Les modification ont été annuler.\n")
            if tabP[i] == "PASSER":
                tabP[i] = "UNKNOWN"
        listeEnq[num][3].append({idPreu : preuve(idPreu,tabP[0],tabP[1],tabP[2])})
        idPreu += 1
        print("Enregistrement complet!\n")
    elif mod == "2":
        ts = input("Tapez l'id de la preuve à supprimer. Tapez ANNULER pour annuler.\n")
        if ts == "ANNULER":
            print("Modification annulée.\n")
            return 0
        ts = int(ts)
        for i in range(len(listeEnq[num][3])):
            kr = listeEnq[num][3][i].keys()
            for j in kr:
                if j == ts:
                    kr = listeEnq[num][3].pop(i)
        print("Preuve effacer.")
    elif mod == "3":
        ts = input("Etes-vous sûr de vouloir effacer toute les preuves de cette enquête? Tapez YES pour confirmer et n'importe quoi d'autre pour annuler.\n")
        if ts != "YES":
            print("Action annulée.\n")
            return 0
        listeEnq[num][3] = []
        print(f"Le tableau des preuves à été vidée.")
    else:
        print("Modification annulez.\n")

def afficher():
    chx = input("Affichez la liste des enquêtes - 1 / Affichez la liste des personnes - 2\n")
    if chx == "1":
        affEnq()
    elif chx == "2":
        affPrs()
    else:
        print("Retour au menu principale")

def affEnq():
    if listeEnq == {}:
        print("Liste d'enquête vide")
        return 0
    for i in listeEnq.keys():
        print(listeEnq[i])

#classes
class lieu():
    def __init__(self, ville = "", codePostal = "", rueNum = ""):
        self.__ville = ville
        self.__codePostal = codePostal
        self.__rueNum = rueNum
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

class personne:
    def __init__(self, id, nom = "", prenom = "", age = 0, addr = "", tel = "", nationalite = "", idNationalite = ""):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__addr = addr
        self.__tel = tel
        self.__nation = nationalite
        self.__identityCode = idNationalite
        self.__id = id
    def __str__(self):
        return f"Profil : {self.__id } / {self.__nom} {self.__prenom}\nAge : {self.__age}\nAdresse domicile : {self.__addr}\nTel. : {self.__tel}\nNationalité et code d'identité : {self.__nation} {self.__identityCode}\n"
    @property
    def getNom(self):
        return self.__nom
    @property
    def getPrenom(self):
        return self.__prenom
    @property
    def getAge(self):
        return self.__age
    @property
    def getAddr(self):
        return self.__addr
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
    @getPrenom.setter
    def getPrenom(self, valeur):
        if isinstance(valeur, str):
            self.__prenom = valeur
    @getAge.setter
    def getAge(self, valeur):
        if isinstance(valeur, int):
            self.__age = valeur
    @getAddr.setter
    def getAddr(self, valeur):
        self.__addr = valeur
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

class preuve():
    def __init__(self, id, type = "", pseudo = "", ddate = datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__type = type
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


class entityEnq(): #Création d'une classe entité d'enquête qui va regroupé les liens et informations sur une enquêtes
    def __init__(self, idEnq, enqNom, nivGravit, dateEnq = datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__enqNom = enqNom #Nom de l'enquête, un pseudo donné pour y avoir une idée
        self.__dateEnq = dateEnq #Date précise du délit commit
        self.__nivGravit = nivGravit #Niveau de gravité des faits
        self.__typeEnq = typeInit(nivGravit)
        self.__enqueteId = idEnq #Identifiant de l'enquête
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

#Dictionnaires

listeEnq = {98 : entityEnq(98,"Test",5),99 : entityEnq(99,"test2",3)} #Dictionnaire des enquêtes
listePrs = {} #Dictionnaire des personnes
#Corps principale
