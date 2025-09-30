# Ejercicio 2: Funciones básicas

# Función para saludar
def saludar(nombre):
    return f"\n¡Hola {nombre}! Espero que tengas un excelente día."

# Función para calcular IMC
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    Fórmula: IMC = peso / (altura ^ 2)
    """
    imc = peso / (altura ** 2)
    return imc

# Solicitar datos adicionales (peso) para el IMC
print("EJERCICIO 2: FUNCIONES BÁSICAS\n")

# Usar los datos del ejercicio anterior y pedir el peso
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.70): "))
peso = float(input("Ingresa tu peso en kg (ej: 65.5): "))

# Usar función saludar
saludo = saludar(nombre)
print(saludo)

# Usar función calcular_imc
imc_calculado = calcular_imc(peso, altura)
print(f"\nTu IMC (Índice de Masa Corporal) es: {imc_calculado:.2f}")
