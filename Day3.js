// para leitura
const readline = require('readline');
const forInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


// primeira instrução 
function firstQuestion(){
    forInput.question('Qual área deseja seguir? \n1- Back-end; \n2- Front-end.\n ', (area) =>{
        if(area != '1' && area != '2'){
            console.log('Escolha "1" ou "2", vamos tentar novamente.')
            firstQuestion()
        }else if(area === "1"){
            console.log('Olha, boa escolha!')
            secondQuestion('1- Java \n2- C#\n')
        }else if(area === '2'){
            console.log('Olha, boa escolha!')
            secondQuestion('1- Vue \n2- React')
        }
    })


}


// segunda instrução

function secondQuestion(tecnologias){
    forInput.question(`Escolha uma tecnologia para sua área: \n${tecnologias} `, (tecnologia) =>{
        if(tecnologia != '1' && tecnologia != '2'){
            console.log('Escolha "1" ou "2", vamos tentar novamente.')
            return secondQuestion(tecnologias)
        }else{
            console.log('hmmm legal...')
            return thirdQuestion()
        }
        

    })
}


// terceira instrução
function thirdQuestion(){
    forInput.question('Sabe, além de Back-end e Front-end, tambem há o FullStack \ngostaria de saber mais? \n1- Sim, gostaria. \n2- Não... \n', (thirdAnswer) =>{
        if(thirdAnswer != '1' && thirdAnswer != '2'){
            console.log('Escolha "1" ou "2", vamos tentar novamente.')
            return thirdQuestion()
        }else if(thirdAnswer === '1'){
            console.log('Um desenvolvedor Fullstack é alguém que possui habilidades tanto no desenvolvimento Back-end, quanto no Front-end, ele é um faz tudo!')
            fourthQuestion('Vamos falar dos seus interesses agora,\nquais linguagens gostaria de aprender?\n')
        }else if(thirdAnswer === '2'){
            console.log('ok...')
            fourthQuestion('Vamos falar dos seus interesses agora,\nquais linguagens gostaria de aprender?\n')
        }
    })

}

// quarta instrução
let list = [];
function fourthQuestion(question){
    forInput.question(question, (linguagens) =>{
        list.push(linguagens)
        forInput.question('deseja citar outra linguagem? \n1- sim \n2- não', (fourthAnswer) =>{
            if(fourthAnswer != '1' && fourthAnswer != '2'){
                console.log('Escolha "1" ou "2", vamos tentar novamente.')
                return fourthQuestion(question)
            }else if(fourthAnswer === '1'){
                return fourthQuestion('vamos lá, diga outra:\n')
            }else if(fourthAnswer === '2'){
                console.log('suas linguagens:')
                for(let i = 0; i < list.length; i++){
                    console.log(list[i])
                }
            }
            forInput.close()
        })
    }
    )
}

firstQuestion()

