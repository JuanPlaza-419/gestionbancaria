import json
import os
from datetime import datetime, timedelta

BD = "usuarios.json"

def cargar_bd():
    if not os.path.exists(BD):
        with open(BD, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
    with open(BD, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_bd(data):
    with open(BD, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def crear_usuario():
    data = cargar_bd()
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    contraseña = input("Contraseña: ")

    for u in data:
        if u["dni"] == dni:
            print("Ese DNI ya está registrado.")
            return

    hoy = datetime.now().strftime("%Y-%m-%d")

    nuevo = {
        "nombre": nombre,
        "dni": dni,
        "password": contraseña,
        "saldo": 0,
        "historial": [],
        "pendientes": [],
        "cobradores": [],
        "bloqueado_hasta": "",
        "creado": hoy
    }

    data.append(nuevo)
    guardar_bd(data)
    print("Cuenta creada correctamente.")
