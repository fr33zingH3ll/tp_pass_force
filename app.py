import tkinter as tk
from tkinter.scrolledtext import ScrolledText  
from src.utils.logs_manager import Logger
from src.options.json_import import importer_json
from src.phase_3 import generate_combinations, arguments 
from src.utils.my_lists import ALLS

class MaFenetre(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Ma Fenêtre Tkinter")
        self.geometry("700x700")

        self.create_widgets()

        self.logger = Logger("src/logs", text_widget=self.textbox)
        self.password_list = {}

        self.create_menu()

    def create_widgets(self):
        self.label = tk.Label(self, text="Sélectionnez les options :")
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        self.widgets = []  # Liste pour stocker les widgets créés

        for i, option in enumerate(ALLS):
            if option == "ALGOS":
                # Créer une liste d'options pour ALGOS
                algos_options = [algo for algo in ALLS["ALGOS"]]
                selected_algo = tk.StringVar()  # Variable pour stocker l'option sélectionnée
                selected_algo.set(algos_options[0])  # Définir la première option comme sélectionnée par défaut

                algos_menu = tk.OptionMenu(self, selected_algo, *algos_options)
                algos_menu.grid(row=1, column=i+1)
                self.widgets.append((option, algos_menu, selected_algo))
            else:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self, text=option, variable=var)
                checkbox.grid(row=1, column=i+1)
                self.widgets.append((option, checkbox, var))

        self.textbox = ScrolledText(self, wrap=tk.WORD)
        self.textbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.button = tk.Button(self, text="Obtenir la sélection", command=self.get_selection)
        self.button.grid(row=3, column=0, columnspan=4, pady=10)


    def create_menu(self):
        self.menu_principal = tk.Menu(self)
        self.config(menu=self.menu_principal)

        self.option1_menu = tk.Menu(self.menu_principal, tearoff=0)
        self.option1_menu.add_command(label="Importer JSON", command=lambda: self.json_import())
        self.option1_menu.add_checkbutton(label="Sous-option 1B", variable=tk.BooleanVar())
        self.option1_menu.add_checkbutton(label="Sous-option 1C", variable=tk.BooleanVar())

        self.option2_menu = tk.Menu(self.menu_principal, tearoff=0)
        self.option2_menu.add_checkbutton(label="Sous-option 2A", variable=tk.BooleanVar())
        self.option2_menu.add_checkbutton(label="Sous-option 2B", variable=tk.BooleanVar())
        self.option2_menu.add_checkbutton(label="Sous-option 2C", variable=tk.BooleanVar())

        self.menu_principal.add_cascade(label="Option 1", menu=self.option1_menu)
        self.menu_principal.add_cascade(label="Option 2", menu=self.option2_menu)

    def json_import(self):
        self.password_list = importer_json(self.logger)

    def get_selection(self):
        arguments.clear()  # Efface les arguments précédents à chaque appel
        self.textbox.delete(1.0, tk.END)

        for option, widget, var in self.widgets:
            if isinstance(widget, tk.Checkbutton) and var.get():
                if option in ALLS:
                    arguments.append(ALLS[option])
                    self.logger.info(f"Ajout de la liste {option}")
                else:
                    self.logger.warning(f"Option {option} non prise en charge")

        # Traiter les sélections des listes déroulantes
        for option, widget, var in self.widgets:
            if isinstance(widget, tk.OptionMenu):
                selected_option = var.get()
                # Ajouter le code pour gérer les sélections des listes déroulantes
                if selected_option == "": self.logger.info(f"Sélection dans la liste déroulante {option}: None")
                else: self.logger.info(f"Sélection dans la liste déroulante {option}: {selected_option}")
        self.logger.info(f"mot de passe commun : {generate_combinations(arguments, self.password_list, hash=selected_option)}")
                


if __name__ == "__main__":
    app = MaFenetre()
    app.mainloop()
