produtos = int(input("Digite a quantidade de produtos que você deseja comparar:  "))
soma1 = 0
soma2 = 0

while (produtos > 0):
        
    preco = float(input("Digite o preço do produto.....: "))
    reajuste = float(input("Digite o peço com reajuste....: "))
    
    maior_aumento_percentual = 0
    maior_aumento_reais = 0
    
    if(preco < 0):
        print("Preço tem de ser positivo!")
    elif(reajuste < 0):
        print("Reajuste tem de ser positivo!")
    else:
        soma1 += preco
        soma2 += reajuste
        produtos -= 1
        
        aumentoReal = reajuste - preco
        aumentoPercentual = (aumentoReal / preco) * 100
        
        if aumentoReal > maior_aumento_reais:
            maior_aumento_reais = aumentoReal
            
        if aumentoPercentual > maior_aumento_percentual:
            maior_aumento_percentual = aumentoPercentual

print("Aumento:")
print(f"O aumento real foi de..............: R$ {aumentoReal}") 
print(f"O aumento percentual foi de........: {aumentoPercentual} %")
print("\nMaior aumento:")
print(f"O maior aumento real foi de........: R$ {maior_aumento_reais}") 
print(f"O maior aumento percentual foi de..: {maior_aumento_percentual} %")