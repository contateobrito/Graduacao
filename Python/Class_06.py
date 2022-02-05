class Livro():
    def __init__(self, titulo, autor, paginas):
        print('Livro criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return 'Titulo: %s, autor %s, páginas: %s' \
    %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas
    def len(self):
        return print('print do livro com método comum', self.paginas)

#-----------------------------------------------------------------------
livro1 = Livro('Os lusiadas','Luis de Camoes',8816)
#print(livro1)
#str(livro1)

livro1.len()
#len(livro1)
#print(livro1.__len__())

#del livro1.paginas

#hasattr(livro1,'paginas')