#include <iostream>
#include <string>

using namespace std;

int main() {
    string nome;
    int posicao;

    cout << "nome: ";
    cin >> nome;
    cout << "posição: ";
    cin >> posicao;

    if (nome[posicao] == 'R') {
        nome[posicao] = 'S';
    } else if (nome[posicao] == 'r') {
        nome[posicao] = 's';
    } else if (nome[posicao] == 'M') {
        nome[posicao] = 'N';
    } else if (nome[posicao] == 'm') {
        nome[posicao] = 'n';
    } else {
        nome.erase(posicao, 1);
    }

    cout << "reformulado: " << nome << endl;
    return 0;
}
