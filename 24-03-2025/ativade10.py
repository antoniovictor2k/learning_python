idade = int(input("Digite idade: "))

if idade > 4:
    if   idade >= 5 and idade <=7:
        print("Infantil A: 5 a 7 anos")
    elif idade >= 8 and idade <= 10:
        print("Infantil B: 8 a 10 anos")
    elif idade >= 11 and idade <= 13:
        print("Juvenil A: 11 a 13 anos")
    elif idade >= 14 and idade <= 17:
        print("Juvenil B: 14 a 17 anos")
    else:
        print("Adulto: Maior que 18 anos")
else:
    print("Idade precisar ser maior que 4 anos!")

