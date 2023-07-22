nome = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

valor_media = 7.0
media_aluno = (nota1 + nota2) / 2

if media_aluno > valor_media:
    print(f'Parabens! {nome}, Sua media é {media_aluno} e você ficou acima da media de {valor_media}.')
else:
    print(f'{nome}, sua media é {media_aluno} e infelismente você ficou abaixo da media {valor_media}.')