import io

entrada = 'aabaaa'


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

    estados = set()

    # Abre e separa o arquivo de entrada
    with io.open(caminho, 'r') as arquivo:
        bruto = arquivo.read().split('&')

    # Avalia os dados do arquivo de entrada
    for indice, dado in enumerate(dados):
        dados[dado] = eval(bruto[indice])

    # Obtém os estados do automato a partir da tabela de transição
    for transicao in dados['tabela'].items():
        estados.add(transicao[0][0])
        estados.add(transicao[1])

    # Salva os estados do automato
    dados['estados'] = estados

    return dados


def automato(tabela, entrada, estados, estado_inicial, estados_finais):
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


dados = le_entrada('entrada.txt')

estados = dados['estados']
estado_inicial = dados['estado_inicial']
estados_finais = dados['estados_finais']
tabela = dados['tabela']
entrada = dados['entrada']

resultado = automato(tabela, entrada, entrada, estado_inicial, estados_finais)

# Imprime o resultado
if resultado is None:
    print('Palavra não reconhecida')
else:
    print('Palavra', resultado[1], 'reconhecida no estado', resultado[0])