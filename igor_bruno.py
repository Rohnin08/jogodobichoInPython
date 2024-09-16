import random

def criar_tabela_bicho():#A função criar_tabela_bicho vai criar e definir o dicionario com o nome do bicho e os número a ele associados
    tabelaBicho = {
        1: {'nome': 'Avestruz', 'numeros': list(range(1, 4))},
        2: {'nome': 'Águia', 'numeros': list(range(4, 8))},
        3: {'nome': 'Burro', 'numeros': list(range(8, 12))},
        4: {'nome': 'Borboleta', 'numeros': list(range(12, 16))},
        5: {'nome': 'Cachorro', 'numeros': list(range(16, 20))},
        6: {'nome': 'Cabra', 'numeros': list(range(20, 24))},
        7: {'nome': 'Carneiro', 'numeros': list(range(24, 28))},
        8: {'nome': 'Camelo', 'numeros': list(range(28, 32))},
        9: {'nome': 'Cobra', 'numeros': list(range(32, 36))},
        10: {'nome': 'Coelho', 'numeros': list(range(36, 40))},
        11: {'nome': 'Cavalo', 'numeros': list(range(40, 44))},
        12: {'nome': 'Elefante', 'numeros': list(range(44, 48))},
        13: {'nome': 'Galo', 'numeros': list(range(48, 52))},
        14: {'nome': 'Gato', 'numeros': list(range(52, 56))},
        15: {'nome': 'Jacaré', 'numeros': list(range(56, 60))},
        16: {'nome': 'Leão', 'numeros': list(range(60, 64))},
        17: {'nome': 'Macaco', 'numeros': list(range(64, 68))},
        18: {'nome': 'Porco', 'numeros': list(range(68, 72))},
        19: {'nome': 'Pavão', 'numeros': list(range(72, 76))},
        20: {'nome': 'Peru', 'numeros': list(range(76, 80))},
        21: {'nome': 'Touro', 'numeros': list(range(80, 84))},
        22: {'nome': 'Tigre', 'numeros': list(range(84, 88))},
        23: {'nome': 'Urso', 'numeros': list(range(88, 92))},
        24: {'nome': 'Veado', 'numeros': list(range(92, 96))},
        25: {'nome': 'Vaca', 'numeros': list(range(96, 100))}
    }
    return tabelaBicho #O retorno da função é a variavel dicionario_bicho

def mostrar_opcoes_bicho(): #A função mostra dicionario bicho vai mostrar no terminal os bichos e os valores.
    tabela = criar_tabela_bicho() #Atribui a variavel dicionario a função criar_dicionario_bicho.
    print("Escolha um animal para a aposta:") #O usuario vai poder escolher um animal, e apostar nele.
    for grupo, info in tabela.items():
        print(f"{info['nome']}")

def obter_escolha_usuario():
    escolha = input("Digite o nome do animal: ").strip()
    return escolha

def verificar_aposta(escolha, sorteio):
    tabela = criar_tabela_bicho()
    for grupo, info in tabela.items():
        if info['nome'].lower() == escolha.lower():
            if sorteio in info['numeros']:
                return True
            else:
                return False
    return False

def realizar_sorteio():
    return random.randint(0, 99)

def mostrar_resultado(escolha, sorteio, acertou):
    print(f"\nSorteio: {sorteio}")
    if acertou:
        print(f"Parabéns! Você ganhou com o bicho {escolha}.")
    else:
        print(f"Que pena! O bicho {escolha} não ganhou. Tente novamente!")

def main():
    mostrar_opcoes_bicho()
    escolha = obter_escolha_usuario()
    sorteio = realizar_sorteio()
    acertou = verificar_aposta(escolha, sorteio)
    mostrar_resultado(escolha, sorteio, acertou)

# Executa o programa
if __name__ == "__main__":
    main()
