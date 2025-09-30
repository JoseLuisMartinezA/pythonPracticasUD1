entrada = input("Ingresa una lista de números separados por coma: ")
numeros = [int(x) for x in entrada.split(',')]

suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")