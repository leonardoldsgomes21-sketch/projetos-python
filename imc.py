#etapa1 - calculo imc
def cal_imc(imc):
    imc = peso/ (altura*altura)
    return imc 

#etapa2 - classificação do imc
def classificação_imc(resultado):
    if reultado >=25:
        return "peso normal"
#etapa3 - mensagem de retorno
def mensagem(status):
    if status == "acima do peso":
        return "☣️procure um medico☣️"
    else:
        return "peso ok"
#etapa4 - integração do código
valor_peso = float(input("digite o seu peso"))
valor_altura = float(input("digite sua altura"))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificação_imc(valor_imc)
saida = mensagem(resultado_imc)

print("="*50)
print("RESULTADO DO SEU IMC")
print(f"n/ seu IMC é:{valor_imc}")
print(f"n/ {sida}")
print("=" * 50)

