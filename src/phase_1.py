from src.utils.database import MyDatabase
from src.utils.fields_options import IntegerOptions, TextOptions

class Phase1:
    def __init__(self, logger):
        """
        Initialise la Phase 1 de gestion de mots de passe.

        Cette classe gère la récupération des mots de passe depuis une base de données.

        Args:
            logger (Logger): L'objet de journalisation pour enregistrer les messages.

        Exemple:
            phase1 = Phase1(logger)
        """
        self.db = MyDatabase("./src/resources/tp_pass_force.db", logger)
        self.db.create_table("Password", {
            'id': IntegerOptions.integer_ai,
            'username': TextOptions.varchar,
            'password': TextOptions.varchar
        })

        # Chargez les données depuis la base de données pour l'analyse ultérieure
        self.data = self.db.get_data("Password", ["password"])
