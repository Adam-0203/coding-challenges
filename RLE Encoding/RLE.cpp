#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;


string encode_rle(const string& text)
{
    string res;
    auto current = text[0];
    int counter = 1;

    for (size_t i=1; i<text.length() ; ++i)
    {
        if (text[i] == text[i-1])
        {
            counter++;
        }
        else
        {
            res += current;
            res += to_string(counter);
            current = text[i];
            counter = 1;
        }
    }

    res += current;
    res += to_string(counter);
    return res;
}


int main()
{
    //input
    string input;
    cout << "entrer une chainde de caractère: ";
    getline(cin, input);

    cout << "l'encodage RLE : " << encode_rle(input) << endl;

}
