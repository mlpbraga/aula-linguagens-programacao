const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Digite um texto: ', (texto) => {
  let textoInvertido = ''; // Esta linha pode precisar de ajustes

  // Verificação de palíndromo

  console.log(texto === textoInvertido ? 'É um palíndromo!' : 'Não é um palíndromo.');
  rl.close();
});
