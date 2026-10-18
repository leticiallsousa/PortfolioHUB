# instale a biblioteca rich escrevendo no terminal: pip install rich (pra ficar mais bonito !!!)

from rich import print
from rich.panel import Panel
from rich.console import Console

print(Panel('Digite a letra correspondente à operação aritmética que quer realizar: \n\nA. Adição (+)\nB. Subtração (-)\nC. Multiplicação (*)\nD. Divisão (/)')) # painel com infos

operacao = str(input('Qual a operação escolhida? '))

while operacao.lower() not in ['a', 'b', 'c', 'd']: # vê se selecionou apenas as opções válidas
    print('[red]Alternativa inválida, tente novamente.[/]', end=' ')
    operacao = str(input('Qual a operação escolhida? '))

n1 = float(input('Digite o primeiro número da operação: '))
n2 = float(input('Digite o segundo número da operação: '))

console = Console()
console.rule(style='white') # barra divisória

if operacao.lower() == 'a':
    print(f'A [b blue]soma[/] entre [b]{n1} + {n2}[/] resulta em [blue]{(n1+n2):.2f}[/]')

elif operacao.lower() == 'b':
    print(f'A [b blue]subtração[/] entre [b]{n1} - {n2}[/] resulta em [blue]{(n1-n2):.2f}[/]')

elif operacao.lower() == 'c':
    print(f'A [b blue]multiplicação[/] entre [b]{n1} * {n2}[/] resulta em [blue]{(n1*n2):.2f}[/]')

elif operacao.lower() == 'd':
    print(f'A [b blue]divisão[/] entre [b]{n1} / {n2}[/] resulta em [blue]{(n1/n2):.2f}[/]')
