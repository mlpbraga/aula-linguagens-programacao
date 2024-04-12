#include <iostream>
using namespace std;

int main() {
    double peso, altura, imc;
    string classificacao;

    cout << "Digite seu peso em kg: ";
    cin >> peso;
    cout << "Digite sua altura em metros: ";
    cin >> altura;

    imc = 0 // Cálculo do IMC precisa ser corrigido

    if (imc < 18.5) {
        classificacao = "Baixo peso";
    } else if (imc < 30) {
        classificacao = "Sobrepeso";
    } else {
        classificacao = "Obesidade";
    }

    cout << "Seu IMC é " << imc << " e sua classificação é: " << classificacao << endl;

    return 0;
}
