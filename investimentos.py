deposito = 50
total = 0
for mes in range(1,7):
    total = total + deposito
    print(f"Mes :{mes} ,saldo total: R${total}")
print(f"Ao final de {mes} meses, voce tera R${total}")