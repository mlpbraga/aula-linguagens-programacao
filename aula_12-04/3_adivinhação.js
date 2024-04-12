const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
const numeroSecreto = Math.floor(Math.random() * 10 + 1);
let tentativas = 3;

function adivinhar() {
  rl.question('Adivinhe o número entre 1 e 10: ', (palpite) => {
    // Lógica do jogo

    rl.close();
  });
}

adivinhar();
