metros = float(input('Digite uma distancia em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'A distancia de {metros} metros equivale a:')
print(f'{km} Km')
print(f'{hm} Hm')
print(f'{dam} Dam')
print(f'{dm} dm')
print(f'{cm} cm')
print(f'{mm} mm')