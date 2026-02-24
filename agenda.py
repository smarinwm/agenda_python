# Agenda de Contactos
import csv 

def agregar_contacto(contacto, archivo):
    with open(archivo, mode='a', newline='') as file:

        ID = contacto['ID']
        nombre = contacto['nombre']
        apellido = contacto['apellido']
        telefono = contacto['telefono']
        email = contacto['email']
        poblacion = contacto['poblacion'] 

        writer = csv.writer(file)
        writer.writerow([ID,nombre, apellido, telefono, email, poblacion])

def cargar_contactos(archivo):
    contactos = []
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contactos.append(row)
    return contactos

def mostrar_contactos(contactos):
    for contacto in contactos:
        print(f"ID: \n{contacto['ID']}, \nNombre: {contacto['nombre']} \nApellido: {contacto['apellido']}, \nTeléfono: {contacto['telefono']}, \nEmail: {contacto['email']}, \nPoblación: {contacto['poblacion']}")

if __name__ == "__main__":

    archivo_csv = 'listado_personas_bk.csv'
    contactos = cargar_contactos(archivo_csv)
    mostrar_contactos(contactos)

    # Agregar un nuevo contacto
    contacto = {
        'ID': 6,
        'nombre': 'Maria',
        'apellido': 'Pérez',
        'telefono': '123456789',
        'email': 'm.p@example.com',
        'poblacion': 'Madrid'
    }
    agregar_contacto(contacto, archivo_csv)