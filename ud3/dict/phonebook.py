import time, re

# Teléfono válido: exactamente 9 dígitos
def valid_tel(tel):
    patro = r"^\d{9}$"

    if re.match(patro, tel):
        return True
    else:
        return False
    
def add_contact(contacts):
    name = input("Nombre: ").lower()

    # Repite hasta que el teléfono sea válido
    while True:
        tel = input("Telefono: ")
        if valid_tel(tel):
            break

    # No sobrescribe un contacto existente
    if name in contacts:
        print("Contacto existente")
    else:
        contacts[name] = tel
        print(f"Contacto {name} añadido")

def search_contact(contacts):
    name = input("Nombre: ").lower()
    if name in contacts:
        print(f"Telefono de {name}: {contacts[name]}")
    else:
        print(f"El contacto {name} no existe")

def delete_contact(contacts):
    name = input("Nombre: ").lower()

    if name in contacts:
        confirm = input(f"Seguro que quieres eliminar a {name} y/N: ")
        # Pide confirmación antes de borrar
        if confirm in "yY":
            del contacts[name]
        else:
            print(f"{name} no eliminado")
    else:
        print(f"{name} no esta en tus contactos")

def list_contact(contacts):
    for name, tel in contacts.items():
        print(f"Nombre: {name}, Telefono: {tel}")

def menu():
    print("\n\n=== AGENDA TELEFONICA ===")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Listar contactos")
    print("5. Salir")

def main():
    # Pequeña pausa antes de mostrar el menú
    time.sleep(2)
    # Agenda: nombre -> teléfono
    contacts = {}
    while True:
        menu()
        select = input("\n> ")
    
        # Ejecuta la opción elegida
        match select:
            case "1":
                add_contact(contacts)
            case "2":
                search_contact(contacts)
            case "3":
                delete_contact(contacts)
            case "4":
                list_contact(contacts)
            case "5":
                break
            case _:
                print("Selecciona una opcion valida")

if __name__ == "__main__":
    main()