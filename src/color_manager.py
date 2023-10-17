

class Printer:
    """
    Classe pour afficher des messages colorés dans la console en utilisant des codes de couleurs ANSI.

    exemple d'utilisation: 
        my_printer = Printer()
        my_printer.print("Ceci est un message d'erreur.", Printer.ERROR)
        my_printer.print("Ceci est un message d'info.", Printer.INFO)
        my_printer.print("Ceci est un message de log.", Printer.LOG)
        my_printer.print("Ceci est un warning.", Printer.WARNING)
        my_printer.print("Ceci est un message sans type prédéfinies.")
    """
    INFO = { "message": "INFO : ", "color": "\033[34m" }
    ERROR = { "message": "ERROR : ", "color": "\033[31m" }
    LOG = { "message": "LOG : ", "color": "\033[32m" }
    WARNING = { "message": "WARNING : ", "color": "\033[33m" }
    NOT_DEFINED = { "message": "NOT DEFINED : ", "color": "\033[37m" }

    ALL = [
        INFO, 
        WARNING, 
        LOG, 
        ERROR,
    ]

    def __init__(self):
        """
        Initialise l'instance de la classe Printer avec les types de message disponibles.
        """

    def print(self, text, msg_type = None):
        """
        Affiche un message coloré dans la console en ajoutant automatiquement le type de message.

        Args:
            msg_type (dict): Le type de message avec les clés "message" et "color" (utilisez les constantes de la classe, par exemple, Printer.ERROR).
            text (str): Le texte à afficher.
        """

        if msg_type == None or msg_type not in Printer.ALL:
            msg_type = Printer.NOT_DEFINED
        print(f"{msg_type['color']}{msg_type['message']}{text}\033[0m")
