mesAnterior = float(input("Consumo mês anterior: "))
mesVigente = float(input("Consumo mês vigente: "))

consumo = mesAnterior + mesVigente

if(consumo <= 20):
    valor1 = consumo * 2.0
    print("Consumo:", consumo)
    print("Preço a pagar:", valor1)

elif(consumo > 20 or consumo  <= 35):
    valor2 = consumo * 3.50
    print("Consumo:",consumo)
    print("Preço a ser pago:", valor2)

elif(consumo > 35 or consumo <= 50):
    valor3 = consumo * 5.50
    print("Consumo:",consumo)
    print("Preço a ser pago:", valor3)

elif(consumo > 50):
    valor4 = consumo * 7.0
    print("Consumo:",consumo)
    print("Preço a ser pago:", valor4)






