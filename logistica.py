#logistica.py

def calcular_frete(peso):
    if peso <=20:
        custo = peso * 10
    else:
        custo = peso * 15

    return custo

#entradas de dados
peso_carga = float(input("digite o peso da carga (kg): "))

#calculo do frete
valor_frete = calcular_frete(peso_carga)

#saída
print(f"valor final do frete: R${valor_frete:.2f}")