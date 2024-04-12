#include <iostream>
#include <cstdlib>  // Necessário para rand() e srand()
#include <ctime>    // Necessário para time()

using namespace std;

int main() {
    srand(time(0)); // Inicializa o gerador de números aleatórios
    int numero_secreto = rand() % 10 + 1;
    int tentativas = 3;
    int palpite;

    while (tentativas > 0) {
        cout << "Adivinhe o número entre 1 e 10: ";
        cin >> palpite;

        if (palpite == numero_secreto) {
            cout << "Parabéns! Você acertou." << endl;
            break;
        }
        tentativas--;
    }

    return 0;
}
