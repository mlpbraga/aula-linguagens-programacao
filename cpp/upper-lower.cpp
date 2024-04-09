#include <iostream>
#include <string>
#include <cctype> // Para as funções tolower() e toupper()

using namespace std;

int main() {
    string nome, sobrenome;

    // Obtendo o nome e o sobrenome do usuário
    getline(cin, nome);
    getline(cin, sobrenome);

    // Convertendo o primeiro caractere do nome para minúsculo e o restante para maiúsculo
    nome[0] = tolower(nome[0]);
    for (size_t i = 1; i < nome.size(); ++i) {
        nome[i] = toupper(nome[i]);
    }

    // Convertendo o primeiro caractere do sobrenome para maiúsculo e o restante para minúsculo
    sobrenome[0] = toupper(sobrenome[0]);
    for (size_t i = 1; i < sobrenome.size(); ++i) {
        sobrenome[i] = tolower(sobrenome[i]);
    }

    // Imprimindo o nome e o sobrenome modificados
    cout << nome << endl;
    cout << sobrenome << endl;

    return 0;
}
