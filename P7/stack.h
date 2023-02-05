#include <iostream>

using namespace std;

struct Node{
		char value;
	    struct Node *next;
};

class Stack{
    private:
        struct Node *raiz {};

    public:
        Stack();
        void push(char value);
        char pop();
        char peek();
        bool contain(char value);
        void print_stack();
        

};

Stack::Stack(){
    raiz = nullptr;
}

char Stack::pop(){                
    if(raiz == nullptr){
        cout << "Empty stack"  << endl;
		return 0;
        }
    char valor {};
        
    Node *nuevo_nodo = new Node();
    nuevo_nodo = raiz;
        
	valor = nuevo_nodo->value; 
	raiz = nuevo_nodo->next;
    return valor;  
}

void Stack::push(char value ){
    if(raiz==nullptr){
        Node *nuevo_nodo = new Node();
        nuevo_nodo->value = value;
        nuevo_nodo->next = nullptr;
        raiz = nuevo_nodo;
    }
    else{
        Node *nuevo_nodo = new Node();
        nuevo_nodo->value = value;
        nuevo_nodo->next = raiz;
        raiz = nuevo_nodo;
    }
}

char Stack::peek(){
    if(raiz == nullptr){
        cout << "Empty stack"  << endl;
		return 0;
        }
    return (*raiz).value;
}

bool Stack::contain(char value){

    Node *aux = new Node();
    aux = raiz;
    while(aux->next!=nullptr){
        if(aux->value==value){
            return true;
        }
        aux = aux->next;
    }

    return false;
}

void Stack::print_stack(){
    
    Node *aux = new Node();
    aux = raiz;

    do{
        cout << aux->value << endl;
        aux = aux->next;
    }while(aux!=nullptr );
}
