import io


def le_entrada(caminho):
    """
        Função que lê o arquivo de entrada e retorna o estado inicial do automato
    """

    dados = {
        'tabela': {},
        'entrada': '',
        'estado_inicial': '',
        'estados_finais': {},
    }

    # Abre e separa o arquivo de entrada
    with io.open(caminho, 'r') as arquivo:
        bruto = arquivo.read().split('&')

    # Avalia os dados do arquivo de entrada
    for indice, dado in enumerate(dados):
        dados[dado] = eval(bruto[indice])

    return dados


def automato(tabela, entrada, estado_inicial, estados_finais):
    """
        Função que retorna o estado final do automato
    """

    lexema = ""
    pilha = []
    estado = estado_inicial
    letra = entrada[0]

    # Verifica se a palavra inteira é válida
    while letra != '\0' and estado is not None:
        entrada = entrada[1:]

        lexema += letra
        if estado in estados_finais:
            pilha.clear()

        pilha.append(estado)
        estado = tabela[(estado, letra)]

        if len(entrada) < 1:
            letra = '\0'
            break

        letra = entrada[0]

    # Verifica se uma parte da palavra é válida
    while estado not in estados_finais and len(pilha) > 0:
        estado = pilha.pop()
        lexema = lexema[:-1]
        entrada = letra + entrada

    if estado in estados_finais:
        return estado, lexema

    return None

def roda_automato(caminho):
    dados = le_entrada(caminho)

    estado_inicial = dados['estado_inicial']
    estados_finais = dados['estados_finais']
    tabela = dados['tabela']
    entrada = dados['entrada']

    resultado = automato(tabela, entrada, estado_inicial, estados_finais)

    # Imprime o resultado
    if resultado is None:
        print('Palavra '+  entrada + ':' ,'não reconhecida')
    elif resultado[1] == entrada:
        print('Palavra '+  entrada + ':',' reconhecida no estado', resultado[0])
    else:
        print('Palavra ' + entrada + ':', 'lexema', resultado[1], 'reconhecido no estado', resultado[0])

roda_automato('entrada1.txt')
roda_automato('entrada2.txt')