import random


def transforma_base(questoes):
    saida = {}
    for i in range(len(questoes)):
        questao = questoes[i]
        nivel = questao['nivel'] 
        if nivel not in saida:
            saida[nivel] = []
        saida[nivel].append(questao)
    return saida

def valida_questao(questao):

    erros = {}

    chaves = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves:
        if chave not in questao:
            erros[chave] = 'nao_encontrado'

    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'

    if 'titulo' in questao and not questao['titulo'].strip():
        erros['titulo'] = 'vazio'

    niveis = ['facil', 'medio', 'dificil']
    if 'nivel' in questao and questao['nivel'] not in niveis:
        erros['nivel'] = 'valor_errado'


    if 'opcoes' in questao and len(questao['opcoes']) != 4:
        erros['opcoes'] = 'tamanho_invalido'
    else:
    
        alternativas = ['A', 'B', 'C', 'D']
        opcoes_existentes = set(questao.get('opcoes', {}).keys())
        if not opcoes_existentes.issubset(alternativas):
            erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'

        opcoes_vazias = {opcao: 'vazia' for opcao, resposta in questao.get('opcoes', {}).items() if not resposta.strip()}
        if opcoes_vazias:
            erros['opcoes'] = opcoes_vazias


    if 'correta' in questao and questao['correta'] not in ['A', 'B', 'C', 'D']:
        erros['correta'] = 'valor_errado'


    return erros

def valida_questoes (lista_questoes):
    lista = []
    for i in range (len(lista_questoes)):
        lista.append(valida_questao(lista_questoes[i]))
    
    return lista 


def sorteia_questao(questoes, nivel):
    for dificuldade, lista_questoes in questoes.items():
        if nivel== dificuldade:
            
            x= random.choice(lista_questoes)
    return x

def sorteia_questao_inedita (questoes, nivel, lista_sorteadas):
    for dificuldade, lista_por_nivel in questoes.items():
        if nivel== dificuldade:
            x= random.choice(lista_por_nivel)    
            while x in lista_sorteadas:
                x= random.choice(lista_por_nivel)
            
            lista_sorteadas.append(x)
            
    return x 

def questao_para_texto(questao, n):
    titulo = questao["titulo"]
    opcoes_formatadas = "\n".join(f"{opcao}: {texto}" for opcao, texto in questao["opcoes"].items())
    resposta_correta = questao["correta"]
    return f"----------------------------------------\nQUESTAO {n}\n\n{titulo}\n\nRESPOSTAS:\n{opcoes_formatadas}\n"
    

def gera_ajuda(questao):

    titulo = questao["titulo"]
    opcoes = questao["opcoes"]
    correta = questao["correta"]

    incorretas = [opcoes[opcao] for opcao in opcoes if opcao != correta]
    
    num_incorretas = len(incorretas)
    
    num_opcoes_ajuda = random.randint(1, 2)
    opcoes_ajuda = random.sample(incorretas, num_opcoes_ajuda)
    

    dica = f"DICA:\nOpções certamente erradas: {' | '.join(opcoes_ajuda)}"
    
    return dica


premio = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
ajuda = 2
pulos = 3
n_questao = 0
acertos = 0
jogo = False 

questoes_ja_sorteadas = []

ordem_nivel = { 0:'facil', 1:'facil', 2:'facil', 3:'medio', 4:'medio', 5:'medio', 6: 'dificil', 7:'dificil', 8: 'dificil', 9:'dificil'}


questoes = [
  {
      "titulo": "Qual é o resultado de 3 + 7?",
      "nivel": "facil",
      "opcoes": {
          "A": "9",
          "B": "10",
          "C": "11",
          "D": "12"
      },
      "correta": "B"
  },
  {
      "titulo": "Em que ano ocorreu a Revolução Francesa?",
      "nivel": "facil",
      "opcoes": {
          "A": "1787",
          "B": "1788",
          "C": "1789",
          "D": "1790"
      },
      "correta": "C"
  },
  {
      "titulo": "Qual é o maior rio do mundo?",
      "nivel": "facil",
      "opcoes": {
          "A": "Rio Nilo",
          "B": "Rio Amazonas",
          "C": "Rio Yangtzé",
          "D": "Rio Mississipi"
      },
      "correta": "B"
  },
  {
      "titulo": "Qual é o dobro de 15?",
      "nivel": "facil",
      "opcoes": {
          "A": "20",
          "B": "25",
          "C": "30",
          "D": "35"
      },
      "correta": "C"
  },
  {
      "titulo": "Quem foi o primeiro presidente dos Estados Unidos?",
      "nivel": "facil",
      "opcoes": {
          "A": "Thomas Jefferson",
          "B": "George Washington",
          "C": "Benjamin Franklin",
          "D": "John Adams"
      },
      "correta": "B"
  },
  {
    "titulo": "Qual destes números é primo?",
    "nivel": "medio",
    "opcoes": {
      "A": "259",
      "B": "85",
      "C": "49",
      "D": "19"
    },
    "correta": "D"
  },
  {
    "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
    "nivel": "medio",
    "opcoes": {
      "A": "Collatz",
      "B": "Goldbach",
      "C": "Poincaré",
      "D": "Hodge"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
    "nivel": "medio",
    "opcoes": {
      "A": "Cristiano Ronaldo",
      "B": "Dwayne Johnson",
      "C": "Kim Kardashian",
      "D": "Kylie Jenner"
    },
    "correta": "D"
  },
  {
    "titulo": "O que é um período de 1000 anos chamado?",
    "nivel": "medio",
    "opcoes": {
        "A": "Século",
        "B": "Milênio",
        "C": "Década",
        "D": "Milenar"
    },
    "correta": "B"
  },
  {
    "titulo": "Qual é o maior órgão do corpo humano?",
    "nivel": "medio",
    "opcoes": {
        "A": "Coração",
        "B": "Fígado",
        "C": "Pulmões",
        "D": "Pele"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual é o planeta mais próximo do Sol?",
    "nivel": "medio",
    "opcoes": {
        "A": "Marte",
        "B": "Vênus",
        "C": "Terra",
        "D": "Mercúrio"
    },
    "correta": "D"
  },
  {
  "titulo": "Qual é o maior animal terrestre?",
  "nivel": "medio",
  "opcoes": {
      "A": "Elefante africano",
      "B": "Girafa",
      "C": "Baleia azul",
      "D": "Rinoceronte branco"
  },
  "correta": "A"
  },
  {
    "titulo": "Quem pintou a obra 'Mona Lisa'?",
    "nivel": "medio",
    "opcoes": {
        "A": "Vincent van Gogh",
        "B": "Pablo Picasso",
        "C": "Leonardo da Vinci",
        "D": "Michelangelo"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual é o nome da famosa estátua da Grécia Antiga que foi esculpida em mármore de Paros?",
    "nivel": "medio",
    "opcoes": {
        "A": "Vênus de Milo",
        "B": "Estátua da Liberdade",
        "C": "David",
        "D": "Cristo Redentor"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o maior país do mundo em área territorial?",
    "nivel": "medio",
    "opcoes": {
        "A": "Canadá",
        "B": "Rússia",
        "C": "Estados Unidos",
        "D": "China"
    },
    "correta": "B"
  },
  {
    "titulo": "Qual é a capital da Austrália?",
    "nivel": "medio",
    "opcoes": {
        "A": "Sydney",
        "B": "Melbourne",
        "C": "Canberra",
        "D": "Brisbane"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual é o maior rio do mundo em volume de água?",
    "nivel": "medio",
    "opcoes": {
        "A": "Amazonas",
        "B": "Nilo",
        "C": "Mississipi",
        "D": "Yangtzé"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o maior oceano da Terra?",
    "nivel": "medio",
    "opcoes": {
        "A": "Atlântico",
        "B": "Índico",
        "C": "Ártico",
        "D": "Pacífico"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual é a cidade mais populosa do mundo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Tóquio",
        "B": "Mumbai",
        "C": "Nova Delhi",
        "D": "São Paulo"
    },
    "correta": "A"
  },
  {
    "titulo": "Quem foi o primeiro presidente do Brasil?",
    "nivel": "medio",
    "opcoes": {
        "A": "Getúlio Vargas",
        "B": "Juscelino Kubitschek",
        "C": "Prudente de Morais",
        "D": "D. Pedro II"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual é a montanha mais alta do mundo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Monte Everest",
        "B": "Monte Kilimanjaro",
        "C": "Monte Aconcágua",
        "D": "Monte Denali"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o maior deserto do mundo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Deserto do Saara",
        "B": "Deserto do Atacama",
        "C": "Deserto de Gobi",
        "D": "Deserto da Arábia"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o elemento químico mais abundante na crosta terrestre?",
    "nivel": "medio",
    "opcoes": {
        "A": "Oxigênio",
        "B": "Carbono",
        "C": "Silício",
        "D": "Alumínio"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual é o nome da famosa pintura que retrata a criação de Adão, feita por Michelangelo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Última Ceia",
        "B": "A Criação de Eva",
        "C": "O Nascimento de Vênus",
        "D": "A Criação de Adão"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual é a língua mais falada no mundo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Inglês",
        "B": "Espanhol",
        "C": "Hindi",
        "D": "Mandarim"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual é o maior animal do mundo?",
    "nivel": "medio",
    "opcoes": {
        "A": "Elefante africano",
        "B": "Tubarão-baleia",
        "C": "Baleia azul",
        "D": "Girafa"
    },
    "correta": "C"
  },
  {
    "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
    "nivel": "dificil",
    "opcoes": {
      "A": "Autogamia",
      "B": "Esporulação",
      "C": "Partenogênese",
      "D": "Divisão binária"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
    "nivel": "dificil",
    "opcoes": {
      "A": "441",
      "B": "86",
      "C": "Nenhuma das outras respostas",
      "D": "23"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual é a maior cordilheira do mundo?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Cordilheira dos Andes",
        "B": "Cordilheira do Himalaia",
        "C": "Montanhas Rochosas",
        "D": "Cordilheira dos Alpes"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é a maior bacia hidrográfica do mundo?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Bacia Amazônica",
        "B": "Bacia do Congo",
        "C": "Bacia do Rio da Prata",
        "D": "Bacia do Nilo"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é a maior bacia hidrográfica do mundo?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Bacia Amazônica",
        "B": "Bacia do Congo",
        "C": "Bacia do Rio da Prata",
        "D": "Bacia do Nilo"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o país com maior número de ilhas?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Filipinas",
        "B": "Indonésia",
        "C": "Japão",
        "D": "Noruega"
    },
    "correta": "B"
  },
  {
    "titulo": "Qual é a maior usina hidrelétrica do mundo?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Usina de Itaipu",
        "B": "Usina de Três Gargantas",
        "C": "Usina de Belo Monte",
        "D": "Usina de Grand Coulee"
    },
    "correta": "B"
  },
  {
    "titulo": "Quem foi o primeiro homem a caminhar na Lua?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Yuri Gagarin",
        "B": "Buzz Aldrin",
        "C": "Neil Armstrong",
        "D": "Alan Shepard"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual é o país com maior número de vulcões ativos?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Indonésia",
        "B": "Japão",
        "C": "Itália",
        "D": "Estados Unidos"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o único mamífero capaz de voar?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Morcego",
        "B": "Esquilo",
        "C": "Pterossauro",
        "D": "Ave do paraíso"
    },
    "correta": "A"
  },
  {
    "titulo": "Qual é o maior desfiladeiro do mundo?",
    "nivel": "dificil",
    "opcoes": {
        "A": "Grand Canyon",
        "B": "Cânion do Colca",
        "C": "Desfiladeiro de Taroko",
        "D": "Cânion de Blyde River"
    },
    "correta": "A"
  },
  {
    "titulo": "complete: Chega de mentiras, de negar o meu desejo, eu te quero mais que tudo, ____________",
    "nivel": "dificil",
    "opcoes": {
        "A": "Eu preciso do seu beijo",
        "B": "E eu quero seu chamego",
        "C": "Amanhã eu não te deixo",
        "D": "Fico triste sem seu cheiro"
    },
    "correta": "A"

    },
    {
      "titulo": "Qual é o livro mais vendido no mundo, após a Bíblia?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Cem Anos de Solidão",
          "B": "Dom Quixote",
          "C": "O Pequeno Príncipe",
          "D": "O Alquimista"
      },
      "correta": "B"
    },
    {
      "titulo": "Qual é a cidade mais antiga do mundo?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Jerusalém",
          "B": "Atenas",
          "C": "Roma",
          "D": "Damasco"
      },
      "correta": "D"
    },
    {
      "titulo": "Quem é o autor da obra '1984'?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Aldous Huxley",
          "B": "George Orwell",
          "C": "Ray Bradbury",
          "D": "Kurt Vonnegut"
      },
      "correta": "B"
    },
    {
      "titulo": "Qual é a montanha mais alta da América do Norte?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Monte McKinley (Denali)",
          "B": "Monte Logan",
          "C": "Monte Aconcágua",
          "D": "Monte Whitney"
      },
      "correta": "A"
    },
    {
      "titulo": "Quem foi o cientista que formulou a teoria da relatividade?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Isaac Newton",
          "B": "Albert Einstein",
          "C": "Niels Bohr",
          "D": "Galileu Galilei"
      },
      "correta": "B"
    },
    {
      "titulo": "Qual é a capital da Índia?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Mumbai",
          "B": "Nova Delhi",
          "C": "Bangalore",
          "D": "Calcutá"
      },
      "correta": "B"
    },
    {
      "titulo": "Qual é a maior ilha do mundo?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Groenlândia",
          "B": "Bornéu",
          "C": "Nova Guiné",
          "D": "Madagascar"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual é o elemento químico mais leve?",
      "nivel": "dificil",
      "opcoes": {
          "A": "Hidrogênio",
          "B": "Hélio",
          "C": "Lítio",
          "D": "Oxigênio"
      },
      "correta": "A"
    }
    ]


questoes_em_niveis = transforma_base(questoes)

def texto_verde(texto):
  print("\033[80m" + texto + "\033[00m")
  pass

def texto_vermelho(texto):
  print("\033[79m" + texto + "\033[00m")
  pass

def enter(enter):
  input('Aperte ENTER para iniciar')
  pass

print('Bem vindo! Você está na Fortuna DesSoft! Aqui terá a oportunidade de enriquecer!')
nome = input(str('Seu nome: '))
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas\n As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ')
inicio = input ('Aperte ENTER para continuar...')
while True:
    if inicio == '':
        break
print ('\n''O jogo já vai começar! Lá vem a primeira questão!''\n')
inicio1 = input ('Vamos começar com questões do nível FACIL!''\n''Aperte ENTER para continuar...')
while True:
    if inicio1 == '':
        break

while not jogo:
  questao_atual = sorteia_questao_inedita(questoes_em_niveis, ordem_nivel[acertos], questoes_ja_sorteadas)
  n_questao += 1
  finaliza_questao = False
  precisou_de_ajuda = False 

  while not finaliza_questao and not jogo:
    print(questao_para_texto(questao_atual,n_questao ))
    resposta = input ('Qual sua resposta?!')

    if resposta == questao_atual['correta']:
      acertos += 1
      texto_verde(f'Você acertou! Seu prêmio atual é de R$ {premio[acertos]:.2f}')
      finaliza_questao = True

    elif resposta == 'pula':
      if pulos == 0:
        texto_vermelho('Não deu! Você não tem mais direios a pulos!')
        input('Aperte ENTER para continuar...')
      else:
        pulos -= 1 
        if pulos == 0:
          print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!')
          input('Aperte ENTER para continuar...')#tem isso??
          finaliza_questao = True
        else:
          print(f'Ok, pulando! Você ainda tem {pulos} pulos!')
          finaliza_questao = True

    elif resposta == 'ajuda':
      if ajuda == 0:
        texto_vermelho('Não deu! Você não tem mais direito a ajuda!')
        input('Aperte ENTER para continuar...')
      elif precisou_de_ajuda:
        texto_vermelho('Não deu! Você já pediu ajuda nesta questão!')
        input('Aperte ENTER para continuar...')
      else:
        ajuda -= 1
        precisou_de_ajuda = True 
        print(gera_ajuda(questao_atual))
        print(f'Ok, lá vem ajuda! Você ainda tem {ajuda} ajudas!')
        input('Aperte ENTER para continuar...')

    elif resposta == 'parar':
      parar = input(f'Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {premio[acertos]:.2f}!')

      if parar == 'S':
        jogo = True
      else:
        texto_vermelho('Opção inválida!')
        parar = input(f'Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {premio[acertos]:.2f}!')

    elif resposta in ['A', 'B', 'C', 'D']:
        texto_vermelho('Que pena! Você errou e vai sair sem nada :(')
        jogo = True
    else:
        texto_vermelho('Opção inválida!')
        print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' ou 'parar'")
        resposta = input ('Qual sua resposta?!')  

  if acertos == 9:
    texto_verde('PARABÉNS, você zerou o jogo e ganhou um milhão de reais!')   
          

