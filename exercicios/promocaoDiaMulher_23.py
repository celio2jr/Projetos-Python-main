nome = input('Digite seu nome: ')
sexo = input('Digite o sexo (F/M): ')
valor_compras = float(input('Digite o valor das compras: '))

desconto_homens = 5 / 100 * valor_compras
desconto_mulheres = 13 / 100 * valor_compras

if sexo == 'F':
    total_compra = valor_compras - desconto_mulheres
    print(f'Ola {nome}, o valor da sua compra com desconto de 13% ficara em R$ {total_compra}.')
elif sexo == 'M':
    total_compra2 = valor_compras - desconto_homens
    print(f'Ola {nome} o valor da sua compra com desconto de 5% ficara em  R$ {total_compra2}.')
else:
    print('A indentificação do sexo não foi inserida ou foi inserida incorretamente.')
