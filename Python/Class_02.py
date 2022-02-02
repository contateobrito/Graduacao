class Livro():
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe')

    def imprime(self, tiutlo, isbn):
        print('Foi criado o livro %s e ISBN %d' %(self.titulo, self.isbn))

Livro2 = Livro('A menina que roubava livros', 778861)
print(Livro2.isbn)
print(Livro2.titulo)
Livro2.imprime('A menina que roubava livros', 778861)