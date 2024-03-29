# -*- coding: utf-8 -*-
"""Exercicios de Seaborn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wDeWl75ecssFh7BYXOepYNMyjQ95JBPl

1.1 Os dados
Nós estaremos trabalhando com um famoso conjunto de dados do Titanic para esses exercícios.
Mais tarde, na seção de Machine Learning do curso, vamos revisar esses dados e usá-lo para prever
as taxas de sobrevivência dos passageiros. Por enquanto, nos concentraremos apenas na visualização
dos dados com seaborn:
"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

titanic.head()

"""Recrie os plots abaixo usando o DataFrame Titanic. Há poucas dicas, uma vez que a maioria
dos plots pode ser feito com apenas uma ou duas linhas de código e uma dica basicamente daria a
solução. Mantenha atenção aos rótulos x e y para dicas.
"""

#pesquisando pelos tipos de plot, esse abaixo é um jointplot formado pelos dados de idade, fare no dataset titanic
sns.jointplot(x='fare', y='age', data=titanic )

#abaixo temos um distplot, que seria de distribuição, com base no Fare
sns.displot(titanic['fare'], bins=30,kde=False, color='red')
#anteriormente o comando seria distplot mas esse sera descontinuado

#o tipo desse que identifica a distribuição de dados pelos quartis é o boxplot
sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')

sns.swarmplot(x='class', y ='age', data=titanic, palette='Set2')

#plot simples de contabilidade de dados em relação ao sexo do dataset titanic
sns.countplot(x='sex', data=titanic, palette=['blue',"green"])

#plot de mapa de calor definido pela variação de cor bwr
sns.heatmap(titanic.corr(),cmap='bwr')
plt.title('titanic.corr()')

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')