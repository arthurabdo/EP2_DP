def transforma_base(lista):
    saida = {}
    for i in range(len(lista)):
        questao = lista[i]
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

import random
def sorteia_questao(questoes, nivel):
    for dificuldade, lista_questoes in questoes.items():
        if nivel== dificuldade:
            
            x= random.choice(lista_questoes)
    return x

def sorteia_questao_inedita (questoes, nivel, lista_sorteadas):
    for dificuldade, lista_questoes in questoes.items():
        if nivel== dificuldade:
            x= random.choice(lista_questoes)    
            while x in lista_sorteadas:
                x= random.choice(lista_questoes)
            
            lista_sorteadas.append(x)
            
    return x 

def questao_para_texto(questao, n):
    titulo = questao["titulo"]
    opcoes_formatadas = "\n".join(f"{opcao}: {texto}" for opcao, texto in questao["opcoes"].items())
    resposta_correta = questao["correta"]
    return f"----------------------------------------\nQUESTAO {n}\n\n{titulo}\n\nRESPOSTAS:\n{opcoes_formatadas}\n"
    
import random

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


