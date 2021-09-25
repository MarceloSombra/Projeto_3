forca = """ 
______   
|     |
|
|
|
|_____
"""

cabeca = """
______   
|     |
|     O
|
|
|_____
"""

tronco = """
______   
|     |
|     O
|     |
|
|_____

"""

bracoEsq = """
______   
|     |
|     O
|    /|
|
|_____
"""

bracoDir = """
______   
|     |
|     O
|    /|\\
|
|_____
"""

pernaEsq = """
______   
|     |
|     O
|    /|\\
|    /
|_____

"""

pernaDir= """
______   
|     |
|     O
|    /|\\
|    / \\
|____

"""

chancesDoJogador = [forca, cabeca, tronco, bracoEsq, bracoDir, pernaEsq, pernaDir]
# Cada item desta lista representa, em ordem, a parte do boneco que será mostrada na tela a cada
# erro cometido pelo jogador. 

jogar = "S"
while jogar == "s" or jogar == "sim" or jogar == "SIM" or jogar == "S":
    from random import choice
    # comando para importar a opção aleatoria para que a palavra seja escolhida dentre uma lista 
    # armazenada em um arquivo (palavra.txt)
    arquivo = open("palavra.txt", "r", encoding="utf-8")
    linhas = arquivo.read()
    listaDePalavras = linhas.split("\n")
    # este codigo faz com que cada linha seja lida como uma unica palavra, através da separação por \n
    palavra = choice(listaDePalavras).upper()

    acertos = 0
    erros = 0
    letrasAcertadas = ""
    letrasErradas = ""

    while acertos != len(palavra) and erros != 7:
        # statusPalavra é basicamente aquilo que vai aparecer na tela para o jogador.
        # No caso, no começo do jogo, irá aparecer "_ " * a qtde de letras da palavra.
        statusPalavra = "" 
        for letra in palavra:
            if letra in letrasAcertadas:
                statusPalavra += letra + " "
            else:
                statusPalavra += "_ "
        print(chancesDoJogador[erros]) # imprime na tela a forca de acordo com a quantidade de erros
        print(statusPalavra)

        letra = input("\n\n\nEscolha uma letra: ").upper().strip()
        if letra in letrasAcertadas + letrasErradas: 
            print("Você já tentou essa letra. Tente outra" )
            print("Chutes Errados: " + letrasErradas)
            continue
        # esse bloco serve para que o programa siga para o inicio do looping (while) caso o jogador
        # digite uma letra que já tenha sido digitada anteriormente.   

        if letra in palavra:
            print("Você acertou a letra! :-) ")
            letrasAcertadas += " "+ letra
            acertos += palavra.count(letra)
        # O count foi utilizado para eliminar situações onde uma palavra possui mais de uma mesma letra.
        # Dessa forma, o contador irá somar aquela letra duas vezes, fazendo com que a contagem não seja
        # feita incorretamente.

        else: 
            print("Você errou a letra. :-( ")
            letrasErradas += " " + letra
            erros += 1
        print("Chutes Errados: " + letrasErradas)

    if erros == 7:
        print("\n *******VOCÊ PERDEU!!!!!!*******\n\n A palavra correta era ", palavra)
    elif acertos == (len(palavra)):
        print(chancesDoJogador[erros])
        print(statusPalavra)
        print("\nParabens!! A palavra era ", palavra, " e você acertou!!! ")

    jogar = input("\nDeseja continuar jogando(S/N)? ")