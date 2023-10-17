def main():
    try:
        from phase_1 import Phase1
        from phase_2 import Phase2
        from phase_3 import Phase3
        from phase_4 import Phase4
        print("INFO : démarrage du script")
    except Exception as e:
        print("ERREUR : ", e)
    

if __name__=="__main__":
    main()