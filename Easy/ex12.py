# Dado um inteiro largo "digits", somar 1 com o último número

class LargeItegner:
    def __init__(self, *digits):
        self.digits = list(digits)
    def PlusOne(self):
        naosei = ''
        final_number = []
        
        for i in self.digits:
            i = str(i)
            naosei += i
        naosei = int(naosei)
        summed_number = naosei + 1

        for j in str(summed_number):
            final_number.append(j)
        print(final_number)
            
x = LargeItegner(1, 2, 3)
x.PlusOne()