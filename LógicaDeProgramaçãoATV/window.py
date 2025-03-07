import FreeSimpleGUI as sg
from code import calcular

layout = [
    [sg.Text('Calcular a quantidade de tinta necessária por m²')],
    [sg.Text('Altura(m):'), sg.InputText(key='Altura')],
    [sg.Text('Largura(m):'), sg.InputText(key='Largura')],
    [sg.Button('Calcular'), sg.Button('Sair')],
    [sg.Text('', key='Area')],
]

janela = sg.Window('Cálculo de tinta por m²', layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break

    if evento == 'Calcular':
        resultado = calcular(valores['Altura'], valores['Largura'])
        
        janela['Area'].update(resultado)

janela.close()
