time1 = int(input("Número de Gools Time 1: "))
time2 = int(input("Número de Gools Time 2: "))

if (time1 > time2):
    print("Time 1 marcou mais Gools:", time1)
    print("Time 1 ganhou a partida!")
elif (time2 > time1):
    print("Time 2 marcou mais Gools:", time2)
    print("Time 2 Venceu a partida!")
elif (time1 == time2):
    print("A partidade gerou empate: ", time1, time2)
gools = time1 + time2

print("Total de Golls da partida: ", gools)