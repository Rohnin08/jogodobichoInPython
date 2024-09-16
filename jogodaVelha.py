"""Jogo da Velha

Este é um exemplo de projeto para a 2ª Etapa da disciplina PEOO.
Nesta primeira versão, o jogo está totalmente funcional.
Perceba as seguintes boas práticas de programação:
- As funções e variáveis têm nomes adequados.
- O código está devidamente comentado.
- Foram evitadas variáveis globais.
- Foi evitado ao máximo misturar entrada e saída (`input` e `print`) com
  retorno em uma mesma função.
- As funções que implementam a lógica do jogo estão separadas das funções
  que fazem entrada e saída.

Tome este script como inspiração para criar a primeira versão do seu projeto.
"""


# FUNÇÕES DE ENTRADA/SAÍDA


def jogar():
    '''Executa uma partida completa do Jogo da Velha.'''
    # Inicialização das variáveis
    # O jogador X começa jogando
    jogador = 'X'
    # O vencedor pode ser 'X', 'O', '=' (empate) ou '' (indefinido, ainda está jogando)
    vencedor = ''
    '''O tabuleiro é uma lista de strings.
    Casas vazias contêm o seu índice, começando em 1 e terminando em 9.
    Ex.: a lista ['X','','O','','O','','O','X','X'] corresponde ao jogo abaixo:
    O|X|X
    -+-+-
    4|O|6
    -+-+-
    X|2|O'''
    tabuleiro = [''] * 9
    # Aqui começa o jogo
    while vencedor == '':
        exibir(tabuleiro)
        jogada = pedir_jogada(jogador, tabuleiro)
        tabuleiro[jogada] = jogador  # Marca a jogada no tabuleiro
        vencedor = verificar_vencedor(tabuleiro)
        jogador = trocar_jogador(jogador)
    exibir(tabuleiro)
    if vencedor == '=':
        print('Deu velha!')
    else:
        print(f'O {vencedor} venceu!')


def exibir(tabuleiro):
    '''Exibe o tabuleiro no formato do teclado numérico.'''
    # Os números de cima são mais altos, por isso o i vai diminuindo
    for i in range(2,-1,-1):
        for j in range(3):
            # Exibe a posição ou a marca do jogador
            posicao = 3 * i + j
            marca = tabuleiro[posicao]
            if marca == '':
                marca = str(posicao + 1)
            fim = '|'  # Imprime a barra vertical
            if j >= 2:
                fim = '\n'  # Quebra a linha no final
            print(marca, end=fim)
        if i > 0:
            print('-+-+-')


def pedir_jogada(jogador, tabuleiro):
    '''Pede uma jogada ao jogador, repetindo o pedido até que a jogada seja válida.
    Parâmetros:
      - jogador: o jogador atual.
      - tabuleiro: o tabuleiro que do jogo.
    Retorno:
      Retorna uma posição válida para jogar.
    '''
    jogada = -1
    valida = False
    while not valida:
        # Pede a jogada
        jogada = int(input(f'Onde você quer jogar ({jogador})? ')) - 1
        # Verifica se a jogada é válida
        if jogada < 0 or jogada > 8:
            # Jogada inválida, fora do tabuleiro
            print(f'Índice {jogada} fora do tabuleiro [1-9].')
        elif tabuleiro[jogada] in ['X', 'O']:
            # Jogada inválida, índice ocupado
            print('Esta casa já está ocupada.')
        else:
            # Jogada válida, encerra o laço
            valida = True
    return jogada


# FUNÇÕES DE LÓGICA DO JOGO

def verificar_vencedor(tabuleiro):
    '''Verifica se houve um vencedor no jogo.
    Retorna:
    - 'X', se ele for o vencedor (análogo para 'O').
    - '=', se o jogo estiver empatado.
    - '' (vazio), se ainda houver posições a jogar.
    '''
    # Booleano para guardar se o jogo foi empate.
    # Assume que está empatado até que se verifique que não está.
    empate = True
    # Lista com todas as verificações necessárias para detectar um vencedor.
    verificacoes = [
        [0,1,2], [3,4,5], [6,7,8],  # linhas
        [0,3,6], [1,4,7], [2,5,8],  # colunas
        [0,4,8], [2,4,6]            # diagonais
    ]
    # Executar todas as verificações
    for v in verificacoes:
        temp = verificar(*v, tabuleiro)
        if temp in ['X', 'O']:
            # Um jogador venceu, retorna o vencedor
            return temp
        empate = empate and temp == '='
    if empate:
        return '='
    return ''


def verificar(p1, p2, p3, tabuleiro):
    '''Verifica se um sequência (p1, p2, p3) no tabuleiro contém um vencedor.

    Parâmetros:
    - p1, p2 e p3: Posições no tabuleiro para verificar.
    - tabuleiro: O tabuleiro.
    Retorno:
    - 'X' (ou 'O') caso este seja o vencedor.
    - '=' caso a sequência esteja toda preenchida e não haja vencedor.
    - '' (vazio) caso ainda haja elementos a preencher na sequência.'''
    marca1 = tabuleiro[p1]
    marca2 = tabuleiro[p2]
    marca3 = tabuleiro[p3]
    if marca1 == marca2 == marca3:
        return marca1
    if marca1 == '' or marca2 == '' or marca3 == '':
        return ''
    return '='


def trocar_jogador(atual):
    '''Dado o jogador `atual`, retorna o próximo jogador.
    Ex.: se `atual == 'X'`, retorna `'O'`.'''
    if atual == 'O':
        return 'X'
    return 'O'


# PROGRAMA PRINCIPAL

# Essa condição só é verdadeira quando esse script é executado diretamente.
# Isso faz com que a função jogar() não execute se, por exemplo, esse script
# for importado como módulo por outro script. Nesse caso, a função jogar() só
# será executada se o script que o importou a chame.
if __name__ == '__main__':
    jogar()