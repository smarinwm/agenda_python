# Agenda de contactos en Python con persistencia CSV

Proyecto educativo desarrollado en **Python** para practicar la gestión de datos mediante archivos **CSV**, funciones, diccionarios, listas y entrada/salida de ficheros.

La aplicación carga una agenda de contactos desde un archivo CSV, muestra los registros por consola y permite añadir nuevos contactos al mismo fichero.

## Funcionalidades

El proyecto permite:

- Leer contactos almacenados en un archivo CSV.
- Convertir cada fila en un diccionario mediante `csv.DictReader`.
- Mostrar los datos de cada contacto por consola.
- Añadir nuevos contactos al archivo.
- Mantener una estructura sencilla de agenda con datos como:
  - ID
  - Nombre
  - Apellido
  - Teléfono
  - Email
  - Población

## Tecnologías utilizadas

- **Python 3**
- Módulo estándar `csv`
- Archivos CSV
- Diccionarios
- Listas
- Funciones
- Entrada y salida de ficheros

## Estructura del proyecto

```text
agenda_python/
├── agenda.py
├── listado_personas_bk.csv
└── README.md
```

### `agenda.py`

Contiene la lógica principal de la aplicación.

Incluye tres funciones principales:

```python
agregar_contacto(contacto, archivo)
cargar_contactos(archivo)
mostrar_contactos(contactos)
```

### `listado_personas_bk.csv`

Archivo utilizado como almacenamiento de la agenda.

Su estructura es:

```text
ID,nombre,apellido,telefono,email,poblacion
```

## Funcionamiento

### Cargar contactos

La función:

```python
cargar_contactos(archivo)
```

abre el CSV en modo lectura y utiliza `csv.DictReader` para convertir cada fila en un diccionario.

Los contactos se almacenan después en una lista.

### Mostrar contactos

La función:

```python
mostrar_contactos(contactos)
```

recorre la lista y muestra por consola los datos de cada persona.

### Añadir contactos

La función:

```python
agregar_contacto(contacto, archivo)
```

abre el archivo en modo append y añade una nueva fila mediante `csv.writer`.

El contacto se recibe como diccionario:

```python
contacto = {
    "ID": 6,
    "nombre": "Maria",
    "apellido": "Pérez",
    "telefono": "123456789",
    "email": "m.p@example.com",
    "poblacion": "Madrid"
}
```

## Ejecución

### Requisitos

Solo necesitas:

- **Python 3**

No hay dependencias externas.

### Clonar el repositorio

```bash
git clone https://github.com/smarinwm/agenda_python.git
cd agenda_python
```

### Ejecutar

```bash
python agenda.py
```

En algunos sistemas:

```bash
python3 agenda.py
```

## Importante

Tal como está implementado actualmente, **cada vez que se ejecuta `agenda.py` se añade automáticamente el contacto de ejemplo definido al final del fichero**.

Eso significa que sucesivas ejecuciones pueden generar registros duplicados.

Para evolucionar el ejercicio sería recomendable pedir los datos al usuario o comprobar previamente si el contacto ya existe antes de guardarlo.

## Objetivo didáctico

Este repositorio permite practicar conceptos básicos e intermedios de Python como:

- Definición de funciones.
- Diccionarios.
- Listas.
- Bucles.
- Lectura de archivos.
- Escritura de archivos.
- Módulo `csv`.
- `csv.DictReader`.
- `csv.writer`.
- Persistencia sencilla de datos.
- Separación de la lógica en funciones.
- Uso de:

```python
if __name__ == "__main__":
```

## Posibles mejoras

Como evolución del proyecto podrían incorporarse:

- Alta interactiva de contactos.
- Búsqueda por nombre, teléfono o email.
- Modificación de contactos.
- Eliminación de contactos.
- Control de IDs duplicados.
- Validación de teléfonos y direcciones de correo.
- Manejo de errores con `try/except`.
- Gestión de archivos inexistentes.
- Codificación UTF-8 explícita.
- Menú interactivo por consola.
- Separación entre lógica, almacenamiento e interfaz.
- Pruebas unitarias.
- Migración posterior a SQLite o una base de datos relacional.

## Consideraciones sobre datos

El repositorio contiene datos de ejemplo con nombres, teléfonos y correos electrónicos ficticios o de demostración.

Para utilizar una agenda similar con datos reales conviene:

- No publicar información personal en un repositorio.
- Evitar versionar archivos con contactos reales.
- Añadir el archivo de datos al `.gitignore` cuando contenga información privada.
- Aplicar las medidas de privacidad y protección de datos correspondientes.

## Autor

**Silverio Marín** — Docente TIC en Valencia, especializado en programación y desarrollo de software.

Más contenidos sobre **programación y desarrollo de software**:

**[silveriomarin.com/programacion](https://silveriomarin.com/programacion/)**

GitHub: **[@smarinwm](https://github.com/smarinwm)**
