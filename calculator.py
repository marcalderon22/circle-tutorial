def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

while True:
    print("Opciones:")
    print("Introduce 'add' para sumar dos números")
    print("Introduce 'subtract' para restar dos números")
    print("Introduce 'multiply' para multiplicar dos números")
    print("Introduce 'divide' para dividir dos números")
    print("Introduce 'quit' para salir de la calculadora")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        if user_input == "add":
            print("Resultado:", suma(num1, num2))
        elif user_input == "subtract":
            print("Resultado:", resta(num1, num2))
        elif user_input == "multiply":
            print("Resultado:", multiplicacion(num1, num2))
        elif user_input == "divide":
            print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida")
