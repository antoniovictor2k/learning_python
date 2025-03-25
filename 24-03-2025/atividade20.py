nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovador")
elif media <= 6 and media >= 4:
    print("Recuperação")
else:
    print("Reprovado!")