class personne(Dates):
    def __init__(self, nom="", prenom="", addr=lieu(), age=0, tel="", nationalite="", idNationalite=""):
        super().__init__()
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__addr = addr  # Adresse de la personne
        self.__tel = tel
        self.__nation = nationalite  # Nom de la nationalité
        self.__identityCode = idNationalite  # numéro de registre de la carte d'identité
        self.__id = 0

    def __str__(self):
        return f"Profil : {self.__id} / {self.__nom} {self.__prenom}\nAge : {self.__age}\nAdresse domicile : {self.__addr.getVille}\nTel. : {self.__tel}\nNationalité et code d'identité : {self.__nation} {self.__identityCode}\n"

    def __eq__(self, autre):
        return self.__addr.getVille == autre.getAdrr.getVille

    @property
    def getNom(self):
        return self.__nom

    @property
    def getPrenom(self):
        return self.__prenom


    @property
    def getmap(self):
        try:
            self.__addr.getmapPers(self.__id)
        except ParamVideException:
            print("aucune latitude et longitude renseigné")

    @property
    def getAdrr(self):
        return self.__addr

    @property
    def get_age(self):
        """
               Calcule l'âge de la personne en utilisant la date actuelle et sa date de naissance.

               PRE:
                   - Aucun
               POST:
                   - Renvoie un entier représentant l'âge de la personne calculé en années en utilisant les attributs Jour, Mois, Année et dateactuel stocké dans l'objet dateobj
               RAISES:
                   - Renvoie une erreur ValueError si la date de naissance de la personne est dans le futur.
               """
        today = datetime.today()
        annee_courante = today.strftime('%Y')
        return int(annee_courante) - self.get_annee

    @property
    def getTel(self):
        return self.__tel

    @property
    def getNat(self):
        return self.__nation

    @property
    def getIdC(self):
        return self.__id


    @getNom.setter
    def getNom(self, valeur):
        if isinstance(valeur, str):
            self.__nom = valeur


    @getAdrr.setter
    def getAdrr(self,valeur):
        if isinstance(valeur, object):
            self.__addr = valeur
        else:
            raise ValueError("addresse renseignée n'est pas un objet")

    @getPrenom.setter
    def getPrenom(self, valeur):
        if isinstance(valeur, str):
            self.__prenom = valeur

    def set_age(self, valeur):
        """
        Modifie la date de naissance d'une personne qui se trouve dans les attributs Jour, Mois, Année interne à l'objet dateobj de classe Date.

        PRE:
            -
        POST:
            - Modifie l'attribut dateobj qui est un objet de classe Date stocké dans l'objet courant par les paramètre de cette fonction jour_annif, mois_annif, annee_annif.
        RAISES:
            - Renvoie une erreur ParamExceptionError si les attributs ne respectent pas les conditions ou que la date se trouve dans le futur.
        """
        today = datetime.today()
        annee_courante = today.strftime('%Y')
        try:
            dates = datetime.strptime(valeur, "%d-%m-%Y")
        except ValueError:
            raise MauvaisDateException
        except TypeError:
            raise MauvaisDateException
        if dates.year > int(annee_courante):
            raise MauvaisDateException
        self.get_annee = dates.year
        self.get_mois = dates.month
        self.get_jour = dates.day

    @getTel.setter
    def getTel(self, valeur):
        self.__Tel = valeur

    @getNat.setter
    def getNat(self, valeur):
        if isinstance(valeur, str):
            self.__nation = valeur

    @getIdC.setter
    def getIdC(self, valeur):
        self.__id = valeur
