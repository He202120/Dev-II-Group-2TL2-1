class Preuve:
    """
    Classe représentant une preuve dans le cadre d'une enquête.

    Cette classe permet de stocker différentes informations liées à une preuve.
    """

    def __init__(self, contexte="", notes="", type_preuve="", source="", liens=None):
        """
        Initialise une instance de la classe Preuve.

        PRE : Aucune.
        POST : Crée une nouvelle preuve avec les informations spécifiées.
        """
        self.contexte = contexte
        self.notes = notes
        self.type_preuve = type_preuve
        self.source = source
        self.liens = liens or []

    def contexte(self):
        """
        Récupère les informations sur le contexte de la preuve.

        PRE : Aucune.
        POST : Renvoie les informations enregistrées pour comprendre l'importance de la preuve dans le cadre de l'enquête.
        """
        return self.contexte

    def notes(self):
        """
        Récupère les remarques, observations ou détails supplémentaires liés à la preuve.

        PRE : Aucune.
        POST : Renvoie des informations complémentaires si nécessaires dans le cadre de l'enquête.
        """
        return self.notes

    def type_de_preuve(self):
        """
        Sélectionne le type de preuve parmi une liste de types prédéfinis.

        PRE : Aucune.
        POST : Enregistre le type de preuve pour faciliter la classification.
        """
        return self.type_preuve

    def source(self):
        """
        Indique la personne, l'endroit ou l'entité qui a fourni ou généré la preuve.

        PRE : Aucune.
        POST : Enregistre la source de la preuve pour assurer la traçabilité.
        """
        return self.source

    def liens(self):
        """
        Inclut des références ou des liens valides vers d'autres données ou sources liées à la preuve.

        PRE : Aucune.
        POST : Permet de connecter la preuve à d'autres informations pertinentes.
        """
        return self.liens
