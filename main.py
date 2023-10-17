from src.phase_1 import Phase1
from src.phase_2 import Phase2
from src.phase_3 import Phase3
from src.phase_4 import Phase4

from src.utils.logs_manager import Logger
logger = Logger(log_directory="src/logs")

def main():
    Phase1()
    

if __name__=="__main__":
    main()