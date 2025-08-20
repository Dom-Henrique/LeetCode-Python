# Dada uma string 's' que contenha apenas "()", "[]" e "{}"
# Verificar veracidade

x = input('Insert below:\n')

count = 0
for i in x:
    contarParenteses = i.count('()')
    if contarParenteses == 1:
        count += 1
    contarColchetes = i.count('[]')
    if contarColchetes == 1:
        count += 1
    contarChaves = i.count('{}')
    if contarChaves == 1:
        count += 1
if count % 2 != 0:
    print(False)
