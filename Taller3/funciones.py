import random
import json
import csv
from pymongo import MongoClient

# ---------------------- FORMATOS ----------------------

def form_id(n):
    return f"REG-{n:03d}"

def form_fr(edad):
    return random.randint(12, 20)

def form_fc(fc):
    return fc

def form_spo2(spo2):
    return spo2

# ---------------------- VALIDACIÓN ----------------------

def validar(r):
    return (
        12 <= r["fr"] <= 20 and
        50 <= r["fc"] <= 140 and
        85 <= r["spo2"] <= 100
    )

# ---------------------- GENERAR REGISTRO ----------------------

def generar_registro(n):
    edad = random.randint(18, 90)
    fc = random.randint(50, 140)
    spo2 = random.randint(85, 100)
    return {
        "id": form_id(n),
        "fr": form_fr(edad),
        "fc": form_fc(fc),
        "spo2": form_spo2(spo2)
    }

def generar_registros_validos():
    lista = []
    for i in range(1, 51):
        r = generar_registro(i)
        if validar(r):
            lista.append(r)
    return ordenar_por_fc(lista)

# ---------------------- ORDENAMIENTO ----------------------

def ordenar_por_fc(lista):
    return sorted(lista, key=lambda x: x["fc"])

# ---------------------- INGRESO MANUAL ----------------------

def ingresar_manual():
    print("\n--- Ingresar Registro Manual ---")
    idr = input("ID (ej: REG-999): ")
    fr = int(input("FR (12-20): "))
    fc = int(input("FC (50-140): "))
    spo2 = int(input("SpO2 (85-100): "))

    return {
        "id": idr,
        "fr": fr,
        "fc": fc,
        "spo2": spo2
    }

# ---------------------- GUARDADO ----------------------

def guardar_txt(registros):
    with open("data/txt/registros.txt", "w") as f:
        for r in registros:
            f.write(str(r) + "\n")
    print("✔ Guardado en TXT")

def guardar_csv(registros):
    with open("data/csv/registros.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id","fr","fc","spo2"])
        w.writeheader()
        w.writerows(registros)
    print("✔ Guardado en CSV")

def guardar_json(registros):
    with open("data/json/registros.json", "w") as f:
        json.dump(registros, f, indent=4)
    print("✔ Guardado en JSON")

def guardar_todo(registros):
    guardar_txt(registros)
    guardar_csv(registros)
    guardar_json(registros)

# ---------------------- IMPORTAR ----------------------

def importar_json():
    with open("data/json/registros.json", "r") as f:
        return json.load(f)

# ---------------------- MONGO LOCAL ----------------------

def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["taller3"]
        col = db["registros"]
        return col
    except Exception as e:
        print("Error:", e)
        return None

# ---------------------- CRUD MONGO ----------------------

def menu_mongo(registros):
    col = conectar_mongo()
    if col is None:
        print("✖ No se pudo conectar a MongoDB.")
        return

    while True:
        print("\n--- MongoDB ---")
        print("1. Insertar registros")
        print("2. Ver registros")
        print("3. Actualizar un registro")
        print("4. Eliminar un registro")
        print("5. Volver")

        op = input("Opción: ")

        if op == "1":
            col.insert_many(registros)
            print("✔ Insertados en MongoDB.")

        elif op == "2":
            for r in col.find():
                print(r)

        elif op == "3":
            rid = input("ID a actualizar: ")
            nuevo_fc = int(input("Nuevo FC: "))
            col.update_one({"id": rid}, {"$set": {"fc": nuevo_fc}})
            print("✔ Actualizado.")

        elif op == "4":
            rid = input("ID a eliminar: ")
            col.delete_one({"id": rid})
            print("✔ Eliminado.")

        elif op == "5":
            break

        else:
            print("Opción inválida.")

             
