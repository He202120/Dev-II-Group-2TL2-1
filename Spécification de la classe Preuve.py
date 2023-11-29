from datetime import datetime

class Preuve:
    def __init__(self, id, type="", pseudo="", ddate=datetime.today().strftime('%d-%m-%y %H:%M:%S')):
        """
        Initialise une instance de la classe Preuve.

        PRE:
            - id, type, pseudo doivent être des types valides.
            - Le format de date doit être "Jour-Mois-Année".
        POST:
            - Une instance de la classe Preuve est créée avec les attributs spécifiés.
        """
        self.__type = type
        self.__pseudo = pseudo
        self.__date = ddate
        self.__pId = id

    def get_type(self):
        """
        Obtient le type d'une preuve en fonction du pseudo.

        PRE:
            - Aucune condition préalable.
        POST:
            - Renvoie le type d'une preuve.
        """
        return self.__type

    def get_pseudo(self):
        """
        Obtient le nom d'une preuve en fonction du type.

        PRE:
            - Aucune condition préalable.
        POST:
            - Renvoie le nom de la preuve.
        """
        return self.__pseudo

    def get_date(self):
        """
        Obtient la date à laquelle on a ajouté la preuve en question.

        PRE:
            - Le format de date doit être "Jour-Mois-Année".
        POST:
            - Renvoie True si le format est respecté, False sinon.
        """
        # Implémentez le code pour vérifier le format de la date
        pass

    def get_id(self):
        """
        Obtient l'id d'une preuve.

        PRE:
            - Aucune condition préalable.
        POST:
            - Renvoie l'id d'une preuve.
        """
        return self.__pId

    def get_lieu(self):
        """
        Permet d'avoir le lieu où a été trouvée une preuve.

        PRE:
            - Aucune condition préalable.
        POST:
            - Renvoie une chaîne représentant le lieu.
        """
        # Implémentez le code pour obtenir le lieu
        pass
