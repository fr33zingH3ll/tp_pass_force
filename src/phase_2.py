import requests

class Phase2:
    def __init__(self, logger):
        """
        Initialise la Phase 2 de gestion de mots de passe.

        Cette classe gère le téléchargement et la sauvegarde des mots de passe courants à partir d'une source en ligne,
        ainsi que leur utilisation ultérieure.

        Args:
            logger (Logger): L'objet de journalisation pour enregistrer les messages.

        Exemple:
            phase2 = Phase2(logger)
        """
        self.logger = logger
        self.common_password = []
        self.folder_path = "src/cache"

        self.save_as_text()

    def save_as_text(self, file_name="dictionnaire", password_list=None):
        """
        Sauvegarde une liste de mots de passe dans un fichier texte.

        Args:
            file_name (str, optional): Le nom du fichier. Par défaut, "dictionnaire".
            password_list (list, optional): La liste de mots de passe à sauvegarder. Par défaut, utilise la liste
            `self.common_password`.

        Exemple:
            phase2.save_as_text(file_name="my_passwords", password_list=["password1", "password2"])
        """
        if not password_list:
            password_list = self.common_password
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
