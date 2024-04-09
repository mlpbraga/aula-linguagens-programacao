const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Digite o valor de a: ', (a) => {
    readline.question('Digite o valor de b: ', (b) => {
        let soma = parseInt(a) + parseInt(b);
        console.log(`A soma de a + b é: ${soma}`);
        readline.close();
    });
});
