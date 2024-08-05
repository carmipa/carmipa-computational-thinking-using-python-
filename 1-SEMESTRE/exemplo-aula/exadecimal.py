num = int(input("informe o número: "))

resp = ""

while num != 0:
    resto = num % 16
    num = num // 16
    if resto == 10:
        resp = "A" + resp
    if resto == 11:
        resp = "B" + resp
    if resto == 12:
        resp = "C" + resp
    if resto == 13:
        resp = "D" + resp
    if resto == 14:
        resp = "E" + resp
    if resto == 15:
        resp = "F" + resp
    else:
        resp = str(resto) + resp
print(resp)