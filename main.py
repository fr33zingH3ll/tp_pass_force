from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.phase_4 import Phase4
from src.utils.my_lists import COMPLEMENTS, ID
from src.utils.logs_manager import logger

def main():
    ### phase 1 ###
    phase1 = Phase1()
    db_password = []
    db_password_old = phase1.data
    for item in db_password_old:
        db_password.append(item[1])
    db_password = set(db_password)
    ### phase 2 ###
    phase2 = Phase2()
    common_password = phase2.read_file_to_list("dictionnaire")

    ### phase 3 ###
    phase3 = Phase3()
    # test des mots de passe simple
    logger.info(f"mot de passe commun : {phase3.generate_combinations([common_password], db_password)}")
    # test des mots de passe avec XXXX 
    logger.info(f"mot de passe commun : {phase3.generate_combinations([common_password, ID], db_password)}")

if __name__=="__main__":
    main()