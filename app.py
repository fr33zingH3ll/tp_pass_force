import tkinter as tk
from tkinter.scrolledtext import ScrolledText  # Importez ScrolledText
from src.utils.logs_manager import Logger
from backend import Api

class MaFenetre(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Ma Fenêtre Tkinter")

        # Créer une variable pour chaque case à cocher
        self.var_mot_de_passe = tk.BooleanVar()
        self.var_id = tk.BooleanVar()
        self.var_couleur = tk.BooleanVar()
        self.var_special = tk.BooleanVar()

        self.label = tk.Label(self, text="Sélectionnez les options :")
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        # Créer les cases à cocher
        self.check_mot_de_passe = tk.Checkbutton(self, text="Mot de passe commun", variable=self.var_mot_de_passe)
        self.check_id = tk.Checkbutton(self, text="ID", variable=self.var_id)
        self.check_couleur = tk.Checkbutton(self, text="Couleur", variable=self.var_couleur)
        self.check_special = tk.Checkbutton(self, text="Special", variable=self.var_special)

        # Placer les cases à cocher dans la grille
        self.check_mot_de_passe.grid(row=1, column=0)
        self.check_id.grid(row=1, column=1)
        self.check_couleur.grid(row=1, column=2)
        self.check_special.grid(row=1, column=3)

        # Créez une zone de texte redimensionnable avec des barres de défilement
        self.textbox = ScrolledText(self, wrap=tk.WORD)  # Utilisez ScrolledText
        self.textbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # Ajuster la taille de la fenêtre
        self.update_idletasks()
        self.geometry(f"{self.textbox.winfo_reqwidth()}x{self.winfo_reqheight()}")

        # Créer un bouton
        self.button = tk.Button(self, text="Obtenir la sélection", command=self.get_selection)
        self.button.grid(row=3, column=0, columnspan=4, pady=10)

        self.logger = Logger("src/logs", text_widget=self.textbox)
        self.api = Api(self.logger)

    def get_selection(self):
        # Récupérer les valeurs des cases à cocher
        
        mot_de_passe = self.var_mot_de_passe.get()
        id = self.var_id.get()
        couleur = self.var_couleur.get()
        special = self.var_special.get()

        # Effacer le contenu actuel de la zone de texte
        self.textbox.delete(1.0, tk.END)

        # Afficher les résultats dans la zone de texte
        self.api.arguments = []
        if mot_de_passe:
            self.api.arguments.append(self.api.common_password)
            self.logger.info("ajout de la liste common_password")
        elif self.api.common_password in self.api.arguments:
            self.api.arguments.remove(self.api.common_password)
            self.logger.info("suppression de la liste common_password")
        if id:
            self.api.arguments.append(self.api.ID)
            self.logger.info("ajout de la liste id")
        elif self.api.COMPLEMENTS in self.api.arguments:
            self.api.arguments.remove(self.api.ID)
            self.logger.info("suppression de la liste id")
        if couleur:
            self.api.arguments.append(self.api.COMPLEMENTS)
            self.logger.info("ajout de la liste couleur")
        elif self.api.ID in self.api.arguments:
            self.api.arguments.remove(self.api.COMPLEMENTS)
            self.logger.info("suppression de la liste couleur")
        if special:
            self.api.arguments.append(self.api.SPECIALS)
            self.logger.info("ajout de la liste specials")
        elif self.api.SPECIALS in self.api.arguments:
            self.api.arguments.remove(self.api.SPECIALS)
            self.logger.info("suppression de la liste specials")

        self.logger.warning(self.api.arguments)
        self.logger.warning(self.api.db_password)
        self.logger.info(f"mot de passe commun : {self.api.phase3.generate_combinations(self.api.arguments, self.api.db_password)}")
        

if __name__ == "__main__":
    app = MaFenetre()
    app.mainloop()
