const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

// Função para ler a entrada do usuário de forma assíncrona
function askQuestion(query) {
    return new Promise(resolve => {
        readline.question(query, resolve);
    });
}

async function main() {
  // Solicitando o nome e sobrenome do usuário
  let nome = await askQuestion("Digite seu nome: ");
  let sobrenome = await askQuestion("Digite seu sobrenome: ");

  // Convertendo o primeiro caractere do nome para minúsculo e o restante para maiúsculo
  nome = nome.charAt(0).toLowerCase() + nome.slice(1).toUpperCase();

  // Convertendo o primeiro caractere do sobrenome para maiúsculo e o restante para minúsculo
  sobrenome = sobrenome.charAt(0).toUpperCase() + sobrenome.slice(1).toLowerCase();

  // Exibindo o resultado
  console.log(nome);
  console.log(sobrenome);

  // Fechando o readline
  readline.close();
}

main();
