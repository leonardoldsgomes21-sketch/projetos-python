#print("=== QUIZ: REDES DE COMPUTADORES ===\n")

pontuacao = 0

# Pergunta 1
print("1) O que significa a sigla NFC?")
print("a) Near Field Communication")
print("b) Network Fast Connection")
print("c) New Frequency Control")

resposta1 = input("Digite a opção correta: ").lower()

if resposta1 == "a":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta é a letra A.\n")

# Pergunta 2
print("2) Qual tecnologia é mais usada em fones de ouvido sem fio?")
print("a) Wi-Fi")
print("b) Bluetooth")
print("c) NFC")

resposta2 = input("Digite a opção correta: ").lower()

if resposta2 == "b":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta é a letra B.\n")

# Pergunta 3
print("3) Qual é a principal vantagem do Wi-Fi?")
print("a) Baixo consumo de energia")
print("b) Funciona sem sinal de rádio")
print("c) Alta velocidade na transmissão de dados")

resposta3 = input("Digite a opção correta: ").lower()

if resposta3 == "c":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta é a letra C.\n")

# Resultado final
print("=== RESULTADO FINAL ===")
print(f"Você acertou {pontuacao} de 3 questões.")

if pontuacao == 3:
    print("🏆 Excelente desempenho!")
elif pontuacao == 2:
    print("👍 Muito bom!")
else:
    print("📚 Continue estudando!")