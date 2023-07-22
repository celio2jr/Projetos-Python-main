ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = 2023 - ano_nascimento

print

if idade > 17:
    print(f'Você tem {idade} anos e podera votar')
else:
    print(f'Você tem {idade} anos e ainda não podera votar.')