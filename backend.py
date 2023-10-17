from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.utils.my_lists import *

class Api:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.phase1 = Phase1(self.logger)
        self.db_password = []
        self.db_password_old = self.phase1.data
        for item in self.db_password_old:
            self.db_password.append(item[0])
        self.db_password = set(self.db_password)
        self.phase2 = Phase2(self.logger)
        self.common_password = self.phase2.read_file_to_list("dictionnaire")
        self.COMPLEMENTS = COMPLEMENTS
        self.logger.error(self.COMPLEMENTS)
        self.ID = ID
        self.SPECIALS = SPECIALS
        self.arguments = []
        self.phase3 = Phase3()
    