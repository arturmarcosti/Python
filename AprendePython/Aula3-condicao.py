a = int (input('Primeiro Valor:'))
b = int (input('Segundo Valor:'))
c = int (input('Teceiro Valor:'))

if a > b and a > c:
    print('O maior número é: {}' .format(a))
elif b > a and b > c:
    print('O maior número é: {}' .format(b))
else:
    print('O maior número é: {}'.format(c))
print('Final do Programa')

