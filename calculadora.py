import sys
import emoji

def main():
    if len(sys.argv) != 4:
        print(emoji.emojize(":x: Error: Número incorrecto de argumentos"))
        print("Uso: python calculadora.py <num1> <operador> <num2>")
        print("Ejemplos:")
        print("  python calculadora.py 5 + 3")
        print("  python calculadora.py 10 * 4")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        operador = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        print(emoji.emojize(":x: Error: Los números deben ser valores numéricos"))
        sys.exit(1)

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            print(emoji.emojize(":warning: Error: No se puede dividir por cero"))
            sys.exit(1)
        resultado = num1 / num2
    else:
        print(emoji.emojize(f":warning: Operador '{operador}' no reconocido. Usa +, -, * o /."))
        sys.exit(1)

    print(emoji.emojize(f":white_check_mark: Resultado: {num1} {operador} {num2} = {resultado}"))

if __name__ == "__main__":
    main()