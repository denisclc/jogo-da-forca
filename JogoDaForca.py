# Jogo da Forca v0.1

def MontarTabuleiro(palavra):
    """
    Essa função prepara o tabuleiro com um underscore
    para cada letra, exceto se for um espaço ou hífen.

    Retorna o tabuleiro e uma variável indicando se é o jogo válido, OU
    Retorna uma mensagem de erro e uma váriável indicando se o jogo não é válido.

    O jogo é inválido se possuir caracteres especiais ou palavras com acento.
    """
    tabuleiro = ""

    for caractere in palavra:
        if caractere == " ":
            tabuleiro += "  "
        elif caractere == "-":
            tabuleiro += "- "
        elif caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            tabuleiro += "_ "
        else:
            tabuleiro = ("Palavra contém caractere inválido.")
            JogoValido = False
            return [tabuleiro, JogoValido]
    JogoValido = True
    return [list(tabuleiro), JogoValido]

print("Bem-vindo(a) ao Jogo da Forca")
palavra = input("Digite a palavra a ser adivinhada: ")
palavra.strip()
palavra = palavra.upper()
tabuleiro = ""
jogo = MontarTabuleiro(palavra)

# Verifica se o jogo não é inválido antes de continuar
if not jogo[1]:
    print(jogo[0])

# Começa o jogo
else:
    finalizado = False
    while not finalizado:
        # O comando join() pega uma lista e a junta em uma string. Aqui, jogo[0] é o tabuleiro
        # em formato de lista, para que se possa substituir os elementos do tabuleiro.
        print(tabuleiro.join(jogo[0]))
        chute = input("Digite uma letra: ")
        if chute.upper() in palavra:
            i = 0
            for letra in palavra:
                if letra == chute.upper():
                    jogo[0][i] = chute.upper()
                    i = i + 2
                else:
                    i = i + 2
        else:
            print("Letra NÃO está na palavra")
# print(len(palavra))