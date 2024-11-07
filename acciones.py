"""
Interfaz de consola y funciones de manejo de la base de conocimientos
"""
from experto_general.engine import Engine

# Motor como variable global
engine = Engine()

# Carga la base de conocimientos
try:
    engine.base.from_json("Enfermedades.json")
    print("'LA BASE DE CONOCIMIENTO ENFERMEDADES....' Se cargado OK.")
except Exception as e:
    print(f"ERROR.... NO se cargo la Base de Conocimientos: {e}")

def insertar(nombre, prop):
    if nombre and prop:
        entry = engine.base.get_or_add_entry(nombre)
        entry.get_or_add_prop(prop)
        print(f"Entrada agregada: {entry}")
    else:
        print("No se admiten valores vacíos")

def get_base_entries():
    return engine.base.entries

def guardar(entrada):
    """
    Guarda la base de conocimientos
    """
    if entrada:
        engine.base.to_json(entrada.strip())
        print("Se guardado con éxito el Archivo")
    else:
        print("Elegir un nombre....")

def cargar(entrada):
    """
    Carga la base de conocimientos
    """
    if entrada:
        try:
            engine.base.from_json(entrada.strip())
            print("Se cargado con éxito el Archivo")
        except KeyError:
            print("ERROR inválido o con Formato incorrecto")
    else:
        print("Elige un nombre.......")
