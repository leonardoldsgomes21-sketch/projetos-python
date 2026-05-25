#multiplas funçoes -- exercicios controle de qualidade --
def cabecalho():
    print("\n "+" *30")
    print("sistem de qualidade")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
        return "aprovada"
    else:
        return "reprovada"
cabecalho()
peso_item = float(input("digite o peso do item em gramos:"))
status = verificar_status(peso_item)
print(f"resultado da inspiração:{status}")
print("=" *30)
