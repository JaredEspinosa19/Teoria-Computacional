#include <iostream>
#include <string>  

using namespace std;

bool pair_automata(string &string){

    int present_state {0};
    int future_state {0};
    int counter{0};
    
    while(string[counter] != '\0'){
        switch(present_state){
            case 0:
                future_state = (string[counter++] == '1') ? 1 : 2;
                break;
            case 1:
                future_state = (string[counter++] == '1') ? 0 : 3;
                break;
            case 2:
                future_state = (string[counter++] == '1') ? 3 : 0;
                break;
            case 3:
                future_state = (string[counter++] == '1') ? 2 : 1;
                break;
            default:
                std::cerr << "Error al procesar la cadena" << std::endl;
                break;
        }
        present_state = future_state;
    }  

    return (present_state == 0 ) ? true : false;

}