from game_data import game_data

player_data = game_data['player_data']

introducao = [
    ('Da sua varanda, você observa crianças jogando futebol na rua da sua casa...\n'
     'Os gritos de euforia ecoam na sua mente\n'
     'Você lembra de como foi a sua infância\n'
     'Lembra dos seus traumas...\n'
     'Das suas falhas...\n'
     'De repente, a bola de futebol cai no seu quintal\n'
     'Você recobra o juízo\n', True),

    ('Você: Ainda me lembro disso... Só queria esquecer...\n',),

    ('As crianças pedem pela bola de futebol\n'
     'Você desce as escadas para buscar\n'
     'Refletindo nos pensamentos, você acaba tropeçando\n'
     'Ao tocar o chão, você o atravessa e vê o vazio\n', True),

    ('O que é isso...???\n', False, True, True),

    ('Olhando pra trás, não existe mais nada, apenas escuridão...\n'
     'Você começa a afundar, e cada vez mais rápido\n'
     'Sua consciência começa a se esvair...\n', True),

    ('*Estrondo*\n', False, True),

    ('Desconhecido 1: O que foi isso??\n'
     'Desconhecido 2: Não faço a menor ideia...\n'
     'Desconhecido 1: Vamos dar uma olhada\n'
     'Desconhecido 2: ...\n',),

    ('......\n', False, True),

    ('Desconhecido 1: O que vamos fazer?\n'
     'Desconhecido 2: Deixa aí, não quero problemas\n'
     'Desconhecido 1: O que? Não podemos fazer isso\n'
     'Desconhecido 2: Tá, faz o que você quiser\n',),

    ('Você começa a abrir os olhos lentamente\n', True),

    ('Desconhecido 1: Ei, olha... Tá acordando...\n'
     'Desconhecido 2: ...\n'
     'Desconhecido 1: Tá tudo bem? Qual é o seu nome?\n',)
]

a_viagem = [
    ('Desconhecido 2: Consegue andar?\n'
     'Você: Consigo\n'
     'Desconhecido 1: A propósito, eu sou a Foe, o grandão é o Hannad\n'
     'Hannad: Humph\n'
     'Foe: Não liga pra ele não, ele é bem resmungão\n'
     'Hannad: Foe...\n'
     'Foe: Viu? Haha\n',),

    ('Os viajantes levam você até um reino próximo, porém...\n'
     'No meio do caminho, um monstro enorme os ataca\n'
     'Similar a um urso, porém muito maior e com características de javali e porco-espinho\n'
     'O monstro ruge em sua direção\n', True),

    ('Foe: Deixa comigo, Ignis Orbis...\n',),

    ('De repente, uma enorme bola de fogo aparece sobre Foe\n', True),

    ('Foe: Exuro.. HOSTEM!!\n',),

    ('A bola de fogo avança com tudo abrindo um buraco enorme no corpo do monstro\n', True),

    ('Hannad: Ela é incrível, não é?\n'
     'Você: ... O que.. Foi isso???\n'
     'Hannad: Nunca viu magia? De que buraco você saiu?\n'
     'Você: Também gostaria de saber...\n'
     'Foe: Uff, falando nisso, você não lembra de nada além do seu nome?\n'
     'Você: Ahm, eu consigo lembrar mas não consigo ver o que são essas memórias...\n'
     'Hannad: Pelo menos sabe como devemos te chamar? Seu corpo não parece másculo, mas seu rosto também não parece feminino, esquisito\n'
     'Foe: HANNAD!\n'
     'Hannad: O quê? É a verdade\n'
     'Foe: Por Horon, seja mais educado\n'
     f'Hannad: E então? Diga você, {player_data["Nome"]}\n',),

     ('Você se vira e olha por de baixo da roupa...\n', True)
]

pronomes = player_data["Pronomes"]
ele_ela, dele_dela, oa, seu_sua, substantivo = pronomes[0], pronomes[1], pronomes[2], pronomes[3], pronomes[4]

chegada = [
    (f'Foe: Oh, então é {player_data["Sexo"].lower()}?\n'
     'Hannad: Viu, também estava curiosa né? Haha\n'
     'Foe: Ignis Orb-\n'
     'Hannad: EU ESTAVA BRINCANDO FOE, ESPERA UM POUCO\n'
     f'Foe: Uhrum, desculpe por isso, {player_data["Nome"]}\n'
     'Você: Sem problemas, mudando de assunto, para onde estamos indo?\n'
     'Foe: Para o reino Wysteria! Ah, não conhece, né?\n'
     'Você: Não...\n'
     'Foe: Não se preocupe, você vai gostar, lá é seguro e lindo graças as árvores Wystenari\n'
     'Você: Árvores?\n'
     'Hannad: Aquele monstro que nos atacou é chamado de Abyssar\n'
     'Hannad: Um amalgamo de seres vivos que foram corrompidos pelo vazio, uma força obscura desconhecida\n'
     'Hannad: Esses monstros corrompidos odeiam árvores Wystenari, e Wysteria é cercada delas, por dentro e por fora\n'
     'Foe: Por isso é dos reinos mais seguros, nenhum monstro se aproxima de lá\n'
     'Você: Vazio...?? Vazio....\n'
     f'Foe: {player_data["Nome"]}?? Você está bem? Lembrou de algo?\n'
     'Você: Sim... Eu lembro de ter caído no vazio, só consigo lembrar isso..\n'
     'Hannad: Ha, isso é impossível, você teria virado um Abyssar\n'
     'Foe: Não é impossível, existem os magos Vhorim que pegam poder emprestado do vazio\n'
     'Hannad: Uma pequena fração, e ainda assim é suficiente pra perderem a sanidade aos poucos\n'
     f'Foe: Não acho que {pronomes[0]} está mentindo, é só olhar no rosto {pronomes[1]}\n'
     'Hannad: De qualquer forma isso não importa agora, vamos indo, o sol já vai se pôr...\n'
     'Você: Onde vamos passar a noite?\n'
     'Foe: Normalmente eu diria que está cedo, mas estamos perto de Wysteria, amanhã sairemos bem cedo, então vamos dormir\n'
     'Foe: Ferrocaelum, Murus, Vincitur!\n',),

     ('Uma grande muralha de pelo menos 10 metros se forma ao seu redor\n', True),

     ('Foe: Domus, Petra, divisa, Aedificium\n',),

     ('Logo após, uma pequena cabana com 3 divisões surge no centro da muralha\n', True),

     ('Foe: Vamos, entrem e durmam bem\n',),

     ('Todos entram em um quarto e descansam\n'
     'Em um piscar de olhos, Hannad aparece na sua frente\n', True),

     (f'Hannad: Vamos, acorde preguiços{oa}, já é de manhã\n',),

     ('Você levanta e sai da cabana ao lado de Hannad\n', True),

     (f'Foe: Bom dia dorminhoc{oa}! Murus, Dispargo, Domum, Ruina\n',),

     ('Os muros e a cabana caem e se unem de volta a terra\n', True),

     ('Foe: Devolvemos a mãe natureza o que ela nos emprestou, agora, vamos lá\n'
     'Hannad: Chegaremos em Wysteria antes do anoitecer\n',),

     ('......\n', True, True),

     ('Você observa o reino imenso de uma colina a distância\n'
     'Árvores roxas cercam todo o reino... As folhas caem pouco a pouco como árvores Sakura\n'
     'No horizonte, o pôr do sol contrasta com a aparência etérea do reino\n', True),

     ('Você: Então essa é a Wysteria? É linda...\n'
     'Desconhecido 3: Não é mesmo?\n'
     'Foe e Hannad: Grim!\n'
     'Grim: Finalmente voltaram haha, eu estava esperando por vocês\n'
     'Foe: Estava com saudade de você vovô\n'
     'Grim: O vovô também, pequena Foey\n'
     'Hannad: Infelizmente não conseguimos o que o senhor queria, mas conseguimos outra coisa\n'
     'Grim: Deixaremos isso para outra hora grande Han, primeiro devemos aproveitar seu retorno\n'
     f'Grim: A propósito, quem é {oa} {substantivo}?\n'
     f'Foe: O nome {dele_dela} é {player_data["Nome"]}, nós {oa} achamos no Vale da noite\n'
     f'Foe: Não sabemos de onde {ele_ela} veio, perdeu a memória\n'
     f'Grim: Eu sinto resquícios de energia do vazio em você {player_data["Nome"]}, estranho\n'
     'Foe e Hannad: ...\n'
     f'Grim: Bem, de qualquer forma, {oa} convido para comemorar conosco, você aceita?\n'
     'Você: S-sim, agradeço a gentileza\n'
     'Grim: Ótimo! Vamos para casa, o sol já vai se pôr, nos acompanhe\n',),

     (f'Por algum motivo, a aura daquele senhor {oa} deixa assustad{oa}\n'
      'Mas bem, isso não importa agora, finalmente, Wysteria!\n', True),

      ('Continua...', True, True, True)
]