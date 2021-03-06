#!/usr/bin/python2.7
#!-*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Carregando arrays a partir de arquivos
X = np.load('data/X.npy')
Y = np.load('data/Y.npy')
V = np.load('data/V.npy')

# Criando figura
fig = plt.figure()

# Adicionando eixos
fig.add_axes()

# Criando eixo para plotagem
ax = fig.add_subplot(111)

# Formando base para o plot (?)
[Y, X] = np.meshgrid(Y,X)

markers = np.array([(0., 0.), (1.5, 1.9), (3., 2.3), (4., 3.8), (6.5, 8.)], dtype=(float, 2))

# Invertendo o eixo y
plt.gca().invert_yaxis()

# Buscando o maior valor de U para fixar o eixo em z
M = max(abs(V.min()), abs(V.max()))

# Criando plot
plot = ax.contourf(X, Y, V, 20, cmap=plt.cm.seismic, vmin=-M, vmax=M)

# Desenhando a barra de cores
plt.colorbar(plot)

# Plotando as Camadas
for i in range(0, markers.size / 2):
    # TODO: Trocar o 15. por uma variavel passada por parametro
    ax.plot((0., 15.), (markers[i][0], markers[i][1]), '-k')

# Configurando o titulo do grafico e suas legendas
ax.set(title='Velocidades', ylabel='Y', xlabel='X')

# Definindo caminho da plotagem
caminho = 'images/Velocidades.png'

# Salvando a imagem
plt.savefig(caminho)
