# Ejercicio 1: Tipos de datos y entrada de usuario

# Pedir datos al usuario
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.70): "))

# Mostrar mensaje con f-string
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Mostrar tipos de datos
print("\nTipos de datos:")
print(f"Nombre: {type(nombre)}")
print(f"Edad: {type(edad)}")
print(f"Altura: {type(altura)}")