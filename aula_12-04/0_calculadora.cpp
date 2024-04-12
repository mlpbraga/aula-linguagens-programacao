#include <iostream>
using namespace std;

int main() {
    double valor1, valor2;
    char operador;
    double resultado = 0;

    cout << "Digite o primeiro valor: ";
    cin >> valor1;
    cout << "Digite o operador: ";
    cin >> operador;
    cout << "Digite o segundo valor: ";
    cin >> valor2;

    if (operador == '+') {
        resultado = valor1 + valor2;
    } else {
        cout << "Operador inválido";
    }

    cout << "Resultado: " << resultado << endl;

    return 0;
}
