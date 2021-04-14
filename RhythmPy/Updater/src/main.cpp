#include <iostream>

using namespace std;

int main(int argc, char** argv){
    // checks if there are arguments
    if(argc < 2){
        cout << "Use --Help for Usage" << endl;
        return 0;
    }
    cout << "Hello, world!" << endl;
    return 0;
}
