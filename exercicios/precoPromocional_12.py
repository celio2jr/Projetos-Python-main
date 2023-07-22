valor_produto = float(input('Digite o valor do produto: '))

desconto = 5 / 100 * valor_produto
valor_promocional = valor_produto - desconto

print(f'O seu produto com 5% de desconto é R${valor_promocional}')