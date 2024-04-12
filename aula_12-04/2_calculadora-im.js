const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Digite seu peso em kg: ', (peso) => {
  rl.question('Digite sua altura em metros: ', (altura) => {
    let imc = 0; // Cálculo do IMC

    // Classificação do IMC

    console.log(`Seu IMC é ${imc} e sua classificação é: `);
    rl.close();
  });
});
