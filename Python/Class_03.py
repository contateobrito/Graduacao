class Cachorro():
    def __init__(self, raca):
        self.raca = raca
        #print('Construtor chamado para criar um objeto desta classe')

#------------------------------------------------------------------------

Rex = Cachorro('Labrador')
Cacau = Cachorro('salsicha')

print(Cacau.raca)
print(Rex.raca)