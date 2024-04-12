#include <iostream>
#include <string>
#include <algorithm>  // Necessário para transform() e reverse()
using namespace std;

int main() {
    string texto, texto_invertido, texto_limpo;

    cout << "Digite um texto: ";
    getline(cin, texto);

    // Complete o código aqui
  
    if (texto_limpo == texto_invertido) {
        cout << "É um palíndromo!" << endl;
    } else {
        cout << "Não é um palíndromo." << endl;
    }

    return 0;
}
