largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

metro_quadrado = largura * altura

quantidade_tinta = metro_quadrado / 2

print(f'Tera que ser pintado')
print(f'{metro_quadrado} metros quadrados')
print(f'Você precisara de {quantidade_tinta} litros de tinta.')