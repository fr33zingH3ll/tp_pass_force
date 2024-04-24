def save_as_text(self, password_list, file_name="dictionnaire"):
    """
    Sauvegarde une liste de mots de passe dans un fichier texte.

    Args:
        file_name (str, optional): Le nom du fichier. Par défaut, "dictionnaire".
        password_list (list, optional): La liste de mots de passe à sauvegarder. Par défaut, utilise la liste
        `self.common_password`.

    Exemple:
        phase2.save_as_text(file_name="my_passwords", password_list=["password1", "password2"])
    """
    try:
        with open(f"{self.folder_path}/{file_name}.txt", "w") as file:
            for item in password_list:
                file.write(f"{item}\n")
    except Exception as e:
        self.logger.error(f"Erreur lors de la sauvegarde dans le fichier : {e}")
    finally:
        file.close()

def read_file_to_list(self, file):
    """
    Lit un fichier texte contenant une liste de mots de passe et retourne cette liste.

    Args:
        file (str): Le nom du fichier à lire.

    Returns:
        list: Une liste de mots de passe lue à partir du fichier.

    Exemple:
        password_list = phase2.read_file_to_list("my_passwords")
    """
    if not len(self.common_password) <= 0:
        self.common_password = []
    try:
        with open(f"{self.folder_path}/{file}.txt", "r") as file:
            for line in file:
                self.common_password.append(line.strip())
    except FileNotFoundError:
        self.logger.error(f"Le fichier {self.folder_path}/{file}.txt n'a pas été trouvé.")
    except Exception as e:
        self.logger.error(f"Une erreur s'est produite : {e}")
    return self.common_password
