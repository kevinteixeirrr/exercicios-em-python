salario = float(input('Escreva o seu salário: R$'))
p = float(input('Escreva o seu percentual de aumento: '))

valorf = (p / 100) * salario
soma = valorf + salario

print('O salário de R${:.2f} teve um aumento de {}% e foi para R${:.2f}'.format(salario, p, soma))