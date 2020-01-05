r = float(input('quantos reais voce tem ??:'))
d = r / 4.05
e = r / 4.54
print('Com R${:.2f} Você pode comprar US${:.2f} Dolares e €{:.2f} Euros'.format(r,d,e))