import recepcion_datos
def buscar_ip(ip:str):
    count= {"failed":0, "success":0}
    eventos = recepcion_datos.almacenar_logs("logs.txt") #[{'fecha_hora': '2026-08-11 08:00:12', 'usuario': 'admin', 'ip': '192.168.1.20', 'resultado': 'FAILED'}
    for evento in eventos:
        if evento["ip"] == ip and evento["resultado"] == "FAILED":
                count["failed"] += 1
        elif evento["ip"] == ip and evento["resultado"] == "SUCCESS":
                count["success"] += 1
    return count

def buscar_user(user:str):
    count= {"failed":0, "success":0}
    eventos = recepcion_datos.almacenar_logs("logs.txt") #[{'fecha_hora': '2026-08-11 08:00:12', 'usuario': 'admin', 'ip': '192.168.1.20', 'resultado': 'FAILED'}
    for evento in eventos:
        if evento["usuario"] == user and evento["resultado"] == "FAILED":
                count["failed"] += 1
        elif evento["usuario"] == user and evento["resultado"] == "SUCCESS":
                count["success"] += 1
    return count

def buscar_resultado(op:int):
    try:
        usuarios = set()
        eventos = recepcion_datos.almacenar_logs("logs.txt") #[{'fecha_hora': '2026-08-11 08:00:12', 'usuario': 'admin', 'ip': '192.168.1.20', 'resultado': 'FAILED'}
        for evento in eventos:
            if op == 1:
                if evento["resultado"] == "FAILED":
                    usuarios.add(evento["usuario"])
            elif op == 2:
                if evento["resultado"] == "SUCCESS":
                    usuarios.add(evento["usuario"])
        return usuarios
    except ValueError:
        print("El opcion invalida")

def resumen():
    eventos = recepcion_datos.almacenar_logs("logs.txt")
    count_fail = 0
    count_success = 0
    set_usuarios = set()
    lista_usuarios = []
    ip_sospechosa = set()
    lista_usuarios_atacantes = []
    for evento in eventos:
        if evento["resultado"] == "FAILED":
            lista_usuarios.append(evento["usuario"])
            set_usuarios.add(evento["usuario"])
            count_fail += 1
        if evento["resultado"] == "SUCCESS":
            count_success += 1
    for nombre in set_usuarios:
        if lista_usuarios.count(nombre) >= 3:
            lista_usuarios_atacantes.append(nombre)
            for evento in eventos:
                if evento["usuario"] == nombre:
                    ip_sospechosa.add(evento["ip"])

    print('====== SECURITY REPORT ======\n')
    print(f'total de eventos: {len(eventos)}\n')
    print(f'Logs fallidos: {count_fail}')

    print(f'Logs exitosos: {count_success}\n')
    print(f'usuarios sospechosos:{lista_usuarios_atacantes}')
    print(f'ip de sospechosos: {ip_sospechosa}')
    print('=============================')

if __name__ == "__main__":
    buscar_ip("192.168.1.50")
    buscar_user("admin")
    buscar_resultado(1)
    buscar_resultado(2)
    buscar_resultado(3)
    resumen()
