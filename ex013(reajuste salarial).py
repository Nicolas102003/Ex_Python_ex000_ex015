sal = float(input('Qual é o valor do seu salário ??'))
d = int(input('Qual a porcentagem de aumento que voê teve ??'))
val = ((d *sal)/100) + sal
print('O seu novo salário é de R${:.2f}'.format(val))
