# Calcular a raiz quadrada de um inteiro não negativo
from math import sqrt, floor

class SqrtInt:
    def __init__(self, number):
        self.number = number
    def sqrt_int(self):
        sqrt_int = sqrt(self.number)
        sqrt_int = floor(sqrt_int)
        print(f'Square root of {self.number} is {sqrt_int}.')
        
x = SqrtInt(6)
x.sqrt_int()