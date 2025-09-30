while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

while True:
    try:
        altura = float(input("Ingresa tu altura en metros: "))
        break
    except ValueError:
        print("Error: Debes ingresar un número válido (ej: 1.70).")

nombre = input("Por favor, ingresa tu nombre: ")

print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")
print(f"Nombre: {type(nombre)}")
print(f"Edad: {type(edad)}")
print(f"Altura: {type(altura)}")