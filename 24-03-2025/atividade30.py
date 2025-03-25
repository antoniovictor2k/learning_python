
print("""   
      
    Sistema Folha de Pagamento
            
      """)

funcionario = input("""
Escolhar o tipo do funcionário:

1 - Operador
2 - Gerente        

Digite: """)

horas_trabalhada = float(input("Digite a quantidade horas: "))

if funcionario == "1":
    valor_hora = 28
    pagamento = horas_trabalhada * valor_hora
    print(f""" 
    Funcionário - Operador
          
O operador ganhar R${valor_hora} por hora.        
Esse mês ele trabalhou {horas_trabalhada} e vai receber R${pagamento}
""")
elif funcionario == "2":
    valor_hora = 78
    pagamento = horas_trabalhada * valor_hora
    print(f""" 
    Funcionário - Gerente
          
O gerente ganhar R${valor_hora} por hora.      
Esse mês ele trabalhou {horas_trabalhada} e vai receber R${pagamento}
""")
else:
    print("Funcionário não encontrado! Tente novamente.")


