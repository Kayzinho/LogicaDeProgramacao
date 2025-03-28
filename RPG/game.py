from sys import stdout
from time import sleep
from os import system
from importlib import reload
import texts
import game_data

system('cls')

# ----- VARIÁVEIS ÚTEIS ----- #

player_data = game_data.game_data['player_data']

# ----- FUNÇÕES ----- #
#                                                                   intervalo original = 0.075
def exibir_mensagem(texto, italico=False, negrito=False, espacamento=False, intervalo=0.075):
    negrito = '\033[1m' if negrito else ''
    italico = '\033[3m' if italico else ''
    espacamento = ' ' if espacamento else ''
    texto = texto[0].upper() + texto[1:]
    intervalo0 = intervalo
    for caractere in texto:
        intervalo = 0.6 if caractere in (',','.','?','\n') else intervalo0
        stdout.write(f'{italico}{negrito}{caractere}{espacamento}\033[0m')
        stdout.flush()
        sleep(intervalo)
    print()

# mensagem, mensagem_erro e mensagem_except são strings, valores_permitidos deve ser uma tupla, ex: (1,2,3)
def pegar_input_int(mensagem, mensagem_erro='', mensagem_except='', valores_permitidos=None):
    player_input = int(input(mensagem))
    while True:
        try:
            return player_input if player_input in valores_permitidos else exibir_mensagem(mensagem_erro)
        except ValueError:
            exibir_mensagem(mensagem_except)

# mensagem, mensagem_erro_valor e mensagem_except são strings, valores_permitidos deve ser uma tupla, ex: (1,2,3)
def pegar_input_str(mensagem, mensagem_erro_valor='', mensagem_erro='', valores_permitidos=None):
    while True:
        player_input = (input(mensagem)).strip().capitalize()
        if valores_permitidos is not None and player_input.lower() not in valores_permitidos:
            exibir_mensagem(mensagem_erro_valor)
        elif player_input.isalpha():
            return player_input
        else:
            exibir_mensagem(mensagem_erro)

def mostrar_texto(texto):
    for i in texto:
        exibir_mensagem(*i)

# ----- JOGO ----- #

mostrar_texto(texts.introducao)

while True:
    player_data['Nome'] = pegar_input_str('Você: Meu nome... Meu nome é ','',
    'Desconhecido 1: Ainda está acordando... Deixa eu perguntar de novo, qual é o seu nome?\n')
    exibir_mensagem(f'Desconhecido 1: Ah, {player_data["Nome"]}, esse é o seu nome?\n')
    exibir_mensagem('Sim ou não?', True, True)
    player_input = pegar_input_str('Você: ',f'Desconhecido 1: Hein? Não entendi, seu nome é {player_data["Nome"]}?\n',
                                    '', ('s','si','sim','n','na','nao','nã','não'))
    if player_input.lower() in ('s','si','sim'):
        exibir_mensagem(f'Desconhecido 2: {player_data["Nome"]}, não é? É um nome peculiar, você não deve ser daqui')
        exibir_mensagem('Desconhecido 1: Vai ficar tudo bem, vamos te levar para um lugar seguro')
        break
    else:
        exibir_mensagem('Desconhecido 1: Está tudo bem, você ainda está acordando, vamos tentar de novo, qual é o seu nome?\n')

reload(texts)

mostrar_texto(texts.a_viagem)

while True:
    exibir_mensagem('Masculino ou Feminino?', True, True)
    player_input = pegar_input_str('Você: Parece ser ', 'Você: (Não sei se isso existe por aqui)\n',
                                    '', ('masculino', 'feminino'))
    genero = player_input
    exibir_mensagem(f'Você: ({genero}? Será que é isso mesmo?)\n')
    exibir_mensagem('Sim ou não?', True, True)
    player_input = pegar_input_str('Você: Acho que ', 'Você: (Não é isso...)\n', '',
                                   ('s','si','sim','n','na','nao','nã','não'))
    if player_input.lower() in ('s','si','sim'):
        pronomes = ('ele', 'dele', 'o', 'seu', 'rapaz') if genero.lower() == 'masculino' else ('ela', 'dela', 'a', 'sua','moça')
        sexo = 'Homem' if genero.lower() == 'masculino' else 'Mulher'
        exibir_mensagem(f'Você: Pode se referir a mim como "{pronomes[0]}"\n')
        player_data['Genero'] = genero.capitalize()
        player_data['Pronomes'] = pronomes
        player_data['Sexo'] = sexo
        break
    else:
        exibir_mensagem('Hannad: Anda logo, tem problema de visão?\n''Foe: Hannad...\n')

reload(texts)

mostrar_texto(texts.chegada)