#include "Pair_auto.h"
#include <bits/stdc++.h>
#include <string>   
#include <conio.h>
#include <stdio.h>
#include <iostream>
#include <time.h>
#include <windows.h>

void generate_string(char string []){

    for(int i{0}; i<10; ++i){
        string[i] = 48 + (rand()%2);
    }
    string[10] = '\0';
}
void write_message(){ 
    
    std::ofstream out_file{"message.txt", std::ios::app};
    std::ofstream aux_file{"ayudante.txt", std::ios::app};
    
    if (!out_file || !aux_file) {
        std::cerr << "Error opening input file" << std::endl;
        exit(0);
    }

    char string [11] {};
 
    for(int i{0}; i<10; ++i){
        generate_string(string);
        out_file << string << std::endl;
        aux_file << string << std::endl;     
    }

    out_file << '\n';

    out_file.close();
    aux_file.close();
}

void analize_message(){

    std::ofstream pair_file{"pair.txt", std::ios::app};
    std::ofstream unpair_file{"unpair.txt", std::ios::app};

    std::ifstream auxiliar_file;
    auxiliar_file.open("ayudante.txt");

    if (!pair_file || !unpair_file || !auxiliar_file) {
        std::cerr << "Problem opening file" << std::endl;
        exit(0);
    }
    
    std::string line{};

    while(std::getline(auxiliar_file, line)){
    	
        if(pair_automata(line) == true){
            pair_file << line << std::endl;
        }
        else{
            unpair_file << line << std::endl;
        }
    }

    unpair_file << '\n';
    pair_file << '\n';

    unpair_file.close();
    pair_file.close();
    auxiliar_file.close();

    remove("ayudante.txt");

}

int main(){

    int present_state {0};
    int future_state {};
    do{
    	std::cout << "Start of protocol" << std::endl;
    	std::cout << "Writing message..."<< std::endl;
    	write_message();
    	std::cout << "Wait 1 second" << std::endl;
		sleep(1);
    	std::cout << "Analizing message..." << std::endl;
    	analize_message();
    	std:: cout << "Message sent :)" << std::endl;    	
         
    }while(rand()%2 !=1); //Sea diferente de uno

    std::cout << "End of protocol" <<std::endl;

	return 0;
}