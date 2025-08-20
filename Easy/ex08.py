# Dada um vetor 'nums' com inteiros, gerar outro vetor sem um número 'val'

def Nums(*nums):
    list(nums)
    nums_without_val = []
    val = int(input('Which number wiched?\n'))
    for i in nums:
        if i != val:
            nums_without_val.append(i)
            
    print(f'Vetor sem o número {val}:\n{nums_without_val}')
    
Nums(1, 2, 3, 4, 2, 6, 2, 5, 5, 4, 1, 3, 8, 9, 12, 2, 3)