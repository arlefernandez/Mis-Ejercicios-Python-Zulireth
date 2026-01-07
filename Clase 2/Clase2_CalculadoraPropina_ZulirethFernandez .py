# ==============================================================================================================================
# CURSO: Introducción a la Programación con Python
# ALUMNA: Zulireth Fernandez
# CLASE: 02 - Conversión,tipos de datos y Metodos
# EJERCICIO: Calculadora de Propina
# Escribe un programa en Python que calcule la propina que se debe dejar en un restaurante.
# El script debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar.
# Utilizando operadores aritméticos, calcula la cantidad de propina y el total a pagar (incluyendo la
# propina).
# Finalmente, muestra los resultados en la pantalla
# ==============================================================================================================================

import os 
os.system ("cls")  # Limpia la pantalla en Windows; usa "clear" en Linux/Mac

print("---------Bienvenido al sistema de cobro del restaurante Zuli🍣---------")
print()
monto_cuenta= float(input("Ingrese el monto de consumo: $"))
porcentaje_propina= int(input("Ingrese el porcentaje de propina que desea dejar (ejemplo: 10 para 10%):"))
propina= round(monto_cuenta * porcentaje_propina / 100,2)
monto_total= round(monto_cuenta + (monto_cuenta * porcentaje_propina / 100),2)
print()
print("Espera un momento mientras procesamos tu cuenta...")
print()
print(f"El monto total de tu cuenta sin propina es: $ {monto_cuenta}")
print(f"El porcentaje de propina que has elegido es: {porcentaje_propina} %")
print(f"La cantidad de propina a dejar es: $ {propina}")
print(f"El monto total a pagar es: $ {monto_total}")
print()
print("¡Gracias por visitarnos! Esperamos verte pronto 😊")
print()