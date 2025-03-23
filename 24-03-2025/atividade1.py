

while True:
    
    usuario = input("Digite o usuário: ")

    if usuario != "sair":
        if usuario != "":
            senha = input("Digite a senha: ")
            if senha != "":
                confirme = input("Confirme sua senha: ")
                if senha == confirme:
                    print("Login com Sucesso!")
                    break
                else:
                    print("Senha diferente da confirmação!")
            else:
                print(f"Senha é obrigatória!")
        else:
            print("Obrigatório digita o usuário!")
    else:
        print("Saindo...")
        break