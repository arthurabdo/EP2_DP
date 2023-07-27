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
         
         
