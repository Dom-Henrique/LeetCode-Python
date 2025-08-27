# Dado um array ordenado com INTEIROS DISTINTOS retornar o índice se o número desejado for encontrado.
# Caso contrário, retorne o índice onde ele seria inserido na ordem

class DistincIntegners:
    def __init__(self, *array):
        self.array = list(array)
    def SearchIndex(self):
        target = int(input('Insert below the wanted number:\n'))
        self.array.sort()
        print(f'Index where was founded the target {target}: {self.array.index(target)}')
        print(self.array)
        if target not in self.array:
            self.array.append(target)
            self.array.sort()
            print(f'Index where was founded the target {target}: {self.array.index(target)}')
            print(self.array)
                
x = DistincIntegners(1,2,3,8,5,9,7)
x.SearchIndex()