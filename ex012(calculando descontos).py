vp = int(input('Quanto custa o produto ??'))
d = int(input('Quanto de desconto o produto tem ??'))
vf  = (d * vp)/100
vf = vp - vf
print('O valor desse produto com {}% de desconto é R${:.2f}'.format(d,vf))
