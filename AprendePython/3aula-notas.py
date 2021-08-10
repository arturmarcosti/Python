a=int(input ('Primeiro Bimestre: '))
if a>10 :
    a=int(input ('Você digitou errado. Digite novamente o Primeiro Bimestre:'))
b=int(input ('Segundo Bimestre: '))
if b>10 :
    b=int(input ('Você digitou errado. Digite novamente o Segundo Bimestre:'))
c=int(input ('Terceiro Bimestre: '))
if c>10 :
    c=int(input ('Você digitou errado. Digite novamente o Terceiro Bimestre:'))
d=int(input ('Quarto Bimestre: '))
if d>10 :
    d=int(input ('Você digitou errado. Digite novamente o Quarto Bimestre:'))
media=(a+b+c+d) / 4
print('A média é: {}' .format (media))

## primeira versão sugerida
#if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#    print('A média é: {}' .format (media))
#else:
#    print('Alguma nota foi informada errada!')
