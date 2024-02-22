# bibliotecas
import random


# isso aqui serve pra nada não, só pra interação kkk
answer = input('vamos jogar?\n>>')

# gera o numero de acordo com a dificuldade
def generateNumber(number, difficulty): 
    numberGeneret = random.randint(0, number)
    print(f'você escolheu a dificuldade {difficulty}, vamos começar!')
    findNumber(numberGeneret)


# inicar jogo --
def findNumber(generatedNumber):
    chosenNumber = input('adivinhe o número!\n')
    if chosenNumber is '':
        print('ué? vamos tentar novamente')
        return findNumber(generatedNumber)
    else:
        if int(chosenNumber) < int(generatedNumber):
            print('seu número é menor! tente um numero maior')
            return findNumber(generatedNumber)
        elif int(chosenNumber) > int(generatedNumber):
            print('seu número é maior! tente um número menor')
            return findNumber(generatedNumber)
        else:
            print('você acertou!!!!')


# seletor dificuldade --
difficulty = input('escolha a dificuldade:\n1- fácil(1 a 10)\n2- medio(1 a 50)\n3- dificil(1 a 100)')
if difficulty == '1':
    generateNumber(10, 'facil')
elif difficulty == '2':
    generateNumber(50, 'medio')
elif difficulty == '3':
    generateNumber(100, 'dificil')