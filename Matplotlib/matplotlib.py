# -*- coding: utf-8 -*-
"""Matplotlib

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vi3u_CjSOF4Bz-zgq4gdPKgmA2yOTBBM

Importe matplotlib.pyplot como plt e defina% matplotlib inline se você estiver usando o notebook jupyter. Qual comando você usa se você não estiver  usando o notebook jupyter?
"""

import matplotlib.pyplot as plt

plt.show() #comando para exibir plot fora do Jupyter

"""2.2 Exercício 1
** Acompanhe estes passos: * Crie um objeto de figura chamado fig usando plt.figure () * Use
add_axes para adicionar um eixo à tela de figura em [0,0,1,1]. Chame esse novo eixo de “ax”. *
Plote (x, y) nesses eixos e defina os rótulos e títulos para corresponder ao gráfico abaixo: **
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure() #define a figura

ax = fig.add_axes([0,0,1,1]) #define o eixo da figura e adiciona nela
ax.set_title('title') #define o titulo
ax.set_ylabel('Y') #define o titulo do eixo y
ax.set_xlabel('X') #define o titulo do eixo x

y = np.array([0, 200]) #da um array de 0 a 200
x = np.array([0, 100]) #da um array de 0 a 100


plt.yticks(np.arange(0,200.1, 50)) #define eixo y de 0 a 200 variando em 50
plt.plot(x,y)
plt.show()

"""2.3 Exercício 2
** Crie um objeto de figura e coloque dois eixos sobre ele, ax1 e ax2. Localizado em [0,0,1,1] e [0,2,0,5, .2, .2], respectivamente. *
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure() # cria o elemento de figura
ax1 = fig.add_axes([0,0,1,1]) #adiciona o eixo externo a figura
ax2 = fig.add_axes([0.2,0.5,.2,.2]) #adiciona o eixo interno a figura
ax1.tick_params(direction='in',top=True,right=True)#da a posiçao do eixo externo
ax2.tick_params(direction='in',top=True,right=True)#da a posição do eixo interno

ax2.xaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de x do 2° eixo
ax2.yaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de y do 2° eixo


ax1.set_xlabel('x') #da o titulo do 1° eixo x
ax1.set_ylabel('y') #da o titulo do 1° eixo y

ax2.set_xlabel('x') #da o titulo do 2° eixo x
ax2.set_ylabel('y') #da o titulo do 2° eixo y

plt.show()

"""Agora plote (x, y) em ambos os eixos. E chame seu objeto de figura para mostrá-lo"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure() # cria o elemento de figura
ax1 = fig.add_axes([0,0,1,1]) #adiciona o eixo externo a figura
ax2 = fig.add_axes([0.2,0.5,.2,.2]) #adiciona o eixo interno a figura
ax1.tick_params(direction='in',top=True,right=True)#da a posiçao do eixo externo
ax2.tick_params(direction='in',top=True,right=True)#da a posição do eixo interno

ax2.xaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de x do 2° eixo
ax2.yaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de y do 2° eixo

ax1.set_xlabel('x') #da o titulo do 1° eixo x
ax1.set_ylabel('y') #da o titulo do 1° eixo y

ax2.set_xlabel('x') #da o titulo do 2° eixo x
ax2.set_ylabel('y') #da o titulo do 2° eixo y

x = np.arange(0,100) #define x a ser plotado como array de 0 a 100
y = x*2 #define y a ser plotado como a array x com os valores vezes 2

ax1.plot(x,y, color='red') #plota eixo 1 com cor vermelha
ax2.plot(x,y, color='red') #plota eixo 2 com cor vermelha
plt.show()

"""Crie o gráfico abaixo, adicionando dois eixos a um objeto de figura em
[0,0,1,1] e [0,2,0,5, .4, .4]
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure() # cria o elemento de figura
ax1 = fig.add_axes([0,0,1,1]) #adiciona o eixo externo a figura
ax2 = fig.add_axes([0.2,0.5,.4,.4]) #adiciona o eixo interno a figura
ax1.tick_params(direction='in',top=True,right=True)#da a posiçao do eixo externo
ax2.tick_params(direction='in',top=True,right=True)#da a posição do eixo interno

ax2.xaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de x do 2° eixo
ax2.yaxis.set_ticks(np.arange(0,1.1,0.2)) #da a variação de y do 2° eixo

plt.show()

"""Agora use x, y e z arrays para recriar o gráfico abaixo. Observe os limites
xlimits e y no gráfico inserido:
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100) #define x a ser plotado como array de 0 a 100
y = x*2 #define y a ser plotado como a array x com os valores vezes 2
z = x**2 #define z como x elevado ao quadrado

fig2 = plt.figure() # cria o elemento de figura
ax11 = fig2.add_axes([0,0,1,1]) #adiciona o eixo externo a figura
ax22 = fig2.add_axes([0.2,0.5,.4,.4]) #adiciona o eixo interno a figura

ax11.tick_params(direction='in',top=True,right=True)#da a posiçao do eixo externo
ax22.tick_params(direction='in',top=True,right=True)#da a posição do eixo interno

ax22.set_xlim(20,22) #define o intevalo de x linha interno de 20 a 22
ax22.set_ylim(30,50) #define o intevalo de y linha interno de 30 a 50

ax11.set_xlabel('X') #da o titulo do eixo x1
ax11.set_ylabel('Z') #da o titlo do eixo y1

ax22.set_xlabel('X') #da o titlo do eixo x2
ax22.set_ylabel('y') #da o titlo do eixo y2
ax22.set_title('zoom') #da do plot menor interno

ax11.plot(x,z)#faz o plot externo maior
ax22.plot(x,y)#faz o plot interno menor
plt.show()

"""2.5 Exercício 4
** Use plt.subplots (nrows = 1, ncols = 2) para criar o gráfico abaixo.
"""

plt.subplots (nrows = 1, ncols = 2)

"""Agora trace (x, y) e (x, z) nos eixos. Note a largura de linha e o estilo
objetivos.
"""

fig, axes = plt.subplots (nrows = 1, ncols = 2)

x = np.arange(0,100) #define x a ser plotado como array de 0 a 100
y = x*2 #define y a ser plotado como a array x com os valores vezes 2
z = x**2 #define z como x elevado ao quadrado

axes[0].plot(x,y, color ='blue', lw=3, ls='--') #define as caracteristicas dos 1° eixos
axes[1].plot(x,z, color ='red', lw=4) #define as caracteristicas dos 2° eixos

plt.show()

"""Veja se você pode redimensionar o gráfico adicionando o argumento figsize ()
em plt.subplots () apenas copiando e colando seu código anterior.
"""

fig, axes = plt.subplots (nrows = 1, ncols = 2, figsize=(12,3))

x = np.arange(0,100) #define x a ser plotado como array de 0 a 100
y = x*2 #define y a ser plotado como a array x com os valores vezes 2
z = x**2 #define z como x elevado ao quadrado

axes[0].plot(x,y, color ='blue', lw=3, ls='--') #define as caracteristicas dos 1° eixos
axes[1].plot(x,z, color ='red', lw=4) #define as caracteristicas dos 2° eixos

plt.show()