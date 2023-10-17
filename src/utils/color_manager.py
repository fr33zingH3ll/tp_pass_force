import os
import logging
from colorlog import ColoredFormatter
from colorama import init

init(autoreset=True)  # Initialise colorama pour la coloration en console

class Logger:
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
        self.loggers['DEBUG'].debug(message)

    def info(self, message):
        self.loggers['INFO'].info(message)

    def warning(self, message):
        self.loggers['WARNING'].warning(message)

    def error(self, message):
        self.loggers['ERROR'].error(message)

    def critical(self, message):
        self.loggers['CRITICAL'].critical(message)

if __name__ == "__main__":
    log_directory = "src/logs/"  # Spécifiez le répertoire souhaité pour les journaux
    logger = Logger(log_directory)

    logger.debug("Ceci est un message de débogage.")
    logger.info("Ceci est un message d'information.")
    logger.warning("Ceci est un avertissement.")
    logger.error("Ceci est un message d'erreur.")
    logger.critical("Ceci est un message critique.")

