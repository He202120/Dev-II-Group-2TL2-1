#Librairies

from classFile import *

# définitions

etatProg = True  # Définit l'état du programme
nextEnqueteId = 100  # L'identifiant de la prochaine enquête ajoutée
idPrs = 10100  # L'identifiant de la prochaine personne ajoutée
idPreu = 50100  # L'identifiant de la prochaine preuve ajoutée

# Dictionnaires

listeEnq = {}  # Dictionnaire des enquêtes, la valeur d'une clé est un tableau divisé en 4 tableaux (l'enquête crée, son lieu, l'id des personnes impliquées, un tableau de dictionnaire de preuve).
listePrs = {}  # Dictionnaire des personnes, leurs ids sont peuvent être lié à une enquête.

#Fonctions

def ajouter():
    global nextEnqueteId
    vNom = input("Introduire un nom pour l'enquête.\n")  # Variable du nom
    if vNom == "":
        raise NomVideException
    vGra = input(
        "Introduire le niveau de 1 à 9 de la gravité du problème. 1 ==> Le plus bas / 9 ==> Le plus haut\n")  # Variable du niveau de gravité
    if vGra == "" or int(vGra) > 9 or int(vGra) < 1 :
        raise GraviteVideException
    vDate = input(
        "Introduire une date d'initialisation. Inscrivez la dans un format 'Jour-Mois-Année Heure:Minute:Seconde'\n")
    if vDate == "":
        listeEnq[nextEnqueteId] = [entityEnq(nextEnqueteId, vNom, int(vGra))]  # Tableau de l'enquête
    else:
        listeEnq[nextEnqueteId] = [entityEnq(nextEnqueteId, vNom, int(vGra), vDate)]  # Tableau de l'enquête
    listeEnq[nextEnqueteId].append(
        lieu("Pas encodé", "Pas encodé", "Pas encodé","Pas encodé"))  # Tableau du lieu (données non-encodées)
    listeEnq[nextEnqueteId].append([])  # Tableau préventif pour y introduire des ids de personnes
    listeEnq[nextEnqueteId].append([])  # Tableau préventif pour y introduire des dictionnaires de preuves
    nextEnqueteId += 1
    os.system("cls")  # Fonction qui envoie une commande clear au terminal
    print("Enquête rajoutée avec succès.\n")

def enlever():
    vR = int(input("Introduire l'id de l'enquête à supprimer.\n"))  # Variable de l'id à supprimer
    if listeEnq == {}:
        raise ListeVideException
    if vR in listeEnq.keys():  # L'on cherche l'id dans le dictionnaire d'enquête
        del listeEnq[vR]
        os.system("cls")
        print("Enquête retirée avec succès.\n")
    else:
        raise ParamVideException

def modifierEnq():
    num = int(input("Inhtroduire l'id de l'enquête à modifier.\n"))
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
        listeEnq[num][0].typeInit()
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

def afficher(arg):
    if arg == "1":
        affEnq()
    elif arg == "2":
        affPers()
    else:
        raise ValueError

def affEnq():
    if listeEnq == {}:
        print("Liste d'enquête vide.\n")
    else:
        print("Nom Enquête   Identifiant   Date                Gravité des faits")
        for i in listeEnq.keys():
            print(listeEnq[i][0])  # Affiche la liste des enquête

def lieu_enq(id):
    os.system("cls")
    if id not in listeEnq.keys():
        raise ListeVideException
    tab = listeEnq[id][0].dataPr
    print(f"Nom : {tab[0]}\nId : {tab[1]}")
    print(listeEnq[id][1])
    chx = input("Voulez-vous modifier le lieu de cette enquête ? Tapez \"OUI\" pour le changer et MAP pour créer sa carte.\n")
    if chx == "OUI":
        print("Tapez ANNULER pour arrêter l'enregistrement et PASSER pour passer le paramètre.")
        vCode = input("Introduire le code postal.\n")  # Variable du code postal de la ville
        if vCode == "ANNULER":
            os.system("cls")
            print("Les modification ont été annuler.\n")
            return 0
        if vCode == "PASSER":
            vCode = 0
        vVille = input("Introduire une ville.\n")  # Variable du nom de la ville
        if vVille == "ANNULER":
            os.system("cls")
            print("Les modification ont été annuler.\n")
            return 0
        if vVille == "PASSER":
            vVille = "UNKNOWN"
        vRN = input("Introduire la rue.\n")  # Variable de la rue et le numéro du lieu
        if vRN == "ANNULER":
            os.system("cls")
            print("Les modification ont été annuler.\n")
            return 0
        if vRN == "PASSER":
            vRN = "UNKNOWN"
        vNum = input("Introduire le numéro de maison.\n")  # Variable de la rue et le numéro du lieu
        if vNum == "ANNULER":
            os.system("cls")
            print("Les modification ont été annuler.\n")
            return 0
        if vNum == "PASSER":
            vNum = "UNKNOWN"
        listeEnq[id][1].getVille = vVille
        listeEnq[id][1].getCodePostal = vCode
        listeEnq[id][1].getRue = vRN
        listeEnq[id][1].getNum = vNum
        os.system("cls")
        print("Nouvelle donnée enregistré.\n")
    else:
        os.system("cls")

def enq_map(id):
    os.system("cls")
    if int(id) not in listeEnq.keys():
        raise ListeVideException
    listeEnq[int(id)][1].set_Lat_Long
    listeEnq[int(id)][1].getmap(id)