# Soma de dois números

# Dado um array de inteiros 'nums' e um inteiro 'target', e RETONAR OS ÍNDICES dos números somados até o 'target'

# Cada entrada possui apenas uma solução e NÃO PODE USAR O MESMO ELEMENTO DUAS VEZES

target = 10
nums = [0,2,4,6,8,10]

arrayLength = len(nums)

for i in range(arrayLength):
    for j in range(i+1, arrayLength):
        sumNumber = nums[i] + nums[j]
        if sumNumber == target:
            print(f'Índices cuja soma é igual a {target}\n\t{i} e {j}')