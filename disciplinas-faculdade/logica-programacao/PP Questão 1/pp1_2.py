# instale a biblioteca rich escrevendo no terminal: pip install rich (pra ficar mais bonito !!!)

from rich import print
from rich.panel import Panel

print(Panel('Esse programa irá calcular a quantidade ideal de água que alguém necessita beber  por dia para se manter saudável. Para isso, preencha abaixo com suas informações: '))

peso = float(input('Qual é o seu peso em kg? '))
dose_ideal = peso*0.03
print(f'Você deve beber [b blue]{dose_ideal}ml[/] de água por [b]dia[/].')
