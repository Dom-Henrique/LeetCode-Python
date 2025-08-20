# Verificar se o número é um palíndromo

print('*'*50)
print('Veirify if number is palyndrome')
print('*'*50)

palyndrome = int(input('Insert a number: '))
palyndrome = str(palyndrome)

number = []

for x in palyndrome:
    number.append(x)
    
print(number)

for i in range(len(number)):
    if number[i] == number[-i]:
        print('Yes')