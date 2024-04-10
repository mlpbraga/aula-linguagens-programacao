const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Função para perguntar ao usuário e receber a entrada como uma promessa
function ask(question) {
    return new Promise(resolve => readline.question(question, resolve));
}

async function main() {
    const nome = await ask("nome: ");
    const posicaoStr = await ask("posição: ");
    const posicao = parseInt(posicaoStr, 10);

    let nomeModificado = nome.split(''); // Converte a string em um array para modificar

    if (nomeModificado[posicao] === 'R') {
        nomeModificado[posicao] = 'S';
    } else if (nomeModificado[posicao] === 'r') {
        nomeModificado[posicao] = 's';
    } else if (nomeModificado[posicao] === 'M') {
        nomeModificado[posicao] = 'N';
    } else if (nomeModificado[posicao] === 'm') {
        nomeModificado[posicao] = 'n';
    } else {
        nomeModificado.splice(posicao, 1); // Remove o caractere na posição
    }

    nomeModificado = nomeModificado.join(''); // Converte o array de volta para string
    console.log("reformulado:", nomeModificado);

    readline.close();
}

main();
