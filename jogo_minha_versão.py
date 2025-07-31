import random

placar_jogador: int = 0
placar_computador: int = 0
lances = {0: 'Tesoura', 1: 'Pedra', 2: 'Papel'}
resultados = {0: 'Empate', 1: 'Você venceu', 2:'Você perdeu'}
controle = True

def confronto(lance_jogador: int, lance_computador: int):
    global placar_computador, placar_jogador
    if lance_jogador == 2 and lance_computador == 0:
        placar_computador += 1
        return 2
    elif lance_computador == 2 and lance_jogador == 0:
        placar_jogador += 1
        return 1
    elif lance_jogador > lance_computador:
        placar_jogador += 1
        return 1
    elif lance_jogador == lance_computador:
        return 0
    else:
        placar_computador += 1
        return 2

print('----------\nBem vindo ao jogo de papel, pedra e tesoura\n----------\n')
while controle:
    print(f'\nPLACAR:\nVocê:{placar_jogador}\nComputador: {placar_computador}\n')
    while True:
        try:
            lance_jogador: int = int(input('Escolha seu lance:\n0 - Tesoura 1 - Pedra 2 - Papel '))
        except:
            print('Comando errado. Vamos tentar de novo')
            continue
        else:
            if lance_jogador not in lances:
                print('Comando inválido. Escolha 0, 1 ou 2.\n')
                continue
            lance_computador: int = random.choice(list(lances.keys()))    
            placar_atual = confronto(lance_jogador, lance_computador)
            print(f'----------\nSua jogada: {lances[lance_jogador]}')
            print(f'Jogada do computador: {lances[lance_computador]}')
            print(f'{resultados[placar_atual]}\n')
            break
    while True:
        try:
            recomeço = int(input('Jogar novamente? 0 - SIM / 1 - NÃO '))
        except:
            print('Comando errado. Vamos tentar de novo')
            continue
        else:
            if recomeço == 0:
                break
            else:
                controle = False
                break