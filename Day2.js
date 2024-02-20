//- Qual o seu nome?
//- Quantos anos você tem?
//- Qual linguagem de programação você está estudando?


//  para leitura no terminal
const readline = require('readline');
const forInput = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


//.question para os input
forInput.question('Qual o seu nome? ', (nome) => {
    forInput.question('Quantos anos você tem? ', (anos) => {
        forInput.question('Qual linguagem de programação você está estudando? ', (linguagem) => {
            
            console.log(`Seu nome é ${nome}, tem ${anos} anos e estuda ${linguagem}.`)

            forInput.question(`você está feliz estudando ${linguagem}? \n(responda com sim ou não)\n`, (simORno) => {
                let resposta = simORno.includes('sim') ? 'Muito bom! Continue estudando e você terá muito sucesso.' : 'Ahh que pena... Já tentou aprender outras linguagens?' 

                console.log(resposta)

                //  indicar o fim da funcação
                forInput.close();
            });
        });
    });
});