numero1 = float(input("Número 1: "))
operacao = input("Digite a operação desejada: '+ , - , / , * : ")
numero2 = float(input("Número 2: "))

if (operacao == "+"):
    resultado = numero1 + numero2
    print("Soma:", numero1, "+", numero2, "=", resultado)
if (operacao == "-"):
    print("Subtração:", numero2, "-", numero2, "=", resultado)
if (operacao == "*"):
    print("Multiplicação", numero1, "*", numero2, "=", resultado)
if (operacao == "/" or operacao == 0):
    print("A divisão não pode ser feita por 0!")
elif (operacao == "/"):
    print("Divisão:", numero1, "/", numero2, "=", resultado)
    