from os import system
from time import sleep

system('cls')

# ----- TABELAS ----- #

tabela_tamanhos = {1: ('G', 39.99),
                   2: ('M', 29.99),
                   3: ('P', 19.99)}

tabela_sabores = {1: ('Frango', 0),
                  2: ('Calabresa', 0),
                  3: ('Charque', 0),
                  4: ('Frango & Queijo', 4.99),
                  5: ('Calabresa & Queijo', 4.99),
                  6: ('Charque & Queijo', 4.99),}

tabela_bordas = {1: ('Borda simples', 0),
                 2: ('Borda de Catupiry', 1.99),
                 3: ('Borda de Cheddar', 1.99),}

tabela_alteracao = {1: ('Tamanho'),
                    2: ('Sabor'),
                    3: ('Borda'),
                    4: ('Gorjeta'),
                    5: ('Finalizar Pedido')}

tabela_sim_nao = {1: ('Sim'),
                  2: ('Não')}

# ----- FUNÇÕES ----- #

def escolher(tabela, mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
            if escolha in tabela:
                if tabela == tabela_sim_nao or tabela == tabela_alteracao:
                    print(f'Você escolheu a opção: "{tabela[escolha]}"')
                else:
                    print(f'Você escolheu a opção: "{tabela[escolha][0]}"')
                return tabela[escolha]
            else:
                print('Por favor, use apenas os números indicados')
        except ValueError:
            print('Por favor, use apenas números')

def mostrar_tabela_tupla(tabela, titulo):
    print(f'\n{titulo}')
    for chave, (nome, preço) in tabela.items():
        print(f'{chave} = {nome.ljust(30, ".")}+R${preço:.2f}')
    print()

def mostrar_tabela(tabela, titulo):
    print(f'\n{titulo}')
    for chave, nome in tabela.items():
        print(f'{chave} = {nome}')

# ----- CÓDIGO ----- #

print('Bem vindo a pizzaria Sabor & Queijo!'); sleep(2)
print('Por favor, faça seu pedido'); sleep(2)

mostrar_tabela_tupla(tabela_tamanhos, 'Tamanhos:')
tamanho_escolhido = escolher(tabela_tamanhos, 'Escolha de 1 a 3: '); sleep(2)

mostrar_tabela_tupla(tabela_sabores, 'Sabores:')
sabor_escolhido = escolher(tabela_sabores, 'Escolha de 1 a 6: '); sleep(2)

mostrar_tabela_tupla(tabela_bordas, 'Bordas:')
borda_escolhida = escolher(tabela_bordas, 'Escolha de 1 a 3: '); sleep(2)

total = tamanho_escolhido[1] + sabor_escolhido[1] + borda_escolhida[1]
total_com_gorjeta = total + total/10

print(f'Sua pizza será de tamanho {tamanho_escolhido[0]}, sabor {sabor_escolhido[0].lower()}, e com {borda_escolhida[0].lower()}'); sleep(2)
print(f'Seu total é R${total:.2f}'); sleep(2)

# ----- GORJETA ----- #

mostrar_tabela(tabela_sim_nao,'Gostaria de nos ajudar com uma gorjeta de 10%?\n')
gorjeta = escolher(tabela_sim_nao, '\nEscolha entre 1 e 2: ')
if gorjeta == 'Sim':
    print(f'\nObrigado! Seu novo total é {total_com_gorjeta:.2f}'); sleep(2)
else:
    print('\nAgradecemos a sua compra!'); sleep(2)

# ----- ALTERAÇÃO DE PEDIDO ----- #

loops = 0
while True:
    palavra_variavel = 'Deseja ' if loops == 0 else 'Ainda deseja '
    print(f'\n{palavra_variavel}alterar alguma coisa no pedido?')
    mostrar_tabela(tabela_alteracao, 'Opções de Alteração:\n')
    opcao = escolher(tabela_alteracao, '\nEscolha de 1 a 5: ')

    match opcao:
        case 'Tamanho':
            mostrar_tabela_tupla(tabela_tamanhos, 'Tamanhos:')
            tamanho_escolhido = escolher(tabela_tamanhos, 'Escolha de 1 a 3: '); loops =+ 1
        case 'Sabor':
            mostrar_tabela_tupla(tabela_sabores, 'Sabores:')
            sabor_escolhido = escolher(tabela_sabores, 'Escolha de 1 a 6: '); loops =+ 1
        case 'Borda':
            mostrar_tabela_tupla(tabela_bordas, 'Bordas:')
            borda_escolhida = escolher(tabela_bordas, 'Escolha de 1 a 3: '); loops =+ 1
        case 'Gorjeta':
            mostrar_tabela(tabela_sim_nao,'Gostaria de nos ajudar com uma gorjeta de 10%?')
            gorjeta = escolher(tabela_sim_nao, '\nEscolha entre 1 e 2: '); loops =+ 1
            if gorjeta == 'Sim':
                print(f'\nObrigado! Seu novo total é {total_com_gorjeta:.2f}'); sleep(2)
            else:
                print('\nAgradecemos a sua compra!'); sleep(2)
        case 'Finalizar Pedido':
            break
    
    total = tamanho_escolhido[1] + sabor_escolhido[1] + borda_escolhida[1]
    total_com_gorjeta = total + total/10
    print(f'\nSeu pedido atualizado: {tamanho_escolhido[0]}, sabor {sabor_escolhido[0].lower()}, com {borda_escolhida[0].lower()}')
    if gorjeta == 'Sim':
        print(f'Novo total: R${total_com_gorjeta:.2f}'); sleep(2)
    else:
        print(f'Novo total: R${total:.2f}'); sleep(2)

print('\nPedido finalizado! Obrigado pela preferência!\n')