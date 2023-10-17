from src.utils.color_manager import Printer, INFO, WARNING, LOG, ERROR

class Phase:
    def __init__(self) -> None:
        self.printer = Printer()

    def finish(self):
        self.printer("initilization terminé avec succès", INFO)
    
    def error(self, e):
        self.printer(f"une erreur s'est produite pendant l'initialisation.\n{e}", ERROR)