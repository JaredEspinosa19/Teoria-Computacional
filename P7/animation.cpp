#include<conio.h>
#include<graphics.h>
#include<math.h>
#include <stdio.h>
#include <string.h>
#include <iostream>

#define HEIGHT 800
#define WIDTH 800

void fillCircle(int x, int y, int color){
	setfillstyle(SOLID_FILL, color);
	floodfill(x,y, WHITE);
}

using namespace std;


int main(){
	
	//Crea la ventana
	initwindow(WIDTH, HEIGHT);
	
	//CADENAS DE ENTRADA
	
	char cadena []= "00001111";
	int n = sizeof(cadena)/sizeof(char)-1;
	
	
	//Inicializacion
	settextstyle(EUROPEAN_FONT, HORIZ_DIR,3);
	outtextxy(WIDTH*.45,HEIGHT*.2,cadena);
	
	rectangle(WIDTH*.47,HEIGHT*.27,WIDTH*.53,HEIGHT*.33);
	line(WIDTH*.5,HEIGHT*.33,WIDTH*.5,HEIGHT*.40);
	rectangle(WIDTH*.40,HEIGHT*.40,WIDTH*.60,HEIGHT*.60);
	
	char result [10000] = "Zo";
	char X [] = "X"; 
	
	settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
	outtextxy(WIDTH*.45,HEIGHT*.70,result);

	getch();
	char uno [] = "1";
	char cero [] = "0";
	char p [] = "p";
	char q [] = "q";
	char null1 [] = "_";
	char f [] = "f";
 
 	int counter = 0;
 	int dif = 0;
 	int count2 = 2;
 
 	do{
 		char a = cadena[counter];
 		
 		if (a=='1'){
 			settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
 			outtextxy(WIDTH*.49,HEIGHT*.30,uno);
 			settextstyle(EUROPEAN_FONT, HORIZ_DIR,5);
 			outtextxy(WIDTH*.50,HEIGHT*.45,q);
 			
 		
 			dif = dif-1;
 			
 			result[count2] = '_'; 
 			
 			settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
 			outtextxy(WIDTH*.44,HEIGHT*.70,result);
 			++count2;
		 }
		
		else{
			settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
			outtextxy(WIDTH*.49,HEIGHT*.30, cero);
			settextstyle(EUROPEAN_FONT, HORIZ_DIR,5);
 			outtextxy(WIDTH*.50,HEIGHT*.45,p);
 			
 			dif= dif +1;
 			
			settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
 			outtextxy(WIDTH*.44,HEIGHT*.70,strcat(result,X));
 			
		
		}
		
 		cout <<result << endl;
		delay(1000);
 		cadena[counter] = 95;
 		settextstyle(EUROPEAN_FONT, HORIZ_DIR,3);
		outtextxy(WIDTH*.45,HEIGHT*.2,cadena);

 		++counter;
 		getch();
	} 
	while( (counter < n) && dif!=0); 



	settextstyle(EUROPEAN_FONT, HORIZ_DIR,1);
	outtextxy(WIDTH*.49,HEIGHT*.30, null1);
	settextstyle(EUROPEAN_FONT, HORIZ_DIR,5);
 	outtextxy(WIDTH*.50,HEIGHT*.45,f);
 	settextstyle(EUROPEAN_FONT, HORIZ_DIR,3);
	outtextxy(WIDTH*.45,HEIGHT*.2,cadena);
	
	
	getch();
	closegraph();
	
	return 0;
	
}
