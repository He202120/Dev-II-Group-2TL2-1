from MVP import *
import cmd, sys
import os

class EnqueteShell(cmd.Cmd):
    intro = "Bienvenu sur notre gestionnaire d'enquête.   Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = '(Utilisateur) '
    file = None

    # ----- basic enquete commands -----

    def do_enquete(self, arg):
        "// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //\n//                      Unnamed software version 1.0                                   //\n//                                                                                     //\n// 'ajouter' : Permet d'enregistrer une nouvelle enquête de données vide               //\n//                                                                                     //\n// 'enlever' : Permet d'éffacer une enquête ainsi que ses données                      //\n//                                                                                     //\n// 'modifier' : Permet de modifier les données d'une enquête                           //\n//  Certaines fonctions nécessite d'introduire l'id d'une enquête ou d'une personne    //\n//                                                                                     //\n// 'afficher' : Afficher les données d'une catégorie (enquête, personne, etc           //\n//                                                                                     //\n// 'OFF' : Arrêter le programme                                                        //\n//                                                                                     //\n// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //"

        if arg == "ajouter":
            try:
                ajouter()
            except ParamVideException:
                print(f"Vous n'avez pas rentré de nom d'enquete")
        elif arg == "enlever":
            enlever()
        elif arg == "modifier":
            modifier()
        elif arg == "afficher":
            afficher()
        else:
            os.system("cls")
            print('Mauvais paramètre')
            EnqueteShell().cmdloop()
        EnqueteShell().cmdloop()

    def do_afficher(self,id):
        "Affiche-les enquêtes"
        print("liste des enquete")

    def do_enqueteur(self,arg):
        "Gérer les enquêteurs."
        print("liste des enqueteurs")

    def do_suspect(self,arg):
        "Gérer les suspects"
        print("liste des suspects")

    def do_lieu(self,arg):
        "Gérer les lieux"
        print("liste des lieux")

    def do_reset(self, line):
        'Run a shell commande'
        os.system("cls")

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print("Merci davoir utilisé notre gestionnaire enquête")
        return True



if __name__ == '__main__':
    EnqueteShell().cmdloop()
