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
    usuarios_failed = set()
    usuarios_succes = set()
    eventos = recepcion_datos.almacenar_logs("logs.txt") #[{'fecha_hora': '2026-08-11 08:00:12', 'usuario': 'admin', 'ip': '192.168.1.20', 'resultado': 'FAILED'}
    for evento in eventos:
        if op == 1:
            if evento["resultado"] == "FAILED":
                usuarios_failed.add(evento["usuario"])
        elif op == 2:
            if evento["resultado"] == "SUCCESS":
                usuarios_succes.add(evento["usuario"])
    if op == 1: return usuarios_failed
    elif op == 2: return usuarios_succes