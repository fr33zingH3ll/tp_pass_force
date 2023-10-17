from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.utils.my_lists import *
from src.utils.logs_manager import logger

def main():
    """
    Fonction principale pour le test des phases de gestion de mots de passe.

    Cette fonction effectue les opérations suivantes :
    1. Récupère les mots de passe de la phase 1.
    2. Récupère les mots de passe communs de la phase 2.
    3. Effectue des tests de mots de passe simples et avec des ID de la phase 3.

    Args:
        Aucun.

    Returns:
        Aucun.

    Exemple:
        Pour exécuter la fonction principale :
        main()
    """
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

if __name__ == "__main__":
    main()