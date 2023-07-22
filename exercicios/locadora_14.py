km_percorrido = int(input('Qual a quantidade de Km percorrido: '))
quantidade_dias = int(input('Qual a quantidade de dias alugado: '))

diaria = quantidade_dias * 90
valor_km = km_percorrido * 0.20

total = diaria + valor_km

print(f'O valor total de dias é {diaria}')
print(f'O valor de km percorridos é {valor_km}')
print(f'O total a ser pago é {total}')
