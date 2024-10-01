# 1. Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos el archivo en modo escritura (esto crea el archivo)
archivo_escritura = open(file_name, "w")

# Escribimos algunas líneas en el archivo
archivo_escritura.write("Línea 1: 7am desayunar\n")
archivo_escritura.write("Línea 2: Comprar Jabon\n")

#También podemos escribir varias líneas a la vez
lineas = ["Línea 3: Tanquear la moto\n", "Línea 4: Ir al gimnasio\n"]
archivo_escritura.writelines(lineas)

#Cerramos el archivo de escritura
archivo_escritura.close()

#Ahora, abrimos el archivo en modo lectura para leer lo que escribimos
archivo_lectura = open(file_name, "r")

#Leemos y mostramos cada línea en la consola
for line in archivo_lectura:
    print(line.strip())  # Usamos strip() para quitar el salto de línea al final

#Cerramos el archivo de lectura
archivo_lectura.close()