# Dado um array ordenado com INTEIROS DISTINTOS retornar o índice se o número desejado for encontrado.
# Caso contrário, retorne o índice onde ele seria inserido na ordem

class DistincIntegners:
    def __init__(self, *array):
        self.array = list(array)
    def SearchIndex(self):
        target = int(input('Insert below the wanted number:\n'))
        self.array.sort()
        for i in self.array:
            if i == target:
                print(f'Index where was founded the target {target}: {[i]}')
                print(self.array)
                break
        if target not in self.array:
            self.array.append(target)
            self.array.sort()
            for i in self.array:
                if i == target: # Aqui o "i" assume o valor de "target"
                    print(f'Index where was founded the target {target}: {i}')
                    print(self.array)
                    break
                
x = DistincIntegners(1,2,3,8,5,9,7)
x.SearchIndex()