# instale a biblioteca rich escrevendo no terminal: pip install rich (pra ficar mais bonito !!!)

import math
from rich import print

raio = float(input('Digite o raio de uma esfera qualquer: '))
volume = (4/3)*math.pi*(raio**3)

print(f'A [b blue]esfera[/] tem [b]volume[/] de aproximadamente [b blue]{volume:.2f} cm³[/].')
