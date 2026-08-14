
def almacenar_logs(archivo_logs: str):
    # 'r' significa modo lectura (read)
    # encoding='utf-8' es una buena práctica para evitar problemas con acentos o caracteres
    # usar la instruccion with permite cerrar el archivo automaticamente (buena practica)
    eventos = []
    with open("logs.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(" | ")  # Usar " | " te da 4 partes limpias
            if len(partes) == 4:
                fecha_hora, usuario, ip, resultado = partes
                # Guardas cada log como un diccionario sencillo
                eventos.append({
                    "fecha_hora": fecha_hora,
                    "usuario": usuario,
                    "ip": ip,
                    "resultado": resultado
                })
    return eventos