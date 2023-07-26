def transforma_base(lista):
    saida = {}
    for i in range(len(lista)):
        questao = lista[i]
        nivel = questao['nivel'] 
        if nivel not in saida:
            saida[nivel] = []
        saida[nivel].append(questao)
    return saida

def valida_questao(dic):
    saida = {}
    titulo  = dic['titulo']
    nivel = dic['nivel']
    dic_opcoes = dic['opcoes']
    correta = ['correta']
    if titulo == '':
        saida['titulo'] = 'nao_encontrado'
    if titulo == ' ':
        saida['titulo'] = 'vazio'
    if nivel != 'facil' or nivel != 'medio ' or nivel != 'dificil':
        saida['nivel'] = 'valor_errado'
    if len(dic_opcoes) != 4:
        saida['opcoes'] = 'tamanho_invalido'
         
         
