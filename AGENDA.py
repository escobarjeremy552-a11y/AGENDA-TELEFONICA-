"""
Programa: Agenda de Contactos
Descripción: Permite guardar contactos (nombre y número telefónico)
usando un DICCIONARIO como estructura de datos.
Operaciones: agregar, mostrar, buscar y eliminar contactos.
"""

# Creamos la colección de datos: un diccionario vacío
# La clave será el nombre, el valor será el número telefónico
agenda = {}


def agregar_contacto():
    """Agrega un nuevo contacto a la agenda."""
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número telefónico: ")
    agenda[nombre] = telefono
    print(f"✅ Contacto '{nombre}' agregado con éxito.\n")


def mostrar_contactos():
    """Muestra todos los contactos guardados."""
    if not agenda:
        print("⚠️ No hay contactos guardados.\n")
        return
    print("\n--- Lista de Contactos ---")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
    print("--------------------------\n")


def buscar_contacto():
    """Busca un contacto por nombre."""
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in agenda:
        print(f"📞 {nombre}: {agenda[nombre]}\n")
    else:
        print("⚠️ Contacto no encontrado.\n")


def eliminar_contacto():
    """Elimina un contacto de la agenda."""
    nombre = input("Ingrese el nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"🗑️ Contacto '{nombre}' eliminado.\n")
    else:
        print("⚠️ Contacto no encontrado.\n")


def menu():
    """Muestra el menú principal y controla el flujo del programa."""
    while True:
        print("===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()