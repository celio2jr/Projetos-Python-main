velocidade = float(input('Qual a velocidade do veiculo: '))

velocidade_permitida = 80
valor_multa_km = 5


if velocidade > velocidade_permitida:
    km_acima = velocidade - velocidade_permitida
    valor_multa = km_acima * valor_multa_km
    print(f'Você foi multado! A velocidade permitida é de {velocidade_permitida} Km/h.')
    print(f'Você excedeu {km_acima} Km/h e deve pagar uma multa de R$ {valor_multa:.2f}.')
else:
    print('Você esta dentro do limite de velocidade.')