'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome =(input('Informe o nome: ')).strip()
div_nome = nome.split()

print('Nome:{}'.format(div_nome[0]))
print('ultimo sobrenome: {}'.format(div_nome[len(div_nome)-1]))
