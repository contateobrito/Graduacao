'''Tipo de variavés
Demonstrar o resultado da operação entre variavés de tipos distintos
'''
def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado do 
    exercício EP01 na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515

    SUGESTÃO: Simule o programa antes de executar 
    cada exemplo. Em particular, para cada expressão, 
    além do valor do resultado, você deve saber se o 
    tipo do resultado é int, float ou str.

    '''
    # escreva seu programa a seguir
    p = str(input("Digite uma palavra p: "))
    i = int(input("Digite um inteiro i: "))
    r = float(input("Digite um real r: "))
    print("\nResultado de p + p:", p+p)
    print("Resultado de i + i:", i+i)  
    print("Resultado de r + r:", r+r)
    print("Resultado de i * p:", i*p)
    print("Resultado de i * i:", i*i)
    print("Resultado de i * r:", i*r)
    print("Resultado de r / i:", r/i)
    print("Resultado de 2 * i / i:", 2*i/i)
    print("Resultado de i / i * 2:", i/i*2)
    
    # fim da main()

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()