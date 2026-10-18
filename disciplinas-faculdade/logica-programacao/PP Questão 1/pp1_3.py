# instale a biblioteca rich escrevendo no terminal: pip install rich (pra ficar mais bonito !!!)

# achei que ficaria mais fácil fazendo com listas, tem problema?

import math
from rich import print
from rich.console import Console

console = Console()

P = []
Q = []

P_x = int(console.input('Digite um valor inteiro referente ao [b]x[/] do [b purple3]ponto P[/]: '))
P_y = int(console.input('Digite um valor inteiro referente ao [b]y[/] do [b purple3]ponto P[/]: '))
Q_x = int(console.input('Digite um valor inteiro referente ao [b]x[/] do [b hot_pink2]ponto Q[/]: '))
Q_y = int(console.input('Digite um valor inteiro referente ao [b]y[/] do [b hot_pink2]ponto Q[/]: '))

P.append(P_x)
P.append(P_y)
Q.append(Q_x)
Q.append(Q_y)


formula = math.sqrt((Q[0]-P[0])**2+(Q[1]-P[1])**2)

print(f'A distância entre esses dois pontos cartesianos é igual a [blue]{formula:.2f}[/]')