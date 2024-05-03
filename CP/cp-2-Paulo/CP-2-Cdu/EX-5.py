def inverter_string(s):
    string_invertida = ''
    i = len(s) - 1
    while i >= 0:
        string_invertida += s[i]
        i -= 1
    return string_invertida

# Exemplo de uso da função
if __name__ == "__main__":
    string_original = input("Digite uma string: ")
    string_resultante = inverter_string(string_original)
    print(f"String invertida: {string_resultante}")

