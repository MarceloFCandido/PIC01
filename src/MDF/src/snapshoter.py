#!/usr/bin/python2.7
#!-*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt

print "Qual voce deseja plotar:\n 1 - C/ reflexao \n 2 - C/ fronteiras abertas?"
caminhoEscolhido = input()
camh = 'open'
if (caminhoEscolhido == 1):
    camh = 'reflect'
elif (caminhoEscolhido == 2):
    camh = 'open'
else:
    print 'Opcao inexistente'
    exit()

# Carregando arrays a partir de arquivos
X = np.load('../data/outputs/{caminho}/X.npy'.format(caminho=camh))
Y = np.load('../data/outputs/{caminho}/Y.npy'.format(caminho=camh))
U = np.load('../data/outputs/{caminho}/U.npy'.format(caminho=camh))
params = np.load('../data/configs/params.npy')
markers = np.load('../data/configs/markers.npy')

print "Quantos snapshots voce deseja?"
N = input()

# Definindo passo
h = U.shape[2] / N

counter = 0

# Criando figura
fig = plt.figure()

# Adicionando eixos
fig.add_axes()

# Criando eixo para plotagem
ax = fig.add_subplot(111)

# Formando base para o plot (?)
[Y, X] = np.meshgrid(Y, X)


# Colocando limites no plot
plt.xlim(0., params[0])
plt.ylim(0., params[1])

# Invertendo o eixo y
plt.gca().invert_yaxis()

# Cria as imagens de N em N quadros
for i in range(h, U.shape[2], h):

    # Buscando o maior valor de U para fixar o eixo em z
    M = max(abs(U.min()), abs(U.max()))

    # Criando plot
    ax.contourf(X, Y, U[:,:,i], 20, cmap=plt.cm.seismic, vmin=-M, vmax=M)

    # Plotando as Camadas
    for i in range(0, markers.size / 2):
        ax.plot((0., params[0]), (markers[i][0], markers[i][1]), '-k')

    # Configurando o titulo do grafico e suas legendas
    ax.set(title='Onda em 2D', ylabel='Y', xlabel='X')

    # Definindo titulo da plotagem
    titulo = "Teste 0%d - MDF - 1D" % counter

    # Definindo caminho da plotagem
    caminho = '../data/images/{caminho}/Teste0%d.png'.format(caminho=camh) % counter

    # Incrementando o contador
    counter += 1

    # Salvando a imagem
    plt.savefig(caminho)
