ano_nascimento = int(input('Qual o ano de nascimento: '))

idade = 2023 - ano_nascimento
alistamento = 18

if idade > alistamento:
    idade_acima = idade - alistamento
    print(f'Você tem {idade} anos, ja se passaram {idade_acima} anos do alistamento.')
elif idade < alistamento:
    idade_abaixo = alistamento - idade
    print(f'Você tem {idade} anos, ainda faltam {idade_abaixo} anos para o alistamento.')