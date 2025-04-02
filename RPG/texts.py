from game_data import game_data

# ----- VARIÁVEIS ÚTEIS ----- #

player_data = game_data['player_data']
personagem = game_data['personagens']
pronomes = player_data['Pronomes']

ele_ela, dele_dela, oa, seu_sua, substantivo, h_m = pronomes[0], pronomes[1], pronomes[2], pronomes[3], pronomes[4], pronomes[5]

# ----- TEXTOS (CAPÍTULOS) ----- #

introducao = [
    (personagem['narrador'],
    'Da sua varanda, você observa crianças jogando futebol na rua da sua casa...\n\n'
    'Os gritos de euforia ecoam na sua mente\n\n'
    'Você lembra de como foi a sua infância\n\n'
    'Lembra dos seus traumas...\n\n'
    'Das suas falhas...\n\n'
    'De repente, a bola de futebol cai no seu quintal\n\n'
    'Você recobra o juízo\n\n\n', True),

    (personagem['player'], 'Ainda me lembro disso... Só queria esquecer...\n\n\n',),

    (personagem['narrador'],
    'As crianças pedem pela bola de futebol\n\n'
    'Você desce as escadas para buscar\n\n'
    'Refletindo nos pensamentos, você acaba tropeçando\n\n'
    'Ao tocar o chão, você o atravessa e vê o vazio\n\n\n', True),

    (personagem['player'],'O que é isso...???\n\n\n', False, True, True),

    (personagem['narrador'],
    'Olhando pra trás, não existe mais nada, apenas escuridão...\n\n'
    'Você começa a afundar, e cada vez mais rápido\n\n'
    'Sua consciência começa a se esvair...\n\n\n', True),

    (personagem['outro'],'*Estrondo*\n\n\n', False, True),

    (personagem['foe'],'O que foi isso??\n\n', False, False, False, True),
    (personagem['hannad'],'Não faço a menor ideia...\n\n', False, False, False, True),
    (personagem['foe'],'Vamos dar uma olhada\n\n', False, False, False, True),
    (personagem['hannad'],'...\n\n\n', False, False, False, True),

    (personagem['outro'],'......\n\n\n', False, True),

    (personagem['foe'],'O que vamos fazer?\n\n', False, False, False, True),
    (personagem['hannad'],'Deixa aí, não quero problemas\n\n', False, False, False, True),
    (personagem['foe'],'O que? Não podemos fazer isso\n\n', False, False, False, True),
    (personagem['hannad'],'Tá, faz o que você quiser\n\n\n', False, False, False, True),

    (personagem['narrador'],'Você começa a abrir os olhos lentamente\n\n\n', True),

    (personagem['foe'],'Ei, olha... Tá acordando...\n\n', False, False, False, True),
    (personagem['hannad'],'...\n\n', False, False, False, True),
    (personagem['foe'],'Tá tudo bem? Qual é o seu nome?\n\n\n', False, False, False, True)
]

a_viagem = [
    (personagem['hannad'],'Consegue andar?\n\n', False, False, False, True),
    (personagem['player'],'Consigo\n\n',),
    (personagem['foe'],'A propósito, eu sou a Foe, o grandão é o Hannad\n\n', False, False, False, True),
    (personagem['hannad'],'Humph\n\n',),
    (personagem['foe'],'Não liga pra ele não, ele é bem resmungão\n\n',),
    (personagem['hannad'],'Foe...\n\n',),
    (personagem['foe'],'Viu? Haha\n\n\n',),

    (personagem['narrador'],
    'Os viajantes levam você até um reino próximo, porém...\n\n'
    'No meio do caminho, um monstro enorme os ataca\n\n'
    'Similar a um urso, porém muito maior e com características de javali e porco-espinho\n\n'
    'O monstro ruge em sua direção\n\n\n', True),

    (personagem['foe'],'Deixa comigo, Ignis Orbis...\n\n\n',),

    (personagem['narrador'],'De repente, uma enorme bola de fogo aparece sobre Foe\n\n\n', True),

    (personagem['foe'],'Exuro.. HOSTEM!!\n\n\n',),

    (personagem['narrador'],'A bola de fogo avança com tudo abrindo um buraco enorme no corpo do monstro\n\n\n', True),

    (personagem['hannad'],'Ela é incrível, não é?\n\n',),
    (personagem['player'],'... O que.. Foi isso???\n\n',),
    (personagem['hannad'],'Nunca viu magia? De que buraco você saiu?\n\n',),
    (personagem['player'],'Também gostaria de saber...\n\n',),
    (personagem['foe'],'Uff, falando nisso, você não lembra de nada além do seu nome?\n\n',),
    (personagem['player'],'Ahm, eu consigo lembrar mas não consigo ver o que são essas memórias...\n\n',),
    (personagem['hannad'],'Pelo menos sabe como devemos te chamar? Seu corpo não parece másculo, mas seu rosto também não parece feminino, esquisito\n\n',),
    (personagem['foe'],'HANNAD!\n\n',),
    (personagem['hannad'],'O quê? É a verdade\n\n',),
    (personagem['foe'],'Por Horon, seja mais educado\n\n',),
    (personagem['hannad'],f'E então? Diga você, {player_data["Nome"]}\n\n\n',),

    (personagem['narrador'],'Você se vira e olha por de baixo da roupa...\n\n\n', True)
]

chegada = [
    (personagem['foe'],f'Oh, então é {h_m}?\n\n',),
    (personagem['hannad'],'Viu, também estava curiosa né? Haha\n\n',),
    (personagem['foe'],'Ignis Orb-\n\n',),
    (personagem['hannad'],'EU ESTAVA BRINCANDO FOE, ESPERA UM POUCO\n\n',),
    (personagem['foe'],f'Uhrum, desculpe por isso, {player_data["Nome"]}\n\n',),
    (personagem['player'],'Sem problemas, mudando de assunto, para onde estamos indo?\n\n',),
    (personagem['foe'],'Para o reino Wysteria! Ah, não conhece, né?\n\n',),
    (personagem['player'],'Não...\n\n',),
    (personagem['foe'],'Não se preocupe, você vai gostar, lá é seguro e lindo graças as árvores Wystenari\n\n',),
    (personagem['player'],'Árvores?\n\n',),
    (personagem['hannad'],'Aquele monstro que nos atacou é chamado de Abyssar\n\n',),
    (personagem['hannad'],'Um amalgamo de seres vivos que foram corrompidos pelo vazio, uma força obscura desconhecida\n\n',),
    (personagem['hannad'],'Esses monstros corrompidos odeiam árvores Wystenari, e Wysteria é cercada delas, por dentro e por fora\n\n',),
    (personagem['foe'],'Por isso é dos reinos mais seguros, nenhum monstro se aproxima de lá\n\n',),
    (personagem['player'],'Vazio...?? Vazio....\n\n',),
    (personagem['foe'],f'{player_data["Nome"]}?? Você está bem? Lembrou de algo?\n\n',),
    (personagem['player'],'Sim... Eu lembro de ter caído no vazio, só consigo lembrar isso..\n\n',),
    (personagem['hannad'],'Ha, isso é impossível, você teria virado um Abyssar\n\n',),
    (personagem['foe'],'Não é impossível, existem os magos Vhorim que pegam poder emprestado do vazio\n\n',),
    (personagem['hannad'],'Uma pequena fração, e ainda assim é suficiente pra perderem a sanidade aos poucos\n\n',),
    (personagem['foe'],f'Não acho que {pronomes[0]} está mentindo, é só olhar no rosto {pronomes[1]}\n\n',),
    (personagem['hannad'],'De qualquer forma isso não importa agora, vamos indo, o sol já vai se pôr...\n\n',),
    (personagem['player'],'Onde vamos passar a noite?\n\n',),
    (personagem['foe'],'Normalmente eu diria que está cedo, mas estamos perto de Wysteria, amanhã sairemos bem cedo, então vamos dormir\n\n',),
    (personagem['foe'],'Ferrocaelum, Murus, Vincitur!\n\n\n',),

    (personagem['narrador'],'Uma grande muralha de pelo menos 10 metros se forma ao seu redor\n\n\n', True),

    (personagem['foe'],'Domus, Petra, divisa, Aedificium\n\n\n',),

    (personagem['narrador'],'Logo após, uma pequena cabana com 3 divisões surge no centro da muralha\n\n\n', True),

    (personagem['foe'],'Vamos, entrem e durmam bem\n\n\n',),

    (personagem['narrador'],
    'Todos entram em um quarto e descansam\n\n'
    'Em um piscar de olhos, Hannad aparece na sua frente\n\n\n', True),

    (personagem['hannad'],f'Vamos, acorde preguiços{oa}, já é de manhã\n\n\n',),

    (personagem['narrador'],'Você levanta e sai da cabana ao lado de Hannad\n\n\n', True),

    (personagem['foe'],f'Bom dia dorminhoc{oa}! Murus, Dispargo, Domum, Ruina\n\n\n',),

    (personagem['narrador'],'Os muros e a cabana caem e se unem de volta a terra\n\n\n', True),

    (personagem['foe'],'Devolvemos a mãe natureza o que ela nos emprestou, agora, vamos lá\n\n',),
    (personagem['hannad'],'Chegaremos em Wysteria antes do anoitecer\n\n\n',),

    (personagem['outro'],'......\n\n\n', True, True),

    (personagem['narrador'],
    'Você observa o reino imenso de uma colina a distância\n\n'
    'Árvores roxas cercam todo o reino... As folhas caem pouco a pouco como árvores Sakura\n\n'
    'No horizonte, o pôr do sol contrasta com a aparência etérea do reino\n\n\n', True),

    (personagem['player'],'Então essa é a Wysteria? É linda...\n\n',),
    (personagem['grim'],'Não é mesmo?\n\n', False, False, False, True),
    (personagem['foe'],'Grim!\n\n',),
    (personagem['grim'],'Finalmente voltaram haha, eu estava esperando por vocês\n\n',),
    (personagem['foe'],'Estava com saudade de você vovô\n\n',),
    (personagem['grim'],'O vovô também, pequena Foey\n\n',),
    (personagem['hannad'],'Infelizmente não conseguimos o que o senhor queria, mas conseguimos outra coisa\n\n',),
    (personagem['grim'],'Deixaremos isso para outra hora grande Han, primeiro devemos aproveitar seu retorno\n\n',),
    (personagem['grim'],f'A propósito, quem é {oa} {substantivo}?\n\n',),
    (personagem['foe'],f'O nome {dele_dela} é {player_data["Nome"]}, nós {oa} achamos no Vale da noite\n\n',),
    (personagem['foe'],f'Não sabemos de onde {ele_ela} veio, perdeu a memória\n\n',),
    (personagem['grim'],f'Eu sinto resquícios de energia do vazio em você {player_data["Nome"]}, estranho\n\n',),
    (personagem['hannad'],'...\n\n',),
    (personagem['grim'],f'Bem, de qualquer forma, {oa} convido para comemorar conosco, você aceita?\n\n',),
    (personagem['player'],'S-sim, agradeço a gentileza\n\n',),
    (personagem['grim'],'Ótimo! Vamos para casa, o sol já vai se pôr, nos acompanhe\n\n\n',),

    (personagem['narrador'],
    f'Por algum motivo, a aura daquele senhor {oa} deixa assustad{oa}\n\n'
    'Mas bem, isso não importa agora, finalmente, Wysteria!\n\n\n', True),

    (personagem['outro'],'Continua...', True, True, True)
]