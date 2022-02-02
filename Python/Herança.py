'''
Em herança dom funções de mesmo nome o python seleciona a mais interna
'''
class Animal():

    def __init__(self):
        print('Animal criado')
    def Identif(self):
        print('Animal')
    def comer(self):
        print('comendo')

class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Objeto Cachorro criado')
    def Identif(self):
        print('Cachorro')
    def latir(self):
        print('Au Au')

#------------------------------------

rex = Cachorro()
rex.Identif()
rex.comer()
rex.latir()