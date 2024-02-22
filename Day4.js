const readline = require('readline');
const forInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// gerar numero aleatório

function generateNumber(number, difficulty){
    let generatedNumber = Math.floor(Math.random() * number) + 1
    console.log(`você escolheu ${difficulty}! vamos começar`)
    findNumber(generatedNumber)
}

// começar o jogo

function findNumber(generatedNumber){
    forInput.question('adivinhe o número!\n', (chosenNumber)=>{
        if(chosenNumber > generatedNumber){
            console.log('seu número é maior! tente um numero menor')
            return findNumber(generatedNumber)
        }else if(chosenNumber < generatedNumber){
            console.log('seu número é menor! tente um numero maior')
            return findNumber(generatedNumber)
        }else if(chosenNumber = generatedNumber){
            console.log('VOCÊ ACERTOUUU!!!')
        }
        forInput.close()
    })
}

// iniciar do jogador
    forInput.question('vamos jogar?\n1- sim\n2- não\n>>', (answer) =>{
        forInput.question('escolha a dificuldade:\n1- fácil(1 a 10)\n2- medio(1 a 50)\n3- dificil(1 a 100)', (difficulty) =>{
            if (difficulty === '1'){
                
                generateNumber(10, 'facil')
            }else if(difficulty === '2'){
                
                generateNumber(50, 'medio')
            }else if(difficulty === '3'){
                
                generateNumber(100, 'dificil')
            }
        })

    })