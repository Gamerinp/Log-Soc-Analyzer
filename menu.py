import opciones

def menu_general():
    opcion = None
    while (opcion != 5):
        print("--------SOC ANALIZER--------")
        print("Buscar por usuario(1)")
        print("Buscar por ip(2)")
        print("Buscar por resultado(3)")
        print("Resumen de analisis(4)")
        print("Detener programa(5)\n")
        try:
            opcion = int(input("Elige la opcion: "))
            if opcion == 1:
                print("opcion 1 elegida")
                print(opciones.buscar_user(input("Escribe el usuario a buscar: ")))
            elif opcion == 2:
                print("opcion 2 elegida")
                print(opciones.buscar_ip(input("Escribe la ip a buscar: ")))
            elif opcion == 3:
                print("opcion 3 elegida")
                print(opciones.buscar_resultado(int(input("Elige una opcion:\nFailed(1)\nSucces(2)\n"))))
            elif opcion == 4:
                print("opcion 4 elegida")
                opciones.resumen()
        except ValueError:
            print("opcion invalida")

menu_general()