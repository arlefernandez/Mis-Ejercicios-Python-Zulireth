# ==============================================================================================================================
# CURSO: Introducción a la Programación con Python
# ALUMNA: Zulireth Fernandez
# CLASE: 02 - Conversión,tipos de datos y Metodos
# EJERCICIO: Operaciones básicas
# 1. Crea un programa que solicite al usuario dos números enteros.
# 2. Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo.
# 3. Muestra el resultado de cada operación en un formato claro y amigable.
# Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".
# ==============================================================================================================================

import os 
os.system ("cls")  # Limpia la pantalla en Windows; usa "clear" en Linux/Mac

print("---------Bienvenido a la web de promedios ✌️---------")
print()
ingreso_enero= float(input("Ingrese el monto del ingreso del mes de Enero: $"))
ingreso_febrero= float(input("Ingrese el monto del ingreso del mes de Febrero: $"))
ingreso_marzo= float(input("Ingrese el monto del ingreso del mes de Marzo: $"))
ingreso_abril= float(input("Ingrese el monto del ingreso del mes de Abril: $"))
ingreso_mayo= float(input("Ingrese el monto del ingreso del mes de Mayo: $"))
ingreso_junio= float(input("Ingrese el monto del ingreso del mes de Junio: $"))
print()
print("Su ingreso mensual en enero fue de: $", ingreso_enero)
print("Su ingreso mensual en febrero fue de: $", ingreso_febrero)
print("Su ingreso mensual en marzo fue de: $", ingreso_marzo)
print("Su ingreso mensual en abril fue de: $", ingreso_abril)
print("Su ingreso mensual en mayo fue de: $", ingreso_mayo)
print("Su ingreso mensual en junio fue de: $", ingreso_junio)
print()
print("Calculando el promedio de ingresos del semestre...")
promedio_ingreso= round((ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio) / 6,2)
print()
print("El ingreso promedio en el semestre es de: $", promedio_ingreso)

#Dudas Profe:
#Si quiero que me muestre el promedio con dos decimales, como hago?
#Si quiero que me muestre el promedio con formato de moneda, como hago?
#Si quiero que me muestre el promedio con separador de miles, como hago?