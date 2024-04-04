import time
fahr = 50

while (fahr <= 150):

    celcius = 5 / 9 * (fahr -32)
    print(f"{fahr} \t {celcius:.1f}")
    fahr = fahr + 1
    time.sleep(0.3) # imprime de forma mais devagar

print(f"")