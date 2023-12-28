from FonctionProjet import *
import cmd
import os

class EnqueteShell(cmd.Cmd):
    os.system("cls")
    intro = "Bienvenu sur notre gestionnaire d'enquête.  Tapez help ou ? to pour afficher la liste des commandes.\n"
    prompt = '(Utilisateur) '
    file = None

    # ----- basic enquete commands -----

    def do_enquete(self, arg):
        """
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        //                         taper enquete <attribut>                                    //
        //                                                                                     //
        // 'ajouter' : Permet d'enregistrer une nouvelle enquête de données vide               //
        //                                                                                     //
        // 'enlever' : Permet d'effacer une enquête ainsi que ses données                      //
        //                                                                                     //
        // 'modifier' : Permet de modifier les données d'une enquête                           //
        //                                                                                     //
        //  Certaines fonctions nécessitent d'introduire l'id d'une enquête ou d'une personne  //
        //                                                                                     //
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        """

        if arg == "ajouter":
            try:
                ajouter()
            except NomVideException:
                os.system("cls")
                print("Vous n'avez pas rentré de nom d'enquête")
            except GraviteVideException:
                os.system("cls")
                print("Le niveau de gravité renseigné ne convient pas")
        elif arg == "enlever":
            try:
                enlever()
            except MauvaisIdException:
                os.system("cls")
                print("L'id renseigné n'existe pas")
        elif arg == "modifier":
            os.system("cls")
            affEnq()
            try:
                enqueteMod()
            except NomVideException:
                os.system("cls")
                print("Vous n'avez pas rentré de nom d'enquête")
            except MauvaisIdException:
                os.system("cls")
                print("L'id renseigné n'existe pas")
            except ParamVideException:
                os.system("cls")
                print("Le paramètre renseigné ne convient pas")
            except GraviteVideException:
                os.system("cls")
                print("Le niveau de gravité renseigné ne convient pas")
            except MauvaisDateException:
                os.system("cls")
                print("La date renseigné ne convient pas")
        else:
            os.system("cls")
            print("Mauvais paramètre tapez <help enquete> pour plus d'information")

    def do_afficher(self,id):
        """
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        //                         taper afficher <attribut>                                   //
        //                                                                                     //
        //    '1'   : Permet d'afficher la liste des enquêtes déjà encodées                    //
        //                                                                                     //
        //    '2'   : Permet d'afficher la liste des suspects déjà encodés                     //
        //                                                                                     //
        //    '3'   : Permet d'afficher la liste des enquêteurs déjà encodés                   //
        //                                                                                     //
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        """
        try:
            afficher(id)
        except ValueError:
            os.system("cls")
            print("Mauvais paramètre tapez <help afficher> pour plus d'information")


    def do_enqueteur(self,arg):
        """
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        //                         taper enqueteur <attribut> <id>                             //
        //                                                                                     //
        //    'creer'   : Permet d'enregistrer un enquêteur                                    //
        //                                                                                     //
        //    'associer'   : Permet d'associer un enquêteur à une enquête <id>                 //
        //                                                                                     //
        //    'modifier'   : Permet de modifier le nom ou le prénom d'un enquêteur             //
        //                                                                                     //
        //    'supprimer'  : Permet de supprimer un enquêteur d'une enquête                    //
        //                                                                                     //
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        """

        if arg == "creer":
            try:
                ajouter_enqueteur()
            except ParamVideException:
                os.system("cls")
                print("Le nom de l'enquêteur doit être renseigné")
        elif arg == "associer":
            try:
                associer_enqueteur()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id de l'enquête n'existe pas ou n'est pas valide")
        elif arg == "supprimer":
            try:
                supprimer_enqueteur()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id de l'enquête n'existe pas ou n'est pas valide")
        elif arg == "modifier":
            try:
                modifer_enqueteur()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id de l'enquête n'existe pas ou n'est pas valide")
        else:
            os.system("cls")
            print("Mauvais paramètre tapez <help afficher> pour plus d'information")

    def do_suspect(self, arg):
        """
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        //                         taper suspect <attribut> <id>                               //
        //                                                                                     //
        //    'creer'   : Permet d'enregistrer un suspect                                      //
        //                                                                                     //
        //    'associer'   : Permet d'associer un suspect à une enquête <id>                   //
        //                                                                                     //
        //    'modifier'   : Permet de modifier le nom ou le prénom d'un suspect               //
        //                                                                                     //
        //    'supprimer'  : Permet de supprimer un suspect d'une enquête                      //
        //                                                                                     //
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        """

        if arg == "creer":
            try:
                ajouter_suspect()
            except ParamVideException:
                os.system("cls")
                print("Le nom du suspect doit être renseigné")
        elif arg == "associer":
            try:
                associer_suspect()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id du suspect n'existe pas ou n'est pas valide")
        elif arg == "supprimer":
            try:
                supprimer_suspect()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id de l'enquête n'existe pas ou n'est pas valide")
        elif arg == "modifier":
            try:
                modifer_suspect()
            except ListeVideException:
                print("Aucune n'enquête ne possède cet id.")
            except ParamVideException:
                print("L'id de l'enquête n'existe pas ou n'est pas valide")
        else:
            os.system("cls")
            print("Mauvais paramètre tapez <help afficher> pour plus d'information")

    def do_lieu(self, arg):
        """
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        //                         taper lieu <attribut> <id>                                  //
        //                                                                                     //
        //    'enquetes' :  Permet d'afficher le lieu pour une enquete avec l'<id>             //
        //                                                                                     //
        //    'suspectes' : Permet d'afficher le lieu pour un suspect avec l'<id>              //
        //                                                                                     //
        //    'map' : Permet de creer un fichier html contenant la carte d'un lieu             //
        //                                                                                     //
        // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
        """

        a = ""
        h = ""
        try:
            a, h = [s for s in arg.split()]
        except ValueError:
            os.system("cls")
            print("Les arguments rentrés sont erronés")
        if a == "enquetes":
            try:
                lieu_enq(int(h))
            except ListeVideException:
                os.system("cls")
                print("Aucune n'enquête ne possède cet id.")
            except ValueError:
                os.system("cls")
                print("Aucun lieu n'a été modifié")
            except MauvaiseValeurException:
                os.system("cls")
                print("le paramètre renseigné n'est pas valide")
        elif a == "suspects":
            print(h)
            # lieu_sus(h)
        elif a == "map":
            try:
                enq_map(str(h))
            except ListeVideException:
                os.system("cls")
                print("Aucune n'enquête ne possède cet id.")
            except ValueError:
                print("Aucune n'enquête ne possède cet id.")

    def do_reset(self, line):
        'Run a shell commande'
        os.system("cls")

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print("Merci davoir utilisé notre gestionnaire enquête")
        return True

    def emptyline(self):
        # Cette méthode est appelée lorsque l'utilisateur appuie simplement sur Enter
        os.system("cls")
        print("tapez <help> pour plus d'information")
        pass

if __name__ == '__main__':
    EnqueteShell().cmdloop()