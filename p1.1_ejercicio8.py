import sys

def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        if len(sys.argv) > 2:
            edad = sys.argv[2]
            if len(sys.argv) > 3:
                ciudad = sys.argv[3]
                print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad} 👋")
            else:
                print(f"Hola {nombre}, tienes {edad} años 👋")
        else:
            print(f"Hola, {nombre} 👋")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()