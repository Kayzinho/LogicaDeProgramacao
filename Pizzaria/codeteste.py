from os import system
from time import sleep

system('cls')

# ----- Funções de Tabela ----- #

def tabelaTamanhos():
    print('Tamanhos:\n',
            '1 = G..........R$39,99\n',
            '2 = M..........R$29,99\n',
            '3 = P..........R$19,99\n')
    
def tabelaSabores():
    print('Sabores normais:\n',
        '1 = Frango......................+R$0,00\n',
        '2 = Calabresa...................+R$0,00\n',
        '3 = Charque.....................+R$0,00')
    print('Sabores da casa:\n',
        '4 = Frango & Queijo.............+R$4,99\n',
        '5 = Calabresa & Queijo..........+R$4,99\n',
        '6 = Charque & Queijo............+R$4,99\n')
    
def tabelaBordas():
    print('Bordas:\n',
        '1 = Sem borda...................+R$0,00\n',
        '2 = Catupiry....................+R$1,99\n',
        '3 = Cheddar.....................+R$1,99\n')
    
# ----- Funções de Cálculo ----- #

def tamanhos(valor, tamanho):
    match tamanho:
        case 1: valor = 39.99; tamanho = 'G'
        case 2: valor = 29.99; tamanho = 'M'
        case 3: valor = 19.99; tamanho = 'P'

    return(valor, tamanho)

def sabores(valor, sabor):
    match sabor:
        case 1: sabor = 'frango'; valor = 0
        case 2: sabor = 'calabresa'; valor = 0
        case 3: sabor = 'charque'; valor = 0
        case 4: sabor = 'frango & queijo'; valor = 4.99
        case 5: sabor = 'calabresa & queijo'; valor = 4.99
        case 6: sabor = 'charque & queijo'; valor = 4.99

    return(valor, sabor)

def bordas(valor, borda):
    match borda:
        case 1: borda = 'borda simples'; valor = 0
        case 2: borda = 'borda de catupiry'; valor = 1.99
        case 3: borda = 'borda de cheddar'; valor = 1.99

    return(valor, borda)

# ----- Funções Input ----- #

def tamanhoF():
    while True:
        try:
            inputTamanho = int(input('Escolha seu tamanho usando 1, 2 ou 3: '))
            if inputTamanho not in (1,2,3):
                print('Por favor, use apenas os números indicados')
                sleep(1)
            else:
                return inputTamanho
        except ValueError:
            print('Por favor, use apenas números')
            sleep(1)

def saborF():
    while True:
        try:
            inputSabor = int(input('Escolha seu sabor usando 1, 2, 3, 4, 5 ou 6: '))
            if inputSabor not in (1,2,3,4,5,6):
                print('Por favor, use apenas os números indicados')
                sleep(1)
            else:
                return inputSabor
        except ValueError:
            print('Por favor, use apenas números')
            sleep(1)

def bordaF():
    while True:
        try:
            inputBorda = int(input('Escolha a borda usando 1, 2 ou 3: '))
            if inputBorda not in (1,2,3):
                print('Por favor, use apenas os números indicados')
                sleep(1)
            else:
                return inputBorda
        except ValueError:
            print('Por favor, use apenas números')
            sleep(1)

# ----- Código Executável ----- #

print('Bem vindo a pizzaria Sabor & Queijo!')
sleep(2)
print('Por favor faça seu pedido', '\n')
sleep(2)

tabelaTamanhos()
inputTamanho = tamanhoF()
total1, tamanhoEscolhido = tamanhos(valor = 0, tamanho = inputTamanho)

print(f'Você escolheu o tamanho {tamanhoEscolhido}')
sleep(2)
print('Agora, escolha um sabor!\n')
sleep(2)

tabelaSabores()
inputSabor = saborF()
total2, saborEscolhido = sabores(valor = 0, sabor = inputSabor)

print(f'Você escolheu o sabor {saborEscolhido}')
sleep(2)
print('Estamos quase lá! Por último, escolha a borda da sua pizza\n')
sleep(2)

tabelaBordas()
inputBorda = bordaF()
total3, bordaEscolhida = bordas(valor = 0, borda = inputBorda)

print(f'Você escolheu {bordaEscolhida}')
sleep(2)
print(f'Sua pizza será de tamanho {tamanhoEscolhido}, de sabor {saborEscolhido} e com {bordaEscolhida}')
sleep(2)
total = total1 + total2 + total3
print(f'Total: R${total:.2f}')
sleep(2)

# ----- Alteração do pedido ----- #
segundoloop = False
quartasaida = False
print('Deseja realizar alguma alteração no pedido?\n''1 = Sim\n''2 = Não\n')
while True:
    sair = False
    if segundoloop == True:
        print('Deseja alterar algo mais?\n''1 = Sim\n''2 = Não\n')
        segundoloop = False
        total = total1 + total2 + total3
        sleep(2)
    elif quartasaida == True:
        print('Ainda deseja alterar alguma coisa?\n''1 = Sim\n''2 = Não\n')
        quartasaida = False
        total = total1 + total2 + total3
        sleep(2)
    else:
        try:
            if sair == True:
                break
            alterar = int(input('Escolha usando 1 ou 2: '))
            if alterar not in (1,2):
                print('Por favor, use apenas os números indicados')
                sleep(1)
            elif alterar == 1:
                print('O que deseja alterar?\n''1 = Tamanho\n''2 = Sabor\n''3 = Borda\n''4 = Cancelar\n')
                while True:
                    try:
                        alterar2 = int(input('Escolha usando 1, 2, 3 ou 4: '))
                        if alterar2 not in (1,2,3,4):
                            print('Por favor, use os números indicados')
                            sleep(1)
                        else:
                            match alterar2:
                                case 1:
                                    tabelaTamanhos()
                                    inputTamanho = tamanhoF()
                                    total1, tamanhoEscolhido = tamanhos(valor = 0, tamanho = inputTamanho)
                                    print(f'Você alterou o tamanho para {tamanhoEscolhido}')
                                    sleep(2)
                                    print(f'Sua pizza será de tamanho {tamanhoEscolhido}, de sabor {saborEscolhido} e com {bordaEscolhida}')
                                    segundoloop = True
                                    sleep(2)
                                    break
                                case 2:
                                    tabelaSabores()
                                    inputSabor = saborF()
                                    total2, saborEscolhido = sabores(valor = 0, sabor = inputSabor)
                                    print(f'Você alterou o sabor para {saborEscolhido}')
                                    sleep(2)
                                    print(f'Sua pizza será de tamanho {tamanhoEscolhido}, de sabor {saborEscolhido} e com {bordaEscolhida}')
                                    segundoloop = True
                                    sleep(2)
                                    break
                                case 3:
                                    tabelaBordas()
                                    inputBorda = bordaF()
                                    total3, bordaEscolhida = bordas(valor = 0, borda = inputBorda)
                                    print(f'Você alterou a borda para {bordaEscolhida}')
                                    sleep(2)
                                    print(f'Sua pizza será de tamanho {tamanhoEscolhido}, de sabor {saborEscolhido} e com {bordaEscolhida}')
                                    segundoloop = True
                                    sleep(2)
                                    break
                                case 4:
                                    print('Tudo certo então! Nada foi alterado')
                                    quartasaida = True
                                    sair = True
                                    sleep(2)
                                    break
                    except ValueError:
                        print('Por favor, use apenas números')
                        sleep(1)
            else:
                print('Tudo certo então!')
                sleep(2)
                break
        except ValueError:
            print('Por favor, use apenas números')
            sleep(1)


# ----- Gorjetinha paizão ----- #

print('Gostaria de nos ajudar com uma gorjeta de 10%?\n''1 = Sim\n''2 = Não\n')
while True:
    try:
        gorjeta = int(input('Escolha usando 1 ou 2: '))
        if gorjeta not in (1,2):
            print('Por favor, use apenas os números indicados')
        elif gorjeta == 1:
            total = total+total/10
            print(f'Obrigado! Seu total é de R${total:.2f}')
            break
        else:
            print(f'Obrigado pela compra! Seu total é de R${total:.2f}')
            break
    except ValueError:
        print('Por favor, use apenas números')