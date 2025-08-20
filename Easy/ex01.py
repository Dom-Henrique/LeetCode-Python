# Soma de dois números

# Dado um array de inteiros 'nums' e um inteiro 'target', e RETONAR OS ÍNDICES dos números somados até o 'target'

# Cada entrada possui apenas uma solução e NÃO PODE USAR O MESMO ELEMENTO DUAS VEZES

target = 10
nums = [0,2,4,6,8,10] # Quando 


"""for i in nums:
    firstIndex = nums[::2] 
    secondIndex = nums[i+1::2] # Tá no caminho
    sumNumbers = firstIndex + secondIndex
    print(f'{sumNumbers}')
    if sumNumbers == target:
        print(f'{sumNumbers}')
        break"""
        
for i in range(len(nums)): # Percorre cada elemento da lista
    for j in range(i+1, len(nums)): # Percorre cada elemento sucessor da lista
        sumNumbers = nums[i] + nums[j]
        if sumNumbers == target:
            print(f'Índices: {i}, {j}')
            break