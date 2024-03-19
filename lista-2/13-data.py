print(".............................................................")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
print(".............................................................")
print("Regra:", 
      "\n1- dia, mês e ano devem ser números inteiros",
      "\n2- O ano deve ser digitado com 4 digitos",
      "\n3- O mês deve ser digitado o número")
print(".............................................................")

if(dia > 0 and dia <= 31):
    print("O dia está correto!")
else:
    print("Dia digitado de forma errada!")

if(mes > 0 and mes <= 12):
    ("O mês está correto")
else:
    print("mês digitado de forma errada!")

if(ano >0 and ano <= 9999):
    ("O ano está correto")
else:
    print("Ano está digitado de forma incorreta!")
    
    
    
    
    