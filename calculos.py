import random
from dados import dados_base


dado_a_usar = dados_base

print(dado_a_usar[2]*4)



def calculo_promedio(dado):
    tiradas = 0
    suma_dados = 0
    promedio_actual = 0
    promedio_total = 1

    while promedio_actual != promedio_total:
        promedio_total = promedio_actual

        for n in range(1000):
            tiradas = tiradas+1
            suma_dados = suma_dados + random.randint(1, dado)
        
        promedio_actual = round(suma_dados/tiradas, 2)
        print(promedio_actual)
        print(promedio_total)

    print("el dado se tiro: ", tiradas ," veces")
    return promedio_actual


print(calculo_promedio(12))