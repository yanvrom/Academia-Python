x1 = input("Já assistiu todos os filmes?")
x2 = input("Tem camiseta temática?")
x3 = input("Já se fantasiou de algum personagem?")
x4 = input("Tem algum action figure/nave/etc?")
x5 = input("Já foi no Galaxy's Edge, o parque temático da franquia?")

pontuacao = 0

if x1 == 'sim':
    pontuacao += 1
if x2 == 'sim':
    pontuacao += 1
if x3 == 'sim':
    pontuacao += 1
if x4 == 'sim':
    pontuacao += 1
if x5 == 'sim':
    pontuacao += 1

if pontuacao < 2:
    print('Inocente')
if pontuacao == 2:
    print('Padawan')
elif pontuacao <= 4:
    print('Jedi')
elif pontuacao == 5:
    print('One with the Force')