# -*- coding: utf-8 -*-
"""Numpy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eege4_evo2Ic3gJqnxhgGe5Y1eLJl0Kf

1.Exercicios NumPy
"""

#Importe NumPy como np
import numpy as np

#Crie uma matriz de 10 zeros

np.zeros(10)

#Crie uma matriz de 10 ones

np.ones(10)

#Crie uma matriz de 10 cincos

np.full((1,10),5)

#Crie um array de inteiros de 10 até 50
i = 10
array = []
while i < 51:
    array.append(i)
    i = i + 1

print(array)

#Crie um array de numero pares de 10 até 50
i = 10
array = []
while i < 51:
    array.append(i)
    i = i + 2

print(array)

#Crie uma matriz 3x3 com valores cariando de 0 até 8
i = 0
j = 0
count = 0
matriz = [[0 for i in range(3)] for j in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = count
        count += 1

print("array")
for linha in range(3):
    for coluna in range(3):
        print("%4d" % matriz[linha][coluna], end='')
    print()

#Crie uma matriz identidade 3x3
matriz = np.eye(3,3)
print(matriz)

#Use NumPy para gerar numeros aleatórios entre 0 e 1
x=np.random.random(1)
print(x)

#Use NumPy para gerar um array de 25 numeros aleatórios tirados de uma distribuição normal
i = 0
array = []
x = 0
while i < 25:
  x = np.random.normal()
  array.append(x)
  i = i + 1

print(array)

#Crie a seguinte matriz
array = np.arange(1,101) / 100
array

#Crie um array de tamanho 20 igualmente espaçado entre 0 e 1
array = np.linspace(0, 1, 20)
array

"""1.1 Indexação Numpy e Seleção"""

mat = np.arange(1,26).reshape(5,5)
mat

mat = np.arange(1,26).reshape(5,5)
mat[2:5, 1:5]

mat = np.arange(1,26).reshape(5,5)
mat[3][4]

mat = np.arange(1,26).reshape(5,5)
mat[0:3, 1:2]

mat = np.arange(1,26).reshape(5,5)
mat[4:5, 0:5]

mat = np.arange(1,26).reshape(5,5)
mat[3:5, 0:5]

"""1.1.1 Agora faça o seguinte"""

#Obtenha a soma de todos os valores no "mat"
mat = np.arange(1,26).reshape(5,5)
mat.sum()

mat = np.arange(1,26).reshape(5,5)
mat.std()

mat = np.arange(1,26).reshape(5,5)
sum(mat)