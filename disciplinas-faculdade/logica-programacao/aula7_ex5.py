from rich import print
from rich.console import Console
from rich.panel import Panel


console = Console()

inicial = int(console.input('[b hot_pink3]Valor inicial:[/] '))
final = int(console.input('[b hot_pink3]Valor final:[/] '))

if inicial > final:
    print(Panel(renderable='Ordem Decrescente', width=22))
    for i in range(inicial, final-1, -1):
        print(f'[white]{i}[/]')
    print('[b hot_pink3]Repetição encerrada.[/]')
elif final > inicial:
    print(Panel(renderable='Ordem Crescente', width=20))
    for i in range(inicial, final+1, 1):
        print(f'[white]{i}[/]')
    print('[b hot_pink3]Repetição encerrada.[/]')
else:
    print('[b red]Você deve informar valores diferentes![/]')

