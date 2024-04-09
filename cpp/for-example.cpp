#include <iostream>
#include <string>

using namespace std;

int main() {
    string palavra = "Luisa";

    for(char letra : palavra) {
        cout << "letra: " << letra << endl;
    }

    for(int i = 0; i < palavra.length() - 1; i++) {
        cout << "letra " << i << ": " << palavra[i] << endl;
    }

    return 0;
}
