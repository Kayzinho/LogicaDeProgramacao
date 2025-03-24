from sys import stdout
from time import sleep
from os import system

system('cls')

# ----- DADOS ----- #

personagens = ['Hannad','Foe','Jasper']

# ----- FUNÇÕES ----- #

def mensagem(texto, italico=False, negrito=False, espacamento=False, intervalo=0.075):
    negrito = '\033[1m' if negrito else ''
    italico = '\033[3m' if italico else ''
    espacamento = ' ' if espacamento else ''
    intervalo0 = intervalo
    for caractere in texto:
        intervalo = 0.7 if caractere in (',','.','\n') else intervalo0
        stdout.write(f'{italico}{negrito}{caractere}{espacamento}\033[0m')
        stdout.flush()
        sleep(intervalo)
    print()

# ----- JOGO ----- #



mensagem('Da sua varanda, você observa crianças jogando futebol...\n'
         'Os gritos de euforia ecoam na sua mente\n'
         'Você lembra de como foi a sua infância\n'
         'Lembra dos seus traumas...\n'
         'Das suas falhas...\n'
         'Derrepente, a bola de futebol cai no seu quintal\n'
         'Você recobra o juízo\n', italico=True)

mensagem('Ainda me lembro disso... Quando vou esquecer?\n')

mensagem('As crianças pedem pela bola de futebol\n'
         'Você desce as escadas para buscar\n'
         'Você tropeça e cai\n'
         'Ao tocar o chão, você o atravessa e vê apenas vazio\n', italico=True)

mensagem('O que é isso...???\n', negrito=True, espacamento=True)

mensagem('Olhando pra trás, não existe mais nada, apenas escuridão...\n'
         'Você começa a afundar, e cada vez mais rápido\n'
         'Sua consciência começa a se esvair...\n', italico=True)

mensagem('*Estrondo*\n', negrito=True)

mensagem('Pessoa 1: O que foi isso??\n'
         'Pessoa 2: Não faço a menor idéia...\n'
         'Pessoa 1: Vamos dar uma olhada\n'
         'Pessoa 2: ...\n')

mensagem('......\n', negrito=True)

mensagem('Pessoa 1: O que vamos fazer?\n'
         'Pessoa 2: Deixa aí, não quero problemas\n'
         'Pessoa 1: O que? Não podemos fazer isso!\n'
         'Pessoa 2: Tá, faz o que cê quiser então\n'
         'Pessoa 1: Ei, olha... Tá acordando...\n'
         'Pessoa 2: ...\n'
         'Pessoa 1: Tá tudo bem? Qual é o seu nome?\n')

nome = str(input('Meu nome... Meu nome é ')).strip()

mensagem(f'Pessoa 1: {nome}, não é? Foi você que fez esse barulho todo, o que aconteceu?\n')