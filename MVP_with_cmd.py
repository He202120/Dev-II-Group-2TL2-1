import os
import cmd, sys
from MVP import *
def demande():
    la = input("vvvx")
    lo = input("cscqscqs")

class EnqueteShell(cmd.Cmd):
    intro = "Bienvenu sur notre gestionnaire d'enquête.   Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = '(Utilisateur) '
    file = None

    # ----- basic enquete commands -----

    def do_enquete(self, arg):
        "// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //\n//                      Unnamed software version 1.0                                   //\n//                                                                                     //\n// 'ajouter' : Permet d'enregistrer une nouvelle enquête de données vide               //\n//                                                                                     //\n// 'enlever' : Permet d'éffacer une enquête ainsi que ses données                      //\n//                                                                                     //\n// 'modifier' : Permet de modifier les données d'une enquête                           //\n//  Certaines fonctions nécessite d'introduire l'id d'une enquête ou d'une personne    //\n//                                                                                     //\n// 'afficher' : Afficher les données d'une catégorie (enquête, personne, etc           //\n//                                                                                     //\n// 'OFF' : Arrêter le programme                                                        //\n//                                                                                     //\n// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //"

        if arg == "ajouter":
            ajouter()
        elif arg == "enlever":
            enlever()
        elif arg == "modifier":
            modifier()
        elif arg == "afficher":
            afficher()
        else:
            print('Mauvais paramètre')
            EnqueteShell().cmdloop()
        EnqueteShell().cmdloop()
      
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    EnqueteShell().cmdloop()
