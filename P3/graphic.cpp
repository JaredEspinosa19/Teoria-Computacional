#include<conio.h>
#include<graphics.h>
#include<math.h>
#include <stdio.h>
#include <string.h>

#define HEIGHT 800
#define WIDTH 800

void fillCircle(int x, int y, int color){
	setfillstyle(SOLID_FILL, color);
	floodfill(x,y, WHITE);
}

int main(){
	
	//Definir circulo
	int radius = 60;
	int x=WIDTH/4,y=HEIGHT/3; 
		
	initwindow(WIDTH, HEIGHT);
	outtextxy((WIDTH/2)-50, 40 ,"PROTOCOL AUTOMATA");
	//Dibujar circulo
	//estados
	circle(x, y, radius); //1
	circle(x*3, y, radius); //3
	circle(x*2, 2*y/3, radius-20); //2
	circle(x*2, y*2, radius-20); //4
	//
	setfillstyle(SOLID_FILL, WHITE);
	circle((x*3)- (radius+3),y, 3);
	floodfill((x*3)- (radius+3),y, WHITE);
	
	circle(x,y+(radius+3),3);	
	floodfill(x,y+(radius+3), WHITE);
	
	circle(x*2+(radius-20)+3,y*2,3);
	floodfill(x*2+(radius-20)+3,y*2, WHITE);
	
	circle(x*2-(radius-20)-3,2*y/3, 3);
	floodfill(x*2-(radius-20)-3,2*y/3, WHITE);

	circle(x-radius-1,y,3);
	floodfill(x-radius-1,y,WHITE);
	
	circle(x*3, y-radius-2, 3);
	floodfill(x*3, y-radius-3, WHITE);
	//lineas
	line(x+radius,y,x*2-(radius-20)-3,2*y/3);
	line(x*2+(radius-20), 2*y/3,(x*3)- (radius+3),y);
	line(x*3, y+radius,x*2+(radius-20)+3,y*2);
	line(x*2-(radius-20), y*2,x,y+(radius+3));
	line(x/3,y*1.2, x-radius,y);
	line(x*3 +radius,y,x*3 + 2*radius,y);
	line(x*3 + 2*radius,y,x*3 + 2*radius, y-radius-2);
	line(x*3 + 2*radius, y-radius-2,x*3, y-radius-2);
	
	//titles
	outtextxy((WIDTH/2)-50, y/2-10 ,"DATA IN");
	outtextxy(x, y-radius-20 ,"READY");
	outtextxy(x*3, y-radius-20 ,"SENDING");
	outtextxy(x*2, y*2-radius-20 ,"CHECKING");
	
	//ANIMACION
	getch();
	do{
		setcolor(BLACK);
		outtextxy(x*2-100, y*2-radius+140 ,"Try again  Space = N Other key = Y");
		
		fillCircle(x, y, BLUE);
		delay(1500);
		fillCircle(x,y, BLACK);
		
		int counter=0;
		while(counter!=6*2){
			fillCircle(x*2, 2*y/3, BLUE);
			delay(250);
			fillCircle(x*2, 2*y/3, BLACK);
			delay(250);
			counter+=1;
		}
		
		fillCircle(x*3, y, BLUE);
		delay(1500);
		fillCircle(x*3, y, BLACK);
		delay(1000);
		fillCircle(x*3, y, BLUE);
		delay(1500);
		fillCircle(x*3, y, BLACK);
				
		int counter2=0;
		while(counter2!=6*2){
			fillCircle(x*2, y*2, GREEN);
			delay(250);
			fillCircle(x*2, y*2, RED);
			delay(250);
			counter2+=1;
		}
		
		fillCircle(x*2-20, y*2, BLACK);
		setcolor(WHITE);
		outtextxy(x*2-100, y*2-radius+140 ,"Try again  Space = N Other key = Y");
	}while(getch()!=32);	
	
	closegraph();
	
	return 0;
	
}