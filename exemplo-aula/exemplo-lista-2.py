def maiorMenor(conjunto):
    max = conjunto[0]
    min = conjunto[0]

    i = 0
    while i < len(conjunto):
        if conjunto[i] > max:
            max = conjunto[i]
        elif conjunto[i] < min:
            min = conjunto[i]
        i = i + 1
    return(min, max)

lista = [7, 10, -1, 4, 6, 18, 0, 9 ,8]
resp = maiorMenor(lista)
print(resp)
print(lista)