class RemoteControl:
    def __init__(self, cor, altura, largura, profundidade):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.profundidade = profundidade

retomecontrol = RemoteControl('preto', 10, 5, 3)
print(retomecontrol.cor)