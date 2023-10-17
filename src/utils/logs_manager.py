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
        >>> logger = Logger(log_directory="my_logs")

        Pour enregistrer un message de débogage :
        >>> logger.debug("Ceci est un message de débogage.")

        Pour enregistrer un message d'information :
        >>> logger.info("Ceci est un message d'information.")

        Pour enregistrer un avertissement :
        >>> logger.warning("Ceci est un avertissement.")

        Pour enregistrer un message d'erreur :
        >>> logger.error("Ceci est un message d'erreur.")

        Pour enregistrer un message critique :
        >>> logger.critical("Ceci est un message critique.")
    """

    def __init__(self, log_directory="logs"):
        os.makedirs(log_directory, exist_ok=True)
        
        # ...

    def debug(self, message):
        """
        Enregistre un message de débogage.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            >>> logger.debug("Ceci est un message de débogage.")
        """
        self.loggers['DEBUG'].debug(message)

    def info(self, message):
        """
        Enregistre un message d'information.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            >>> logger.info("Ceci est un message d'information.")
        """
        self.loggers['INFO'].info(message)

    def warning(self, message):
        """
        Enregistre un avertissement.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            >>> logger.warning("Ceci est un avertissement.")
        """
        self.loggers['WARNING'].warning(message)

    def error(self, message):
        """
        Enregistre un message d'erreur.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            >>> logger.error("Ceci est un message d'erreur.")
        """
        self.loggers['ERROR'].error(message)

    def critical(self, message):
        """
        Enregistre un message critique.

        Args:
            message (str): Le message à enregistrer.

        Exemple:
            >>> logger.critical("Ceci est un message critique.")
        """
        self.loggers['CRITICAL'].critical(message)
