def main():
    try:
        from src.utils.color_manager import Printer, INFO, WARNING, LOG, ERROR
        printer = Printer()

        from phase_1 import Phase1
        from phase_2 import Phase2
        from phase_3 import Phase3
        from phase_4 import Phase4
        print("démarrage du script", INFO)
    except Exception as e:
        print(e, ERROR)
    

if __name__=="__main__":
    main()