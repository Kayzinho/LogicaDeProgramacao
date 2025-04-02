from sys import stdout
from time import sleep
from os import system
from importlib import reload
import texts
import game_data

system('cls')

# ----- VARIÁVEIS ÚTEIS ----- #

player_data = game_data.game_data['player_data']
personagem = game_data.game_data['personagens']

# ----- FUNÇÕES ----- #
#                                                                                                                    intervalo original = 0.065
def exibir_mensagem(personagem_escolhido='', texto='', italico=False, negrito=False, espacamento=False, desconhecido=False, intervalo=0.065):
    negrito = '\033[1m' if negrito else ''
    italico = '\033[3m' if italico else ''
    intervalo0 = intervalo
    if personagem_escolhido:
        identidade = 2 if desconhecido else 0
        cor = f'\033[{personagem_escolhido[1]}m'
        texto = f"{personagem_escolhido[identidade]}{texto[0].upper() + texto[1:]}" if texto else ''
    else:
        cor = ''
        texto = texto[0].upper() + texto[1:]

    for i, caractere in enumerate(texto):
        espacamento = ' ' if espacamento and i < len(texto)-1 else ''
        cor = '' if caractere == ':' else cor
        intervalo = 0.5 if caractere in (',','.','?','\n') else intervalo0
        stdout.write(f'{italico}{negrito}{cor}{caractere}{espacamento}\033[0m')
        stdout.flush()
        sleep(intervalo)

# mensagem, mensagem_erro_valor e mensagem_except são strings, valores_permitidos deve ser uma tupla, ex: (1,2,3)
def pegar_input_str(personagem1='', mensagem='', mensagem_erro_valor='', mensagem_erro='',
                    valores_permitidos=None, personagem2='', desconhecido=False):
    while True:
        exibir_mensagem(personagem1, mensagem)
        player_input = input().strip().capitalize()
        if valores_permitidos is not None and player_input.lower() not in valores_permitidos:
            exibir_mensagem(personagem1, mensagem_erro_valor)
        elif player_input.isalpha():
            return player_input
        else:
            exibir_mensagem(personagem2, mensagem_erro, desconhecido=desconhecido)

def mostrar_texto(texto):
    for i in texto:
        exibir_mensagem(*i)

# ----- JOGO ----- #

mostrar_texto(texts.introducao)

while True:
    player_data['Nome'] = pegar_input_str(personagem["player"],'Meu nome... Meu nome é ','',
    'Ainda está acordando... Deixa eu perguntar de novo, qual é o seu nome?\n\n', personagem2=personagem["foe"], desconhecido=True)

    print()
    exibir_mensagem(personagem["foe"],f'Ah, {player_data["Nome"]}, esse é o seu nome?\n\n', desconhecido=True)
    exibir_mensagem('','Sim ou não?\n\n', True, True)

    player_input = pegar_input_str(personagem["player"],'...',f'Hein? Não entendi, seu nome é {player_data["Nome"]}?\n',
                                    '', ('s','si','sim','n','na','nao','nã','não',), personagem["foe"], True)
    
    if player_input.lower() in ('s','si','sim'):
        print()
        exibir_mensagem(personagem["hannad"],f'{player_data["Nome"]}, não é? É um nome peculiar, você não deve ser daqui\n\n', desconhecido=True)
        exibir_mensagem(personagem["foe"],'Vai ficar tudo bem, vamos te levar para um lugar seguro\n\n', desconhecido=True)
        break
    else:
        exibir_mensagem(personagem["foe"],'Está tudo bem, você ainda está acordando, vamos tentar de novo, qual é o seu nome?\n\n', desconhecido=True)

reload(texts)

mostrar_texto(texts.a_viagem)

while True:
    exibir_mensagem('','Masculino ou Feminino?\n\n', True, True)
    player_input = pegar_input_str(personagem["player"],'Parece ser ', '(Não sei se isso existe por aqui)\n\n',
                                    '', ('masculino', 'feminino'))
    print()
    genero = player_input
    exibir_mensagem(personagem["player"],f'({genero}? Será que é isso mesmo?)\n\n')
    exibir_mensagem('','\nSim ou não?\n\n', True, True)
    player_input = pegar_input_str(personagem["player"],'Acho que ', '(Não é isso...)\n\n', '',
                                   ('s','si','sim','n','na','nao','nã','não'))
    if player_input.lower() in ('s','si','sim'):
        pronomes = ('ele', 'dele', 'o', 'seu', 'rapaz', 'homem') if genero.lower() == 'masculino' else ('ela', 'dela', 'a', 'sua','moça', 'mulher')
        print()
        exibir_mensagem(personagem["player"],f'Pode se referir a mim como "{pronomes[0]}"\n\n')
        player_data['Genero'] = genero.capitalize()
        player_data['Pronomes'] = pronomes
        break
    else:
        exibir_mensagem(personagem["hannad"],'Anda logo, tem problema de visão?\n\n')
        exibir_mensagem(personagem["foe"],'Hannad...\n\n')

reload(texts)

mostrar_texto(texts.chegada)