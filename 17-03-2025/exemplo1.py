senha_armazenada = 123456


# Estrutura condicional para verificar se a senha digitada é igual a senha armazenada
while True:

    senha_digitada = int(input("Digite a senha: "))

    
    if  senha_armazenada != senha_digitada:
        print("Senha incorreta!")
        
    else:
        print("Senha correta!")
        break