class Lieu:
    def creer_map(self):
        """
        Crée une carte du monde se focalisant sur les attributs latitude et la longitude stocké dans l'objet courant pour stocker la carte dans un fichier html.

        PRE:
            - Aucun.
        POST:
            - Va creer un fichier portant l'id de l'objet courant et y stocker la carte.html.
        RAISES:
            -Renvoie une erreur NoLatLongError si l'objet courant ne possède pas de valeurs pour les attributs latitude et longitude.
        """
        # Implémentez le code pour créer la carte
        pass

    def lat_long(self, nom_ville, nom_rue, numero_maison):
        """
        Va modifier les attributs latitude et la longitude d'un endroit grâce aux attributs nom de la ville, le nom de la rue, et le numéro de maison qui sont stocké dans l'objet courant.

        PRE:
            - lors de l'initialisation, les attributs nom ville, nom rue et numero_maison doivent être correctement orthographiés et existés.
        POST:
            - Modifie l'objet courant pour y ajouter la latitude et la longitude d'un lieu dans leurs attributs respectifs.
        RAISES:
            -Renvoie une erreur ParamExceptionError si il y a une erreur dans les paramètres ou si aucun lieu n'a été trouvé.
        
        """
        # Impl
