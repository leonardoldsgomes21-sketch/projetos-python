#ferramenta de converão dólar x real
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("conversor dólar x real")
preço = float(input("digite o preço do produto em dólar:"))
resultado = converter(preço)
print(f"o valor em reis é:{resultado:.2f}")