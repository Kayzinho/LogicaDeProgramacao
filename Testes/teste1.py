from sys import stdout
from time import sleep

game_data = {

    'player_data':{ # os dados são adicionados com o passar do jogo
        'Nome': '',
        'Genero': '',
        'Pronomes': ('','','','',''),
        'Sexo': ''
        },

    'personagens':{ # nome e valor de cor para o código ANSI (exemplo: \033[32m)
        'narrador': ('', 93),
        'player': ('Você', 35),
        'foe': ('Foe', 32),
        'hannad': ('Hannad', '38;5;188')
    }
}

personagem = game_data['personagens']

def exibir_mensagem(personagem, texto, italico=False, negrito=False, espacamento=False, intervalo=0.065):
    negrito = '\033[1m' if negrito else ''
    italico = '\033[3m' if italico else ''
    espacamento = ' ' if espacamento else ''
    cor = f'\033[{personagem[1]}m'
    texto = f"{personagem[0]}: {texto[0].upper() + texto[1:]}"
    intervalo0 = intervalo
    for caractere in texto:
        cor = '' if caractere == ':' else cor
        intervalo = 0.6 if caractere in (',','.','?','\n') else intervalo0
        stdout.write(f'{italico}{negrito}{cor}{caractere}{espacamento}\033[0m')
        stdout.flush()
        sleep(intervalo)
    print()

exibir_mensagem(personagem['hannad'], 'O meu deus o que eu fiz\n')