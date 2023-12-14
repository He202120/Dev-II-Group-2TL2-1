
class Enquete:
    def __init__(self, id, type="", niv_gravite=0, date):
        """
        Initialise une instance de la classe Enquete.

        PRE:
            - id, type doivent être des types valides.
            - niv_gravite doit être un nombre entier.
            - Le format de date doit être "Jour-Mois-Année".
        POST:
            - Une instance de la classe Enquete est créée avec les attributs spécifiés.
        """
        self.__type = type
        self.__niv_gravite = niv_gravite
        self.__date = ddate
        self.__id = id
        self.__liste_preuve = []

    def get_enquete_type(self):
        """
        Obtient le type d'une enquête (infractions, délits, crimes) grâce au niveau de gravité.

        PRE:
            - Aucun.
        POST:
            - Renvoie le type d'une enquête.
        """
        return self.__type

    def get_niv_gravite(self):
        """
        Permet de recevoir le degré de gravité.

        PRE:
            - Aucun.
        POST:
            - Renvoie le chiffre correspondant au niveau de gravité.
        """
        return self.__niv_gravite

    def get_date(self,date):
        """
        Obtient la date à laquelle on a ajouté l'enquête en question.

        PRE:
            - Le format de date doit être "Jour-Mois-Année".
        POST:
            - Renvoie True si le format est respecté, False sinon.
        """
        # Implémentez le code pour vérifier le format de la date
        pass

    def is_meme_addresse(self,autre):
        """
        Prends l'objet courant et un autre objet de la classe Enquete nous dit si les enquetes se trouvent dans la même ville
        
        PRE: 
            - Aucun
        POST:
            -Renvoie une chaine avec l'id des deux enquetes et nous dis si elles sont dans la même ville ainsi que le nom de la ville
        RAISES: 
            -Renvoie une erreur ParamExceptionError si autre n'est pas un objet de la classe Enquete.

        """
    
    def get_id(self):
        """
        Obtient l'id d'une enquête.

        PRE:
            - Aucun.
        POST:
            - Renvoie l'id d'une enquête.
        """
        return self.__id

    def get_liste_preuve(self):
        """
        Obtient la liste des preuves pour une enquête.

        PRE:
            - Aucun.
        POST:
            - Renvoie une liste de toutes les preuves pour une enquête.
        """
        return self.__liste_preuve
