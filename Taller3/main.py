from funciones import *

def main():
    registros = []

    while True:
        print("\n--- Menú Principal ---")
        print("1. Generar 50 registros aleatorios y validar")
        print("2. Ingresar un registro manualmente")
        print("3. Guardar registros en TXT, CSV y JSON")
        print("4. Importar registros desde JSON")
        print("5. Conexión y operaciones con MongoDB")
        print("6. Mostrar registros actuales")
        print("7. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            registros = generar_registros_validos()
            print("✔ Se generaron 50 registros válidos correctamente.")

        elif op == "2":
            r = ingresar_manual()
            if validar(r):
                registros.append(r)
                print("✔ Registro agregado correctamente.")
            else:
                print("✖ Registro inválido y NO se agregó.")

        elif op == "3":
            guardar_todo(registros)

        elif op == "4":
            registros = importar_json()
            print("✔ Datos importados desde JSON.")

        elif op == "5":
            menu_mongo(registros)

        elif op == "6":
            for r in registros:
                print(r)

        elif op == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
