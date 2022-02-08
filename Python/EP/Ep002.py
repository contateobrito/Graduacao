def main():
    '''(None) -> None 

    Coloque sua solução individual abaixo, seguindo o enunciado do 
    exercício EP02 na página da disciplina.

    Siga as instruções para entrega disponíveis em:
    https://paca.ime.usp.br/mod/page/view.php?id=42515
    
    '''
    # escreva seu programa a seguir
    print('\n')
    n = int(input("Digite n: "))
    s = 0

    for i in range(1,n+1):
        print('\n')
        a = float(input("Digite um número: "))
        s += a
        print('Soma parcial %d = %.1f' %(i,s))
    print('Média = %d' %(s/n))
    print('\n')

    # fim da main()

# =========================================================
# NÃO MODIFIQUE AS LINHAS ABAIXO
# ELAS SÃO NECESSÁRIAS PARA O CORRETOR AUTOMÁTICO
# =========================================================

if __name__ == "__main__":
    main()