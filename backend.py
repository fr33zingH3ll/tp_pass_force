from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.utils.my_lists import *

class Api:
    def __init__(self, logger) -> None:
        """
        Initialise l'API pour la gestion de mots de passe.

        Args:
            logger (Logger): Le gestionnaire de journaux pour enregistrer les messages.

        Attributes:
            logger (Logger): Le gestionnaire de journaux pour enregistrer les messages.
            phase1 (Phase1): Phase 1 pour le traitement des données.
            db_password (set): Ensemble de mots de passe à partir de la phase 1.
            phase2 (Phase2): Phase 2 pour la gestion des fichiers et dictionnaires.
            common_password (list): Liste de mots de passe communs depuis la phase 2.
            COMPLEMENTS (list): Liste de compléments (animaux, dates, etc.).
            ID (list): Liste d'identifiants.
            SPECIALS (list): Liste de caractères spéciaux.
            arguments (list): Liste des listes à utiliser pour les combinaisons.
            phase3 (Phase3): Phase 3 pour générer des combinaisons de mots de passe.
        """
        self.logger = logger
        self.phase1 = Phase1(self.logger)
        self.db_password = []
        self.db_password_old = self.phase1.data
        for item in self.db_password_old:
            self.db_password.append(item[0])
        self.db_password = set(self.db_password)
        self.phase2 = Phase2(self.logger)
        self.common_password = self.phase2.read_file_to_list("dictionnaire")
        self.COMPLEMENTS = COMPLEMENTS
        self.logger.error(self.COMPLEMENTS)
        self.ID = ID
        self.SPECIALS = SPECIALS
        self.arguments = []
        self.phase3 = Phase3()