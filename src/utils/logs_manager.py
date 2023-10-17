import os
import logging
from colorlog import ColoredFormatter
from colorama import init
import tkinter as tk

init(autoreset=True)

class Logger:
    def __init__(self, log_directory="logs", text_widget=None):
        """
        Initialise un système de journalisation avec différents niveaux de journalisation et coloration en console.

        Args:
            log_directory (str): Le répertoire où les fichiers journaux seront enregistrés. Par défaut, "logs".
            text_widget (tk.Text): Le widget de zone de texte Tkinter pour afficher les journaux (optionnel).

        """
        os.makedirs(log_directory, exist_ok=True)
        
        self.log_directory = log_directory

        self.text_widget = text_widget
        self.text_widget.config(state=tk.DISABLED)

        log_levels = {
            'DEBUG': os.path.join(log_directory, 'debug.log'),
            'INFO': os.path.join(log_directory, 'info.log'),
            'WARNING': os.path.join(log_directory, 'warning.log'),
            'ERROR': os.path.join(log_directory, 'error.log'),
            'CRITICAL': os.path.join(log_directory, 'critical.log'),
        }

        self.loggers = {}
        for level, log_file in log_levels.items():
            logger = logging.getLogger(f"my_logger_{level}")
            logger.setLevel(getattr(logging, level))

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(getattr(logging, level))

            log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)

            logger.addHandler(file_handler)

            self.loggers[level] = logger

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
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
        
        for level, logger in self.loggers.items():
            logger.addHandler(console_handler)


    def debug(self, message):
        """
        Enregistre un message de débogage.

        Args:
            message (str): Le message à enregistrer.

        """
        self.loggers['DEBUG'].debug(message)
        self.display_in_text_widget(f"DEBUG: {message}")

    def info(self, message):
        """
        Enregistre un message d'information.

        Args:
            message (str): Le message à enregistrer.

        """
        self.loggers['INFO'].info(message)
        self.display_in_text_widget(f"INFO: {message}")

    def warning(self, message):
        """
        Enregistre un avertissement.

        Args:
            message (str): Le message à enregistrer.

        """
        self.loggers['WARNING'].warning(message)
        self.display_in_text_widget(f"WARNING: {message}")

    def error(self, message):
        """
        Enregistre un message d'erreur.

        Args:
            message (str): Le message à enregistrer.

        """
        self.loggers['ERROR'].error(message)
        self.display_in_text_widget(f"ERROR: {message}")

    def critical(self, message):
        """
        Enregistre un message critique.

        Args:
            message (str): Le message à enregistrer.

        """
        self.loggers['CRITICAL'].critical(message)
        self.display_in_text_widget(f"CRITICAL: {message}")

    def display_in_text_widget(self, message):
        """
        Affiche le message de journal dans un widget de zone de texte Tkinter.

        Args:
            message (str): Le message à afficher.

        """
        if self.text_widget:
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, message + '\n')
            self.text_widget.config(state=tk.DISABLED)

    def set_text_display(self, text_display):
        """
        Définit le widget de zone de texte Tkinter pour afficher les journaux.

        Args:
            text_display (tk.Text): Le widget de zone de texte Tkinter.

        """
        self.text_widget = text_display