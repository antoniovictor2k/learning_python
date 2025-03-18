nome = input("Digite seu nome: ")
ano_nascimento = input("Digite o ano de nascimento: ")
ano_nascimento = int(ano_nascimento)

ano_atual = 2025
idade = ano_atual - ano_nascimento


print(f"""
 - Ficha do Aluno - 

Nome: {nome}
Você nasceu em: {ano_nascimento}
Sua idade é: {idade}

""")

