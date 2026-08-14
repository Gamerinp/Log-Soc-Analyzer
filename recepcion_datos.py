
def analizar_logs(archivo_logs: str):
    cantidad_lineas = 0
    # 'r' significa modo lectura (read)
    # encoding='utf-8' es una buena práctica para evitar problemas con acentos o caracteres
    # usar la instruccion with permite cerrar el archivo automaticamente (buena practica)
    with open(archivo_logs, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            cantidad_lineas += 1
            # .strip() quita el salto de línea '\n' al final de cada texto
            linea_limpia = linea.strip()
            #convertimos la linea de log en una lista separada por palabras
            lista_como_linea = linea_limpia.split()
            #separamos los logs con dato correcto, 8 elementos como lista
            if len(lista_como_linea) == 8:
                set_usuarios.add(lista_como_linea[3])
                dict_ip.update({lista_como_linea[3]:lista_como_linea[5]})

                if lista_como_linea[7] == "FAILED":
                    count_falied += 1
                    lista_sospechosos.append(lista_como_linea[3])
                else:
                    count_success += 1

    print('====== SECURITY REPORT ======\n')
    print(f'total de eventos: {cantidad_lineas}\n')
    print(f'Logs fallidos: {count_falied}')
    print(f'Logs exitosos: {count_success}\n')
    for nombre in set_usuarios:
        if lista_sospechosos.count(nombre) >= 3:
            print(f'usuario sospechoso: {nombre} con {lista_sospechosos.count(nombre)} logs fallidos')
            print(f'Ultima ip de acceso: {dict_ip[nombre]}')
            print("posible ataque de fuerza bruta")
    print('=============================')