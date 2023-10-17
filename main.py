from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.phase_4 import Phase4

def main():
    ### phase 1 ###
    phase1 = Phase1()
    db_password = phase1.data
    
    ### phase 2 ###
    phase2 = Phase2()
    common_password = phase2.read_file_to_list("dictionnaire")

    ### phase 3 ###

if __name__=="__main__":
    main()