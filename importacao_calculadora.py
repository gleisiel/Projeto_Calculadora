from calculadora import *

while True:
    print ('''
======================================
            CALCULADORA
======================================
OPERAÇÕES:
    1 Para somar
    2 Para subtrair
    3 Para multiplicar
    4 Para dividir
    x Para encerrar a calculadora
======================================
        ''')

op = input('Entre com a operação: ')
if op == 'x':
    print('Encerrando a calculadora...')
    break
    
n1 = int(input("Digite o Primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

match op:
    case '1':
        print(f'Resultado:{adicao(a,b)}')
    case '2':
        print(f'Resultado:{subtracao(a,b)}')
    case '3':
        print(f'Resultado:{multiplicacao(a,b)}')
    case '4':
        print(f'Resultado:{divisao(a,b)}')
    case '_':
            print (f'[ERRO] Opção inválida')