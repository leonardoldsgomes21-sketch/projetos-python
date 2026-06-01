#aluno1:formato do nome no filme
def formata (nome):
    return nome.upper()
#aluno2:verificação de acesso
def verificador (idade):
    if idade >=18:
        return "Autorizado"
    else:
        return "Não Autorizado"
#aluno3:mensagem de retorno
def gerador_mensagem (status):
    if status == "autorizado":
     return "tenha uma otima sessão😊"
    else:
      return "sinto muito, idade não autorizada😢"
#aluno4:integrador do projeto
nome_fime = input("digite o nome do filme")
idade_fime = (input("digite sua idade"))
filme = formata(nome_fime)
status_final = verificador("idade_filme")
mensagem = gerador_mensagem(status_final)
print(f"\nfilme:{filme}")
print(f"status:{status_final:}")
print(f"aviso:{mensagem}")
