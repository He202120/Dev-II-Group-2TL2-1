#Librairies
from datetime import datetime

#définitions
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
def add():

def remove():

def 

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
    _next_id = 5000
    def __init__(self,nom = "", prenom = "", age = 0, addr = "", tel = "", nationalite = "", identityCode = ""):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__addr = addr
        self.__tel = tel
        self.__nation = nationalite
        self.__identityCode = identityCode
        self.__id = personne._next_id
        personne._next_id += 1
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
    _id_preuve = 1
    def __init__(self, type = "", pseudo = "", lien = "", ddate = datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__type = type
        self.__pseudo = pseudo
        self.__lien = lien
        self.__date = ddate
        self.__pId = preuve._id_preuve
        preuve._id_preuve += 1
    def __str__(self):
        return f"Type : {self.__type}\nPseudo : {self.__pseudo}\nLien avec : {self.__lien}\nDate d'acquisition : {self.__date}\n"
    @property
    def getType(self):
        return self.__type
    @property
    def getPseudo(self):
        return self.__pseudo
    @property
    def getLien(self):
        return self.__lien
    @property
    def getDate(self):
        return self.__date
    @getType.setter
    def getType(self, valeur):
        self.__type = valeur
    @getPseudo.setter
    def getPseudo(self, valeur):
        self.__pseudo = valeur
    @getLien.setter
    def getLien(self, valeur):
        self.__lien = valeur
    @getDate.setter
    def getDate(self, valeur):
        self.__date = valeur


class entityEnq(): #Création d'une classe entité d'enquête qui va regroupé les liens et informations sur une enquêtes
    _next_EnqueteId = 101 #L'identifiant de la prochaine enquête ajoutée
    def __init__(self, enqNom, nivGravit, dateEnq = datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        self.__enqNom = enqNom #Nom de l'enquête, un pseudo donné pour y avoir une idée
        self.__dateEnq = dateEnq #Date précise du délit commit
        self.__nivGravit = nivGravit #Niveau de gravité des faits
        self.__typeEnq = typeInit(nivGravit)
        self.__enqueteId = entityEnq._next_EnqueteId #Identifiant de l'enquête
        entityEnq._next_EnqueteId += 1
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

#Corps principale
enq = [entityEnq("Attentat de Bruxelles", 7, "16-10-2023"),entityEnq("Prise d'otage à Sint-Pieter-Leeuw", 5)]
ville = [lieu("Bruxelles",1000,"Rue du Sabre 55"),lieu("Waterloo",1410,"Avenue bouchier 146")]
pers = [personne("Dupont","Mathieu",23,"Bruxlles Rue du feu 864","+32 478 45 73 21","Belge","34-85.654"),personne("Nemonné","Mathilde",29,"Anderlecht Boulevard Saint-Michel","+32 458 91 36 98","Belge","30-71.550")]
listeEnq = {}
