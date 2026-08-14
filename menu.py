def menu_general():
    while (True):
        print("--------SOC ANALIZER--------")
        print("buscar por usuario(1)")
        print("buscar por ip(2)")
        print("buscar por resultado(3)")
        print("resumen de analisis(4)")
        try:
            opcion = int(input("elige la opcion: "))
            if opcion == 1:
                print("opcion 1 elegida")
            elif opcion == 2:
                print("opcion 2 elegida")
            elif opcion == 3:
                print("opcion 3 elegida")
            elif opcion == 4:
                print("opcion 4 elegida")
        except ValueError:
            print("opcion invalida")