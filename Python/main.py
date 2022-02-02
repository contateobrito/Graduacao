'''
Funções Built-in do Python
https://docs.python.org/pt-br/3.6/library/functions.html
são funções básicas do Python

Além disso o Python tem as palavras reservadas, que não
podem ser usadas como variáveis

objeto.atributo
objeto.método() #metódo = função
objeto.método(parametro)
'''

'''
Slice em lista, podendo ser string também. Há duas formas
variavel[inicial, final, passo] ou variavel[slice(x)]
'''

texto = 'Analise de dados é essencial para os negocios'
texto_trat = texto[::1]
print(texto_trat)
print(len(texto))
print(texto[slice(10)])

a = texto.upper()
print(a)