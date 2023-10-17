import requests

from utils.logs_manager import logger
#from src.utils.logs_manager import logger


class Phase2:

    comon_password = []
    folder_path = "src/cache"

    def __init__(self) -> None:
        req = requests.get('https://nordpass.com/json-data/top-worst-passwords/findings/all.json')
        self.common_password = [item['Password'] for item in req.json()]
        logger.info(self.common_password)

    def save_as_text(self):
        try:
            with open(f"{self.folder_path}/dictionnaire.txt", "w") as file:
                for item in self.common_password:
                    file.write(f"{item}\n")
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde dans le fichier : {e}")
        finally:
            file.close()
    
    def read_file_to_list(self, file):
        if not len(self.common_password) <= 0:
            self.common_password = []
        try:
            with open(f"{self.folder_path}/{file}.txt", "r") as file:
                for line in file:
                    self.common_password.append(line.strip())
        except FileNotFoundError:
            logger.error(f"Le fichier {self.folder_path}/{file}.txt n'a pas été trouvé.")
        except Exception as e:
            logger.error(f"Une erreur s'est produite : {e}")


phase_2 = Phase2()
phase_2.save_as_text()