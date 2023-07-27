import random


def transforma_base(questoes):
    saida = {}
    for i in range(len(questao)):
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


print('Bem vindo! Você está na Fortuna DesSoft! Aqui terá a oportunidade de enriquecer!')
nome = input(str('Seu nome: '))
print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas\n As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"! ')
print('Aperte ENTER para iniciar')

premio = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
ajuda = 2
pulos = 3
n_questao = 0
acertos = 0
end = False
