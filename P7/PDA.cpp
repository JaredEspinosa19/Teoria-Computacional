#include "stack.h"
#include <iostream>
#include <string>
using namespace std;

std::string createString(){
	
	int n = rand() % 61; //100,000
	int c = 0;
	std::string aux;
	
	while (c<n){
		string aux1;
		aux1 = rand()%2 == 1? '1':'0';
		aux = aux + aux1;
		c++;	
	}
	
	return aux;
}

//std::string main(){

int main(){
	
	Stack PDA;
	
	///INICION PROGRAMA
	cout << "Programa que evalua si una cadena de la forma 0^n 1^n es valida" << endl;
	cout << "Escoja la opcion que quiera realizar" << endl;
	cout << "1 - Escribir la cadena \n2 - Generar la cadena aleatoriamente" << endl;
	int opcion = 0;	
	cin >> opcion;
	std::string cadena = "";
	
	if (opcion == 1){
		cout << "Escriba la cadena que desea evaluar, debe estar formada por 0's y 1's'" << endl;
		cin >> cadena;	
	}
	else if(opcion == 2){
		cadena = createString();
	}
	
	//ya se tiene la cadena, ahora crear el loop principal
	int counter = 0;
    bool auxm = true;

    while(cadena[counter] != '\0'){
		
		char aux = cadena[counter];
		//Si es cero se agrega a la pila
		cout << "Posicion actual" << endl;
		cout << aux << endl;
		if (aux=='0'){
			PDA.push(aux);
			//MANDAR A ESCRIBIR LO DEL ESTADO DIRECTOR
		}
		else{
			if (PDA.contain('0')==1){
				PDA.pop();
				//Escribir lo del estado directo
			}
			else{
				auxm = false;
				break;
			}
		}	
		++counter;
	}

	//Checar si la pila esta llena
	if (auxm==true){
		auxm = (PDA.contain('0')==1) ? false : true;
	}	//

	//DECISION FINAL
	if (auxm==true){
			cout << "Cadena valida" << endl;

	}
	else{
		cout << "Cadena invalida"<< endl;
	}	
	
	cout << "FINAL DEL PROGRAMA" << endl;
	
	return 0;

}