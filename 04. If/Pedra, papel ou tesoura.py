def pedra_papel_tesoura(jogador1,jogador2):
    if (jogador1 !='pedra' and jogador1 !='papel' and jogador1 !='tesoura') or (jogador2 != 'pedra' and jogador2 != 'papel' and jogador2 != 'tesoura'):
        return 'Escolha pedra, papel ou tesoura para jogar'
    elif jogador1 == jogador2:
        return 'empate'
    elif jogador1 == 'pedra':
        if jogador2 == 'papel':
            return 'dois'
        elif jogador2 == 'tesoura':
            return 'um'
    elif jogador1 == 'papel':
        if jogador2 == 'pedra':
            return 'um'
        elif jogador2 == 'tesoura':
            return 'dois'
    elif jogador1 == 'tesoura':
        if jogador2 == 'pedra':
            return 'dois'
        elif jogador2 == 'papel':
            return 'um'
