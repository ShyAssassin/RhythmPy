#include <iostream>
#include "Commands.hpp"

using namespace std;

// used for string switch
constexpr unsigned int str2int(const char *str, int h = 0)
{
    return !str[h] ? 5381 : (str2int(str, h + 1) * 33) ^ str[h];
}

int main(int argc, char *argv)
{
    // checks if there are arguments
    if (argc < 2)
    {
        cout << "Use --Help for Usage" << endl;
        return 0;
    }

    switch (str2int(argv))
    {
    case str2int("--help"):
        Help();
        break;

    case str2int("--checkupdate"):
        CheckUpdate();
        break;

    case str2int("--update"):
        Update();
        break;

    default:
        cout << "Invallid input, Use --Help for Usage" << endl;
        return 1;
    }
}
