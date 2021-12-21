nome = input(' escreva seu nome: ')

nota1 = float(input('escreva sua nota 1: '))
nota2 = float(input('escreva sua nota 2: '))
nota3 = float(input('escreva sua nota 3: '))
nota4 = float(input('escreva sua nota 4: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print('Ola {}, a sua média ficou: {:.2f} '.format(nome, media))
