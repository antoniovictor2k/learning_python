print("teste")

quantidade = 0
posicao = 0
frases = ""
palavras = ""
testes = ""

def frase():
    global frases
    frase = input("Digite uma frase: ")
    frases = frase.lower()
    return frase
    

def palavra():
    global palavras
    palavra = input("Digite uma palavra para procurar na frase: ")
    palavras = palavra.lower()
    return palavra

def verificar_programa_funcionando(frases, palavras, indice, posicao):
    global testes
    titulo_teste = (f"Quantidade de indices: {len(frases)} - Palavra Determinada: {palavras}")
    testes += (f"""          
Indice: {indice}, Posição: {posicao}, Palavra: {palavras}
""")
    return f"""
{titulo_teste}

{testes}
"""

def conta_quantidade_de_palavra():
    global quantidade, posicao, frases, palavras

    f_frase = frase()
    f_palavra = palavra()

    while posicao < len(frases):
        indice = frases.find(palavras, posicao)
        if indice == -1:
            break
        verificar_programa_funcionando(frases, palavras, indice, posicao)
        quantidade += 1
        posicao = indice + 1 

    return(f"A palavra '{f_palavra}' aparece {quantidade} vezes na frase '{f_frase}'.")
   
if __name__ == "__main__":
    print(conta_quantidade_de_palavra())
    # print(verificar_programa_funcionando(frases, palavras, posicao, posicao))
