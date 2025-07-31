import random

placar_jogador: int = 0
placar_computador: int = 0
lances = {0: 'Papel', 1: 'Pedra', 2: 'Tesoura'}
resultados = {0: 'Empate', 1: 'Você vencer', 2:'Você perdeu'}

def placar():
    print(f'\nPLACAR:\nVocê:{placar_jogador}\nComputador: {placar_computador}\n')

def jogo():
    print('----------\nBem vindo ao jogo de papel, pedra e tesoura\n----------\n')
    while True:
        placar()
        while True:
            try:
                lance_jogador: int = int(input('Escolha seu lance:\n0 - Papel 1 - Pedra 2 - Tesoura '))
            except:
                print('Comando errado, vamos tentar de novo')
                continue
            else:
                lance_computador_lance = lance_computador()
                confronto(lance_jogador, lance_computador_lance)
                mostrar_jogada(lance_jogador, lance_computador_lance)
                while True:
                    try:
                        recomeço = int(input('Jogar novamente? 0 - SIM / 1 - NÃO'))
                    except:
                        print('Comando errado, vamos tentar de novo')
                        continue
                    else:
                        break
            finally:
                break
        if recomeço == 0:
            continue
        else:
            break

def confronto(lance_jogador: int, lance_computador: int):
    if lance_jogador == 2 and lance_computador == 0:
        placar_computador += 1
        return 2
    if lance_jogador > lance_computador:
        placar_jogador += 1
        return 1
    if lance_jogador == lance_computador:
        return 0
    else:
        placar_computador += 1
        return 2

def mostrar_jogada(lance_jogador, lance_computador):
    print((f'----------\nSua jogada: {lances[lance_jogador]}\Jogada do computador: {lances[lance_computador]}\n\
           {resultados[confronto(lance_jogador, lance_computador)]}\n-----------'))

def lance_computador():
    return random.choice(lances.keys)

jogo()