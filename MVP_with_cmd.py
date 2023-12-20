#Librairies
from functionsFile import *
import cmd, sys
import os

class EnqueteShell(cmd.Cmd):
    os.system("cls")
    intro = "Bienvenu sur notre gestionnaire d'enquête.   Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = '(Utilisateur) '
    file = None

    # ----- basic enquete commands -----

    def do_enquete(self, arg):
        "// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //\n//                         taper enquete <attribut>                                    //\n//                                                                                     //\n// 'ajouter' : Permet d'enregistrer une nouvelle enquête de données vide               //\n//                                                                                     //\n// 'enlever' : Permet d'éffacer une enquête ainsi que ses données                      //\n//                                                                                     //\n// 'modifier' : Permet de modifier les données d'une enquête                           //\n// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //"

        if arg == "ajouter":
            try:
                ajouter()
            except NomVideException:
                os.system("cls")
                print("Vous n'avez pas rentré de nom d'enquete")
            except GraviteVideException:
                os.system("cls")
                print("Vous n'avez pas rentré de niveau gravité")
        elif arg == "enlever":
            try:
                enlever()
            except ListeVideException:
                os.system("cls")
                print("Il n'y a aucune enquête dans la liste.")
            except ParamVideException:
                os.system("cls")
                print("L'id renseigné n'existe pas.")
        elif arg == "modifier":
            modifierEnq()
        else:
            os.system("cls")
            print("Mauvais paramètre tapez <help enquete> pour plus d'information")

    def do_afficher(self,id):
        "// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //\n//                         taper afficher <attribut>                                   //\n//                                                                                     //\n//    '1'   : Permet d'afficher  la liste des enquêtes déjà encodées                   //\n//                                                                                     //\n//    '2'   : Permet d'afficher la liste des suspects déjà encodés                     //\n//                                                                                     //\n// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //"
        try:
            afficher(id)
        except ValueError:
            os.system("cls")
            print("Mauvais paramètre tapez <help afficher> pour plus d'information")

    def do_enqueteur(self,arg):
        "Gérer les enquêteurs."
        print("liste des enqueteurs")

    def do_suspect(self,arg):
        "Gérer les suspects"
        print("liste des suspects")

    def do_lieu(self,arg):
        "// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //\n//                         taper lieu <attribut> <id>                                  //\n//                                                                                     //\n//    'enquetes' :  Permet d'afficher le lieu pour une enquete avec l'<id>             //\n//                                                                                     //\n//    'suspectes' : Permet d'afficher le lieu pour un suspect avec l'<id>              //\n//                                                                                     //\n// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //"
        a = ""
        h = ""
        try:
            a, h = [s for s in arg.split()]
        except ValueError:
            os.system("cls")
            print("Les arguments rentrés sont érronés")
        if a == "enquetes":
            try:
                lieu_enq(int(h))
            except ListeVideException:
                os.system("cls")
                print("Aucune n'enquête ne possède cet id.")
        elif a == "suspects":
            print(h)
            #lieu_sus(h)
        elif a == "map":
            try:
                enq_map(str(h))
            except ListeVideException:
                os.system("cls")
                print("Aucune n'enquête ne possède cet id.")
        else:
            os.system("cls")
            print("Mauvais paramètre tapez <help lieu> pour plus d'information")

    def do_reset(self, line):
        'Run a shell commande'
        os.system("cls")

    def do_bye(self, arg):
        'Ferme le programme'
        print("Merci davoir utilisé notre gestionnaire enquête")
        return True

#Corps principale

if __name__ == '__main__':
    EnqueteShell().cmdloop()
