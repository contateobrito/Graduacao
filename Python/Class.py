class Livro():
    def __init__(self):
        self.titulo = 'O monge e o Executivo'
        self.isbn = 998888
        print('Construtor chamado para criar um objeto desta classe')

    def imprime(self):
        print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

Livro1 = Livro()
Livro1
print(Livro1.isbn)
print(Livro1.titulo)
Livro1.imprime()