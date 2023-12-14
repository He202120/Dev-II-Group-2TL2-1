class Personne(Date):
    def __init__(self, nom, prenom, date_naissance, id_nationalite, code_postal, rue, numero_maison):
        """
        Initialise une instance de la classe Personne.

        PRE:
            - nom, prenom, date_naissance, id_nationalite, code_postal, rue, numero_maison doivent être des types valides.
        POST:
            - Une instance de la classe Personne est créée avec les attributs spécifiés.
        """
        self.dateobj = Date.__init__(self.date_naissance)
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_nationalite = id_nationalite
        self.code_postal = code_postal
        self.rue = rue
        self.numero_maison = numero_maison

    def set_age(self, jour_annif, mois_annif, annee_annif):
        """
        Modifie la date de naissance d'une personne qui se trouve dans les attributs Jour, Mois, Année interne à l'objet dateobj de classe Date.

        PRE:
            - 
        POST:
            - Modifie l'attribut dateobj qui est un objet de classe Date stocké dans l'objet courant par les paramètre de cette fonction jour_annif, mois_annif, annee_annif.
        RAISES:
            - Renvoie une erreur ParamExceptionError si les attributs ne respectent pas les conditions ou que la date se trouve dans le futur.
        """
        # Implémentez le code pour modifier la date de naissance
        pass

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
        # Implémentez le code pour calculer l'âge
        pass

    def get_nationalite(self):
        """
        Obtient la nationalité d'une personne grâce à l'id nationalité de la personne.

        PRE:
            - Aucun.
        POST:
            - Renvoie la nationalité de la personne.
        """
        # Implémentez le code pour obtenir la nationalité
        pass

    def nom_complet(self):
        """
        Renvoie le nom et le prénom d'une personne en une phrase.

        PRE:
            - Aucun.
        POST:
            - Renvoie une chaîne représentant le nom et le prénom d'une personne.
        """
        return f"{self.nom} {self.prenom}"

    def get_adresse(self):
        """
        Obtient l'adresse complète d'une personne grâce à son code postal, sa rue, son numéro de maison.

        PRE:
            - Aucun.
        POST:
            - Renvoie une chaîne représentant l'adresse d'une personne.
        """
        return f"{self.numero_maison}, {self.rue}, {self.code_postal}"
