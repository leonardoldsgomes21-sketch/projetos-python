numero =int(input("tabuada de qual numero? "))
print(f"--- tabuada do {numero}---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")