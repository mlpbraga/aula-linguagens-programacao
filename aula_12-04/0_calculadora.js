const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Digite o primeiro valor: ', (valor1) => {
  rl.question('Digite o operador: ', (operador) => {
    rl.question('Digite o segundo valor: ', (valor2) => {
      let resultado = 0;

      // Cálculo da operação

      console.log(`Resultado: ${resultado}`);
      rl.close();
    });
  });
});
