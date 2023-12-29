class lieu():
    def __init__(self, codePostal="", ville="", rueNum="", nbrmaison=""):
        self.__ville = ville
        self.__codePostal = codePostal
        self.__rueNum = rueNum
        self.__nbrmaison = nbrmaison
        self.__latitude = 0
        self.__longitude = 0

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
    def get_lat(self):
        return self.__latitude

    @property
    def get_long(self):
        return self.__longitude

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

    def lat_long(self):
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
        geolocator = Nominatim(user_agent="mon_script", scheme="https")

        nom_ville = self.__ville
        nom_rue = self.__rueNum
        numero_maison = self.__nbrmaison

        # Concaténer le nom de la ville, de la rue et le numéro de maison pour la recherche
        adresse_complete = f"{numero_maison} {nom_rue}, {nom_ville}"

        # Obtenir les coordonnées à partir de l'adresse complète
        location = geolocator.geocode(adresse_complete)

        if location:
            # Afficher les coordonnées
            self.__latitude = location.latitude
            self.__longitude = location.longitude
        else:
            raise MauvaiseValeurException



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
        if self.__latitude != 0:
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
            raise MauvaiseValeurException

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
        if self.__latitude != 0:
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
            raise MauvaiseValeurException
