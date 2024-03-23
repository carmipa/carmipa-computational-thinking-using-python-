def calcular_data_pascoa(ano):
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return dia, mes

ano_fornecido = int(input("Digite o ano (maior que 1582): "))
dia_pascoa, mes_pascoa = calcular_data_pascoa(ano_fornecido)
print(f"A Páscoa em {ano_fornecido} é em {dia_pascoa} de abril.")