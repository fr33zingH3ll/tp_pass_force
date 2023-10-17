import os
import logging
from colorlog import ColoredFormatter
from colorama import init
import tkinter as tk

init(autoreset=True)  # Initialise colorama pour la coloration en console

class Logger:
    def __init__(self, log_directory="logs", text_widget=None):
        os.makedirs(log_directory, exist_ok=True)
        
        self.log_directory = log_directory

        self.text_widget = text_widget
        self.text_widget.config(state=tk.DISABLED)

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
        self.display_in_text_widget(f"DEBUG: {message}")

    def info(self, message):
        self.loggers['INFO'].info(message)
        self.display_in_text_widget(f"INFO: {message}")

    def warning(self, message):
        self.loggers['WARNING'].warning(message)
        self.display_in_text_widget(f"WARNING: {message}")

    def error(self, message):
        self.loggers['ERROR'].error(message)
        self.display_in_text_widget(f"ERROR: {message}")

    def critical(self, message):
        self.loggers['CRITICAL'].critical(message)
        self.display_in_text_widget(f"CRITICAL: {message}")

    def display_in_text_widget(self, message):
        if self.text_widget:
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, message + '\n')
            self.text_widget.config(state=tk.DISABLED)
    
    def set_text_display(self, text_display):
        self.text_widget = text_display
