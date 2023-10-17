import os
import logging
from colorlog import ColoredFormatter
from colorama import init

init(autoreset=True)  # Initialise colorama pour la coloration en console

class Logger:
    """
    Classe pour gérer la journalisation avec différents niveaux de journalisation et coloration en console.

    Args:
        log_directory (str): Le répertoire où les fichiers journaux seront enregistrés. Par défaut, "logs".

    Exemple:
        Pour initialiser le journal avec des fichiers journaux dans le répertoire "my_logs" :
        logger = Logger(log_directory="my_logs")

        Pour enregistrer un message de débogage :
        logger.debug("Ceci est un message de débogage.")

        Pour enregistrer un message d'information :
        logger.info("Ceci est un message d'information.")

        Pour enregistrer un avertissement :
        logger.warning("Ceci est un avertissement.")

        Pour enregistrer un message d'erreur :
        logger.error("Ceci est un message d'erreur.")

        Pour enregistrer un message critique :
        logger.critical("Ceci est un message critique.")
    """

    def __init__(self, log_directory="logs"):
        # Assurez-vous que le répertoire de journaux existe
        os.makedirs(log_directory, exist_ok=True)

        # Créez un dictionnaire pour mapper les niveaux de journalisation aux fichiers
        log_levels = {
            'DEBUG': os.path.join(log_directory, 'debug.log'),
            'INFO': os.path.join(log_directory, 'info.log'),
            'WARNING': os.path.join(log_directory, 'warning.log'),
            'ERROR': os.path.join(log_directory, 'error.log'),
            'CRITICAL': os.path.join(log_directory, 'critical.log'),
        }

        # Configurez les gestionnaires de journalisation pour chaque niveau
        self.loggers = {}
        for level, log_file in log_levels.items():
            logger = logging.getLogger(f"my_logger_{level}")
            logger.setLevel(getattr(logging, level))

            # Créez un gestionnaire de fichier pour le niveau actuel
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(getattr(logging, level))

            # Créez un formateur pour les messages de journal avec des couleurs
            log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)

            logger.addHandler(file_handler)

            self.loggers[level] = logger

       # Créez un gestionnaire de console pour afficher les messages dans la console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Créez un formateur coloré pour les messages de la console avec colorama
        log_formatter = ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
        )
        console_handler.setFormatter(log_formatter)
        
        # Ajoutez le gestionnaire de console au logger
        for level, logger in self.loggers.items():
            logger.addHandler(console_handler)

    def debug(self, message):
        """
        Enregistre un message de débogage.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            logger.debug("Ceci est un message de débogage.")
        """
        self.loggers['DEBUG'].debug(message)

    def info(self, message):
        """
        Enregistre un message d'information.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            logger.info("Ceci est un message d'information.")
        """
        self.loggers['INFO'].info(message)

    def warning(self, message):
        """
        Enregistre un avertissement.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            logger.warning("Ceci est un avertissement.")
        """
        self.loggers['WARNING'].warning(message)

    def error(self, message):
        """
        Enregistre un message d'erreur.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            logger.error("Ceci est un message d'erreur.")
        """
        self.loggers['ERROR'].error(message)

    def critical(self, message):
        """
        Enregistre un message critique.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            logger.critical("Ceci est un message critique.")
        """
        self.loggers['CRITICAL'].critical(message)


logger = Logger("src/logs")