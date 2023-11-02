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
#classes
class lieu():
    def __init__(self, ville = "", codePostal = 1000):
        self.__ville = ville
        self.__codePostal = codePostal
    def __str__(self):
        return f"Ville : {self.__ville} \nCode postal : {self.__codePostal} \n"

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
ville = [lieu("Bruxelles",1000),lieu("Waterloo",1410)]
print(enq[0])
print(enq[1])
print(ville[0])