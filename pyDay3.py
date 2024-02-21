# primeira instrução
def firstQuestion():
    firstAnswer = input('Qual área deseja seguir? \n1- Back-end; \n2- Front-end.\n ')
    if firstAnswer != '1' and firstAnswer != '2':
        print('Escolha "1" ou "2", vamos tentar novamente.')
        firstQuestion()
    elif firstAnswer == '1':
        print('Olha, boa escolha!')
        secondQuestion('1- Java \n2- C#\n')
    elif firstAnswer == '2':
        print('Olha, boa escolha!')
        secondQuestion('1- Vue \n2- React\n')


# segunda instrução

def secondQuestion(tecnologias):
    secondAnswer = input(f'Escolha uma tecnologia para sua área: \n{tecnologias} ')
    if secondAnswer != '1' and secondAnswer != '2':
        print('Escolha "1" ou "2", vamos tentar novamente.')
        return secondQuestion(tecnologias)
    else:
        print('hmmm legal...')
        thirdQuestion()


# terceira instrução

def thirdQuestion():
    thirdAnswer = input('Sabe, além de Back-end e Front-end, tambem há o FullStack \ngostaria de saber mais? \n1- Sim, gostaria. \n2- Não... \n')
    if thirdAnswer != '1' and thirdAnswer != '2':
        print('Escolha "1" ou "2", vamos tentar novamente.')
        return thirdQuestion()
    elif thirdAnswer == '1':
        print('Um desenvolvedor Fullstack é alguém que possui habilidades tanto no desenvolvimento Back-end, quanto no Front-end, ele é um faz tudo!')
        fourthQuestion('Vamos falar dos seus interesses agora,\nquais linguagens gostaria de aprender?\n')
    elif thirdAnswer == '2':
        print('ok...')
        fourthQuestion('Vamos falar dos seus interesses agora,\nquais linguagens gostaria de aprender?\n')


# quarta instrução

list = []
def fourthQuestion(question):
    fourthAnswer = input(question)
    list.append(fourthAnswer)
    answerYN = input('deseja citar outra linguagem? \n1- sim \n2- não')
    if answerYN != '1' and answerYN != '2':
        print('Escolha "1" ou "2", vamos tentar novamente.')
        return fourthQuestion(question)
    elif answerYN == '1':
        return fourthQuestion('vamos lá, diga outra:\n')
    elif answerYN == '2':
        print('suas linguagens:')
        for i in range(len(list)):
            print(list[i])


firstQuestion()
    