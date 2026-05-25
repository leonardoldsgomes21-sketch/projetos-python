<<<<<<< HEAD
#simulador de investimentos - poupança--
deposito = float(input("digite o valor do aporte"))
taxa = float(input("qual o valor da poupança em % ?"))
meses = float(input("quantos meses no investimentos?"))
conversao = taxa/100
total = 0
for mes in range(1, meses +1):
    total = total + deposito
    total = total +(total * taxa)
print(f"ao final do periodo, você tera: R${total:2f}")
=======
deposito = 50
total = 0
for mes in range(1,7):
    total = total + deposito
    print(f"Mes :{mes} ,saldo total: R${total}")
print(f"Ao final de {mes} meses, voce tera R${total}")
>>>>>>> refs/remotes/origin/main
