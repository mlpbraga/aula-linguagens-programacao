const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Digite um texto: ', (texto) => {
  let numeroDePalavras = 0;

  // Código para contar palavras

  console.log(`O número de palavras é: ${numeroDePalavras}`);
  rl.close();
});
