class lieu():
    def __init__(self, codePostal="", ville="", rueNum="", nbrmaison=""):
        self.__ville = ville
        self.__codePostal = codePostal
        self.__rueNum = rueNum
        self.__nbrmaison = nbrmaison
        self.__latitude = self.lat()
        self.__longitude = self.long()

    def __str__(self):
        return f"Ville : {self.__ville} \nCode postal : {self.__codePostal} \nRue et numéro : {self.__rueNum} {self.__nbrmaison}"

    @property
    def getVille(self):
        return self.__ville

    @property
    def getCodePostal(self):
        return self.__codePostal

    @property
    def getRue(self):
        return self.__rueNum

    @property
    def getNum(self):
        return self.__nbrmaison

    @property
    def set_Lat_Long(self):
        self.__latitude = self.lat()
        self.__longitude = self.long()

    @getVille.setter
    def getVille(self, valeur):
        if isinstance(valeur, str):
            self.__ville = valeur
        else:
            print(ValueError)

    @getCodePostal.setter
    def getCodePostal(self, valeur):
            self.__codePostal = str(valeur)


    @getRue.setter
    def getRue(self, valeur):
        self.__rueNum = valeur

    @getNum.setter
    def getNum(self, valeur):
        self.__nbrmaison = valeur

    def lat(self):
        """
        Va modifier les attributs latitude et la longitude d'un endroit grâce aux attributs nom de la ville, le nom de la rue, et le numéro de maison qui sont stocké dans l'objet courant.

        PRE:
            - lors de l'initialisation, les attributs nom ville, nom rue et numero_maison doivent être correctement orthographiés et existés.
        POST:
            - Modifie l'objet courant pour y ajouter la latitude et la longitude d'un lieu dans leurs attributs respectifs.
        RAISES:
            -Renvoie une erreur ParamExceptionError si il y a une erreur dans les paramètres ou si aucun lieu n'a été trouvé.

        """
        # Initialiser le géocodeur Nominatim
        geolocator = Nominatim(user_agent="mon_script",scheme="https")

        nom_ville = self.__ville
        nom_rue = self.__rueNum
        numero_maison = self.__nbrmaison

        try:
            # Concaténer le nom de la ville, de la rue et le numéro de maison pour la recherche
            adresse_complete = f"{numero_maison} {nom_rue}, {nom_ville}"

            # Obtenir les coordonnées à partir de l'adresse complète
            location = geolocator.geocode(adresse_complete)

            if location:
                # Afficher les coordonnées
                return location.latitude
            else:
                return ""

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def long(self):
        """
        Va modifier les attributs latitude et la longitude d'un endroit grâce aux attributs nom de la ville, le nom de la rue, et le numéro de maison qui sont stocké dans l'objet courant.

        PRE:
            - lors de l'initialisation, les attributs nom ville, nom rue et numero_maison doivent être correctement orthographiés et existés.
        POST:
            - Modifie l'objet courant pour y ajouter la latitude et la longitude d'un lieu dans leurs attributs respectifs.
        RAISES:
            -Renvoie une erreur ParamExceptionError si il y a une erreur dans les paramètres ou si aucun lieu n'a été trouvé.

        """
        # Initialiser le géocodeur Nominatim
        geolocator = Nominatim(user_agent="mon_script",scheme="https")

        nom_ville = self.__ville
        nom_rue = self.__rueNum
        numero_maison = self.__nbrmaison

        try:
            # Concaténer le nom de la ville, de la rue et le numéro de maison pour la recherche
            adresse_complete = f"{numero_maison} {nom_rue}, {nom_ville}"

            # Obtenir les coordonnées à partir de l'adresse complète
            location = geolocator.geocode(adresse_complete)

            if location:
                # Afficher les coordonnées
                return location.longitude
            else:
                return ""

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def getmapEnq(self, id):
        """
        Crée une carte du monde se focalisant sur les attributs latitude et la longitude stocké dans l'objet courant pour stocker la carte dans un fichier html.

        PRE:
            - Aucun.
        POST:
            - Va creer un fichier portant l'id de l'objet courant et y stocker la carte.html.
        RAISES:
            -Renvoie une erreur NoLatLongError si l'objet courant ne possède pas de valeurs pour les attributs latitude et longitude.
        """
        if self.__latitude != "":
            # Coordonné GPS (latitude, longitude) de l'emplacement souhaité
            latitude = self.__latitude
            longitude = self.__longitude

            # Création de la carte
            ma_carte = folium.Map(location=[latitude, longitude], zoom_start=14)

            # Ajout d'un marqueur
            folium.Marker([latitude, longitude], popup='Mon Marqueur').add_to(ma_carte)

            # Sauvegarde de la carte au format HTML
            ma_carte.save(f"lieux-enquetes/{id}.html")
            print("La map a bien été crée")
        else:
            print("aucune latitude ou longitude n'ont été renseigné")

    def getmapPers(self, id):
        """
        Crée une carte du monde se focalisant sur les attributs latitude et la longitude stocké dans l'objet courant pour stocker la carte dans un fichier html.

        PRE:
            - Aucun.
        POST:
            - Va creer un fichier portant l'id de l'objet courant et y stocker la carte.html.
        RAISES:
            -Renvoie une erreur NoLatLongError si l'objet courant ne possède pas de valeurs pour les attributs latitude et longitude.
        """
        if self.__latitude != "":
            # Coordonné GPS (latitude, longitude) de l'emplacement souhaité
            latitude = self.__latitude
            longitude = self.__longitude

            # Création de la carte
            ma_carte = folium.Map(location=[latitude, longitude], zoom_start=14)

            # Ajout d'un marqueur
            folium.Marker([latitude, longitude], popup='Mon Marqueur').add_to(ma_carte)

            # Sauvegarde de la carte au format HTML
            ma_carte.save(f"lieux-personnes/{id}.html")
            print("La map a bien été crée")
        else:
            print("aucune latitude ou longitude n'ont été renseigné")
