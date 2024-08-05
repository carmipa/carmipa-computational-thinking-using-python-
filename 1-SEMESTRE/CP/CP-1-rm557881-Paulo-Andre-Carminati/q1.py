num_a = float(input("A: "))
num_b = float(input("B: "))
num_c = float(input("C: "))
num_d = float(input("D: "))

if num_a > 0 and num_b > 0 and num_c > 0 and num_d > 0:
    media_geo = (num_a * num_b * num_c * num_d) ** (1 / 4)
    media_geo = (num_a * num_b * num_c * num_d) ** 0.25
    print(f"A média geométrica vale {media_geo}")
else:
    media_arit = (num_a + num_b + num_c + num_d) / 4
    print(f"A média aritmética vale {media_arit}") 
       