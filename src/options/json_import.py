from tkinter import filedialog
import json
import shutil

def is_valid_json(data):
    # Vérifie si le JSON a uniquement des entrées dans le format { "password": "valeur" }
    for entry in data:
        if not isinstance(data[entry], str) or not entry.startswith("password_"):
            return False
    return True

def importer_json(logger):
    # Ouvrir une boîte de dialogue pour sélectionner un fichier JSON
    filename = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])

    if filename:
        # Lire le contenu du fichier JSON
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                logger.error("Erreur de décodage JSON. Le fichier n'est pas au format JSON valide.")
                return
                
            # Vérifier la validité du JSON
            if not is_valid_json(data):
                logger.error("Le fichier JSON ne contient pas des entrées dans le format requis (password_[numéro de l'entrée]).")
                return

            logger.info(f"Fichier JSON importé : {filename}")
            logger.info("Contenu du fichier :")
            logger.info(json.dumps(data, indent=4))

        # Copier le fichier JSON vers un répertoire spécifique dans le projet
        destination_folder = "src/cache"
        shutil.copy(filename, destination_folder)
        logger.info(f"Fichier JSON copié vers : {destination_folder}")