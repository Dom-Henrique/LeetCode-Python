# Dado um vetor array, criar função que encontre uma o prefixo mais longo

"""def longestPrefix():
    array = ['banana', 'barulho', 'abacate', 'cachorro', '']
    prefixTerms = []
    x = input('Insira qual prefixo desejado: ')
    for i in array:
        if x in i:
            prefixTerms.append(i)
            
    print(max(prefixTerms))"""
    


# Dado um vetor array, criar função que encontre uma o prefixo mais longo
# Prefixo estaria em evidência nas palavras

"""def longestPrefix():
    prefixCount = []
    array = ['flower', 'flow', 'flight']
    tamanho = len(array)
    
    for i in range(tamanho):
        for j in range(i+1, tamanho):
            if array[i][i] == array[j][j]:
                prefixCount.append(i)
                
    print(prefixCount)"""
                
def longestPrefix():
    array = ['flower', 'flow', 'flight']
    
longestPrefix()