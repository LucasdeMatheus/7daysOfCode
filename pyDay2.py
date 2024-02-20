#   Qual o seu nome?
#   Quantos anos você tem?
#   Qual linguagem de programação você está estudando?


nome = input('Qual o seu nome? ')
idade = input('Quantos anos você tem? ')
linguagem = input('Qual linguagem de programação você está estudando? ')

print(f'Seu nome é {nome}, tem {idade} e estuda sim{linguagem}')

feedback = input(f'você está feliz estudando {linguagem}? \n(responda com sim ou não)\n')

mensagem = "Muito bom! Continue estudando e você terá muito sucesso." if 'sim' in feedback else "Ahh que pena... Já tentou aprender outras linguagens?"

print(mensagem)