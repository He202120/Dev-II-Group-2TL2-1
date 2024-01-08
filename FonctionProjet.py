from ClassProjet import *


def ajouter():
    vNom = input("Introduire un nom pour l'enquête.\n")  # Variable du nom
    if vNom == "":
        raise NomVideException
    try:
        vGra = int(input("Introduire le niveau de 1 à 9 de la gravité du problème. 1 ==> Le plus bas/9 ==> Le plus haut\n"))
    except ValueError:
        raise GraviteVideException
    if vGra > 9 or vGra < 1:
        raise GraviteVideException
    vDate = input(
        "Introduire une date d'initialisation. Inscrivez la dans un format 'Jour-Mois-Année Heure:Minute:Seconde'\n")
    if vDate == "":
        nv_obj = entityEnq(vNom, int(vGra))
        listeEnq[nv_obj.get_id_enq] = [nv_obj]  # Tableau de l'enquête
        listeEnq[nv_obj.get_id_enq].append(lieu())  # Tableau du lieu (données non-encodées)
        listeEnq[nv_obj.get_id_enq].append([])  # Tableau préventif pour y introduire des ids de personnes
        listeEnq[nv_obj.get_id_enq].append([])  # Tableau préventif pour y introduire des dictionnaires de preuves
    else:
        nv_obj = entityEnq(vNom, int(vGra), vDate)
        listeEnq[nv_obj.get_id_enq] = [nv_obj]  # Tableau de l'enquête
        listeEnq[nv_obj.get_id_enq].append(lieu())  # Tableau du lieu (données non-encodées)
        listeEnq[nv_obj.get_id_enq].append([])  # Tableau préventif pour y introduire des ids de personnes
        listeEnq[nv_obj.get_id_enq].append([])  # Tableau préventif pour y introduire des listes de preuves

    os.system("cls")  # Fonction qui envoie une commande clear au terminal
    print("Enquête rajoutée avec succès.\n")


def enlever():
    os.system("cls")
    affEnq()
    try:
        vR = int(input("Introduire l'id de l'enquête à supprimer.\n"))  # Variable de l'id à supprimer
    except ValueError:
        raise MauvaisIdException
    if listeEnq == {}:
        os.system("cls")
        print("Il n'y a encore aucune enquête encoder.\n")
        return 0
    if vR in listeEnq.keys():  # L'on cherche l'id dans le dictionnaire d'enquête
        del listeEnq[vR]
        os.system("cls")
        print("Enquête retirée avec succès.\n")
        return 0

    else:
        os.system("cls")
        raise MauvaisIdException

def histoEnq():
    try:
        num = int(input("Introduire l'id de l'enquête pour voir son historique.\n"))
    except ValueError:
        raise MauvaisIdException
    if num in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
        os.system("cls")
        print(listeEnq[num][0].historique)
        input("Continuez ?")
        os.system("cls")        
    else:
        print("Cette enquête n'existe pas")

def enqueteMod():
    try:
        num = int(input("Introduire l'id de l'enquête que vous souhaitiez modifier.\n"))
    except ValueError:
        raise MauvaisIdException
    if num in listeEnq.keys():  # On regarde si l'id se trouve dans le dictionnaire d'enquête
        try:
            mod = int(input("Que voulez-vous modifier? Tapez : 1 pour le Nom / 2 pour le Niveau de gravité"
                            " / 3 pour la Date \n"))
        except ValueError:
            raise ParamVideException

        if mod not in range(1, 4):
            raise ParamVideException
    else:
        raise MauvaisIdException

    if mod == 1:
        nom = input("Introduire un nouveau nom. Tapez n'importe quoi d'autre pour annuler\n")  # Modification du nom
        if nom == "":
            raise NomVideException
        listeEnq[num][0].addHistorique({'nom':nom,'fnom':listeEnq[num][0].get_enq_nom,'date':datetime.today().strftime('%d-%m-%y %H:%M:%S')})
        listeEnq[num][0].get_enq_nom = nom
        os.system("cls")
        print("Modification réussite.\n")
    elif mod == 2:
        try:
            num_grav = int(input("Introduire un niveau de gravitez de 1 - 9 (1 est le moins important).\n"))
        except ValueError:
            raise ParamVideException
        if 0 < int(num_grav) < 10:
            listeEnq[num][0].addHistorique({'gravite':num_grav,'fgravite':listeEnq[num][0].get_niv_gravit,'date':datetime.today().strftime('%d-%m-%y %H:%M:%S')})
            listeEnq[num][0].get_niv_gravit = num_grav
        else:
            raise GraviteVideException
        os.system("cls")
        print("Modification réussite.\n")
    elif mod == 3:
        datem = input("Introduire une nouvelle date (jj-mm-AAAA)\n")
        try:
            datetime.strptime(datem, "%d-%m-%Y")
        except ValueError:
            raise MauvaisDateException
        listeEnq[num][0].addHistorique({'fdate':listeEnq[num][0].get_enq_date,'ndate':datem,'date':datetime.today().strftime('%d-%m-%y %H:%M:%S')})
        listeEnq[num][0].get_enq_date = datem
        os.system("cls")
        print("Modification réussite.\n")


def ajouter_enqueteur():
    nom = input("Quel est le nom de l'enquêteur?\n")
    if nom == "":
        raise ParamVideException
    prenom = input("Quel est le prénom de l'enquêteur?\n")
    nv_enqueteur = Enqueteur(nom, prenom)
    listePrs[nv_enqueteur.getId] = nv_enqueteur
    os.system("cls")
    print("l'enquêteur a bien été enregistré")


def ajouter_suspect():
    nom = input("Quel est le nom du suspect ?\n")
    if nom == "":
        raise ParamVideException
    prenom = input("Quel est le prénom du suspect ?\n")
    alibi = input("Quel est l'alibi du suspect ?\n")
    nv_suspect = Suspect(nom, prenom, alibi)
    listeSus[nv_suspect.getId] = nv_suspect
    os.system("cls")
    print("le suspect a bien été enregistré")


def afficher_enqueteur():
    os.system("cls")
    if listePrs == {}:
        print("Liste d'enquêteur vide.\n")
    else:
        print("Liste des enquêteurs")
        print("--------------------------------")
        for i in listePrs.values():
            print(i)  # Affiche la liste des enquêtes
            print("--------------------------------")


def afficher_suspect():
    os.system("cls")
    if listeSus == {}:
        print("Liste des suspects vide.\n")
    else:
        print("Liste des suspects")
        print("--------------------------------")
        for i in listeSus.values():
            print(i)
            print("--------------------------------")


def supprimer_enqueteur():
    os.system("cls")
    try:
        num_enqueteur = int(input("Quel est l'id de l'enquêteur que vous voulez supprimer\n"))
    except ValueError:
        raise ParamVideException
    try:
        num_enquete = int(input("A quelle id enquête voulez supprimer cet enquêteur?\n"))
    except ValueError:
        raise ParamVideException
    if num_enquete not in listeEnq.keys():
        raise ParamVideException
    for j in range(len(listeEnq[num_enquete][2])):
        if listeEnq[num_enquete][2][j] == num_enqueteur:
            del listeEnq[num_enquete][2][j]
    os.system("cls")
    print(f"l'enquêteur : {num_enqueteur} a bien été supprimé à l'enquête : {num_enquete} ")


def supprimer_suspect():
    os.system("cls")
    try:
        num_suspect = int(input("Quel est l'id du suspect que vous voulez supprimer\n"))
    except ValueError:
        raise ParamVideException
    try:
        num_enquete = int(input("A quelle id enquête voulez supprimer cet enquêteur?\n"))
    except ValueError:
        raise ParamVideException
    if num_enquete not in listeEnq.keys():
        raise ParamVideException
    for j in range(len(listeEnq[num_enquete][2])):
        if listeEnq[num_enquete][2][j] == num_suspect:
            del listeEnq[num_enquete][2][j]
    os.system("cls")
    print(f"l'enquêteur : {num_suspect} a bien été supprimé à l'enquête : {num_enquete} ")


def modifer_enqueteur():
    os.system("cls")
    try:
        num_enqueteur = int(input("Quel est l'id de l'enquêteur que vous voulez modifier\n"))
    except ValueError:
        raise ParamVideException
    if num_enqueteur not in listePrs.keys():
        raise ListeVideException
    nom = input("Quel est le nom de l'enquêteur?\n")
    if nom == "":
        raise ParamVideException
    prenom = input("Quel est le prénom de l'enquêteur?\n")
    listePrs[num_enqueteur].get_prenom = prenom
    listePrs[num_enqueteur].get_nom = nom
    os.system("cls")
    print(f"l'enquêteur : {num_enqueteur} a bien été modifié avec le nom {nom} et {prenom}")


def modifer_suspect():
    os.system("cls")
    try:
        num_suspect = int(input("Quel est l'id du suspect que vous voulez modifier\n"))
    except ValueError:
        raise ParamVideException
    if num_suspect not in listeSus.keys():
        raise ListeVideException
    nom = input("Quel est le nom du suspect ?\n")
    if nom == "":
        raise ParamVideException
    prenom = input("Quel est le prénom du suspect ?\n")
    alibi = input("Quel est l'alibi du suspect ?\n")
    listeSus[num_suspect].get_prenom = prenom
    listeSus[num_suspect].get_nom = nom
    listeSus[num_suspect].get_alibi = alibi
    os.system("cls")
    print(f"le suspect : {num_suspect} a bien été modifié avec le nom {nom} et {prenom} et l'alibi {alibi}")


def associer_enqueteur():
    os.system("cls")
    try:
        num_enqueteur = int(input("Quel est l'id de l'enquêteur que vous voulez associer\n"))
    except ValueError:
        raise ParamVideException
    if num_enqueteur not in listePrs.keys():
        raise ListeVideException
    try:
        num_enquete = int(input("A quelle id enquête voulez rajouter cet enquêteur?\n"))
    except ValueError:
        raise ParamVideException
    if num_enquete not in listeEnq.keys():
        raise ParamVideException
    listeEnq[num_enquete][2].append(num_enqueteur)
    os.system("cls")
    print(f"l'enquêteur : {num_enqueteur} a bien été associé à l'enquête : {num_enquete} ")


def associer_suspect():
    os.system("cls")
    try:
        num_suspect = int(input("Quel est l'id du suspect que vous voulez associer\n"))
    except ValueError:
        raise ParamVideException
    if num_suspect not in listeSus.keys():
        raise ListeVideException
    try:
        num_enquete = int(input("A quelle id enquête voulez rajouter cet enquêteur?\n"))
    except ValueError:
        raise ParamVideException
    if num_enquete not in listeEnq.keys():
        raise ParamVideException
    listeEnq[num_enquete][3].append(num_suspect)
    os.system("cls")
    print(f"le suspect : {num_suspect} a bien été associé à l'enquête : {num_enquete} ")


def afficher(arg):
    if arg == "1":
        affEnq()
    elif arg == "2":
        afficher_suspect()
    elif arg == "3":
        afficher_enqueteur()
    else:
        raise ValueError


def affEnq():
    if listeEnq == {}:
        print("Liste d'enquête vide.\n")
    else:
        print("Liste des enquêtes")
        print("---------------------------------------------------")
        for i in listeEnq.keys():
            print(listeEnq[i][0])  # Affiche la liste des enquêtes
            print(listeEnq[i][1])
            print(f"Liste des ids des enquêteurs: {listeEnq[i][2]}")
            print(f"Liste des ids des suspects: {listeEnq[i][3]}")


def affPers():
    if listePrs == {}:  # On regarde si la liste est vide
        print("Liste des personnes vide.\n")
        return 0
    for i in listePrs.keys():
        print(listePrs[i])


def lieu_enq(id):
    os.system("cls")
    if id not in listeEnq.keys():
        raise ListeVideException
    tab = listeEnq[id][0].dataPr
    print(f"Id : {tab[1]}\nNom : {tab[0]}")
    print(listeEnq[id][1])
    chx = input("Voulez-vous modifier le lieu de cette enquête ? Tapez OUI ou NON\n")
    if chx == "OUI":
        try:
            vCode = int(input("Introduire le code postal.\n"))  # Variable du code postal de la ville
        except ValueError:
            raise MauvaiseValeurException

        vVille = input("Introduire une ville.\n")  # Variable du nom de la ville
        vRN = input("Introduire la rue.\n")  # Variable de la rue et le numéro du lieu

        try:
            vNum = int(input("Introduire le numéro de maison.\n"))  # Variable de la rue et le numéro du lieu
        except ValueError:
            raise MauvaiseValeurException

        listeEnq[id][1].getVille = vVille
        listeEnq[id][1].getCodePostal = vCode
        listeEnq[id][1].getRue = vRN
        listeEnq[id][1].getNum = vNum
        os.system("cls")
        print("Nouvelle donnée enregistré.\n")
    elif chx == "NON":
        raise ValueError
    else:
        os.system("cls")
        print("Le paramètre renseigné ne convient pas")


def enq_map(id):
    os.system("cls")
    if int(id) not in listeEnq.keys():
        raise ListeVideException
    listeEnq[int(id)][1].set_Lat_Long
    listeEnq[int(id)][1].getmapEnq(id)
