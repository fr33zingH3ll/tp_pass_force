from src.utils.color_manager import Printer, INFO, WARNING, LOG, ERROR
printer = Printer()

def main():
    try:
        from src.phase_1 import Phase1
        from src.phase_2 import Phase2
        from src.phase_3 import Phase3
        from src.phase_4 import Phase4

        Phase1()
    except Exception as e:
        printer.print(e, ERROR)
    finally:
        printer.print("démarrage du script", INFO)
    

if __name__=="__main__":
    main()