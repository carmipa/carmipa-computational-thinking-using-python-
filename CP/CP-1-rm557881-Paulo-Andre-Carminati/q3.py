vl_compra = float(input("Informe o total da compra: "))

if vl_compra > 0:
    print(f"Pix ou money (-10%) R$ {vl_compra * 0.9}")
    print(f"Débito (-5%) R$ {vl_compra * 0.95}")
    print(f"Em 2x sem juros: 2 X {vl_compra / 2}")
    print(f"Em 3x (5%): 3 X {vl_compra * 1.05 / 3}")
    print(f"Em 4x (8%): 4 X {vl_compra * 1.08 / 4}")
else:
    print("Informe um valor positivo")
    