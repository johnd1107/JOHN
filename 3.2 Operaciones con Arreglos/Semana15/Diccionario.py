# Crear un diccionario con información  personal
informacion_personal = {
    "nombre": "Luis Defaz",
    "edad": 32,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor al diccionario
informacion_personal["profesion"] = "Aprendiz"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0997432758"  # Agregar número de teléfono

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario
# Imprimir el diccionario resultante
print(informacion_personal)