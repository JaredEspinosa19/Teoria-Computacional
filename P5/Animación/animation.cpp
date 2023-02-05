#include<iostream>
#include<graphics.h>
#include<cstdlib>
#include<string>
#include<fstream>
#include<ctime>
#include<windows.h>
#include<stdlib.h>
#include<time.h>
using namespace std;

void sleepcp(int milliseconds) // Cross-platform sleep function
{
    #ifdef _WIN32
        Sleep(milliseconds);
    #else
        usleep(milliseconds * 3000);
    #endif // _WIN32
}

void dibujoAutomataPalabras(){
    int colorAleat0 = rand()%16;
    int colorAleat1 = rand()%16;
    int colorAleat2 = rand()%16;
    int colorAleat3 = rand()%16;
    int colorAleat4 = rand()%16;

    
    // Start:
    setcolor(9);
    line(10, 370, 50, 330);       
    line(40, 330, 50, 330); 
    line(50, 340, 50, 330);       
    outtextxy(5, 345, "Z0");
    circle(70, 330, 15);      /* INICIO */
    
    setcolor(9);
    line(70, 315, 105, 205);
    line(85, 330, 105, 355);
    line(70, 345, 105, 430);
    setcolor(3);
    outtextxy(75, 255, "c");
    outtextxy(95, 325, "d");
    outtextxy(75, 380, "g");

    //circle(10, 30, 15);     /* Q Inicial */
    setcolor(9);
    circle(120, 205, 15);      /* A -   'a1,a2,a3,a4,a5' */
    circle(120, 355, 15);      /* B - 	'a6,a7' */
    circle(120, 430, 15);
	setcolor(15);     /* C -   'a8' */
    outtextxy(115, 200, "A");
    outtextxy(115, 350, "B");
    outtextxy(115, 425, "C");
	setcolor(9);
    line(120, 190, 155, 105);  /* flecha (A -> D) */
    line(135, 205, 155, 205);  /* flecha (A -> E) */
    line(120, 220, 155, 280);  /* flecha (A -> F) */
    line(135, 355, 155, 330);  /* flecha (B -> G) */
    line(135, 355, 155, 380);  /* flecha (B -> H) */
    line(135, 430, 155, 430);  /* flecha (C -> I) */
    setcolor(3);
	outtextxy(120, 145, "a");
    outtextxy(140, 188, "o");
    outtextxy(120, 242, "u");
    outtextxy(140, 328, "i");
    outtextxy(137, 368, "o");
    outtextxy(140, 412, "r");

    setcolor(11);
    circle(170, 105, 15);      /* D -   'b1,b2' */
    circle(170, 205, 15);      /* E -   'b3,b4' */
    circle(170, 280, 15);      /* F -   'b5' */
    setcolor(14);
    circle(170, 330, 15);      /* G -   'b6' */
    circle(170, 380, 15);      /* H -   'b7' */
    setcolor(10);
    circle(170, 430, 15);      /* I -	'b8' */

    setcolor(15);
    outtextxy(165, 100, "D");
    outtextxy(165, 200, "E");
    outtextxy(165, 275, "F");
    setcolor(15);
    outtextxy(165, 325, "G");
    outtextxy(165, 375, "H");
    outtextxy(165, 425, "I");
    setcolor(9);
    line(185, 105, 205, 80);  /* flecha (D -> J) */
    line(185, 105, 205, 130);  /* flecha (D -> K) */
    line(185, 205, 205, 180);  /* flecha (E -> L) */
    line(185, 205, 205, 230);  /* flecha (E -> M) */
    line(185, 280, 205, 280);  /* flecha (F -> N) */
    line(185, 330, 205, 330);  /* flecha (G -> O) */
    line(185, 380, 205, 380);  /* flecha (H -> P) */
    line(185, 430, 205, 430);  /* flecha (I -> Q) */
	setcolor(11);    
	outtextxy(185, 78, "l");
    outtextxy(185, 115, "n");
    outtextxy(185, 180, "n");
    outtextxy(185, 215, "v");
    outtextxy(190, 262, "b");
    outtextxy(190, 312, "s");
    outtextxy(190, 362, "l");
    outtextxy(190, 412, "i");

    setcolor(9);
    circle(220, 80, 15);      /* J -	'c1' */
    circle(220, 130, 15);      /* K -	'c2' */
    setcolor(9);
    circle(220, 180, 15);      /* L -	'c3' */
    circle(220, 230, 15);      /* M -	'c4' */
    circle(220, 280, 15);      /* N -	'c5' */
    circle(220, 330, 15);      /* O -	'c6' */
    circle(220, 380, 15);      /* P -	'c7' */
    circle(220, 430, 15);
	setcolor(15);      /* Q -	'c8' */
    outtextxy(215, 75, "J");
    outtextxy(215, 125, "K");
    outtextxy(215, 175, "L");
    outtextxy(215, 225, "M");
    outtextxy(215, 275, "N");
    outtextxy(215, 325, "O");
    outtextxy(215, 375, "P");
    outtextxy(215, 425, "Q");
    setcolor(9);
    line(235, 80, 255, 80);  /* flecha (J -> R) */
    line(235, 130, 255, 130);  /* flecha (K -> S) */
    line(235, 180, 255, 180);  /* flecha (L -> T) */
    line(235, 230, 255, 230);  /* flecha (M -> U) */
    line(235, 280, 255, 280);  /* flecha (N -> V) */
    line(235, 330, 255, 330);  /* flecha (O -> W) */
    line(235, 380, 255, 380);  /* flecha (P -> X) */
    line(235, 430, 255, 430);  /* flecha (Q -> Y) */
    setcolor(11);
	outtextxy(245, 62, "e");
    outtextxy(245, 112, "s");
    outtextxy(245, 162, "t");
    outtextxy(245, 212, "i");
    outtextxy(245, 262, "r");
    outtextxy(245, 312, "t");
    outtextxy(245, 362, "o");
    outtextxy(245, 412, "p");

	setcolor(9);
    circle(270, 80, 15);      /* R -	'd1' */
    circle(270, 130, 15);      /* S -	'd2' */
    circle(270, 180, 15);      /* T -	'd3' */
    circle(270, 230, 15);      /* U -	'd4' */
    circle(270, 280, 15);      /* V -	'd5' */
    circle(270, 330, 15);      /* W -	'd6' */
    circle(270, 380, 15);      /* X -	'd7' */
    circle(270, 430, 15);      /* Y -	'd8' */
    setcolor(15);
	outtextxy(265, 75, "R");
    outtextxy(265, 125, "S");
    outtextxy(265, 175, "T");
    outtextxy(265, 225, "U");
    outtextxy(265, 275, "V");
    outtextxy(265, 325, "W");
    outtextxy(265, 375, "X");
    outtextxy(265, 425, "Y");
    setcolor(9);
    line(285, 80, 305, 80);  /* flecha (I -> Q) */
    line(285, 130, 305, 130);  /* flecha (I -> Q) */
    line(285, 180, 305, 180);  /* flecha (I -> Q) */
    line(285, 230, 305, 230);  /* flecha (I -> Q) */
    line(285, 280, 305, 280);  /* flecha (I -> Q) */
    line(285, 330, 305, 330);  /* flecha (I -> Q) */
    line(285, 380, 305, 380);  /* flecha (I -> Q) */
    line(285, 430, 305, 430);  /* flecha (I -> Q) */
    setcolor(11);
	outtextxy(290, 62, "n");
    outtextxy(290, 112, "a");
    outtextxy(290, 162, "a");
    outtextxy(290, 212, "d");
    outtextxy(290, 262, "e");
    outtextxy(290, 312, "a");
    outtextxy(290, 362, "r");
    outtextxy(290, 412, "a");
	setcolor(9);
    circle(320, 80, 15);      /* Z -	'e1' */
    circle(320, 130, 15);      /* AA -	'e2' */
    circle(320, 180, 15);      /* AB -	'e3' */
    circle(320, 230, 15);      /* AC -	'e4' */
    circle(320, 230, 12);
    circle(320, 280, 15);      /* AD -	'e5' */
    circle(320, 330, 15);      /* AE -	'e6' */
    circle(320, 380, 15);      /* AF -	'e7' */
    circle(320, 380, 12);
    circle(320, 430, 15);      /* AG -	'e8' */
    circle(320, 430, 12);
    setcolor(15);
    outtextxy(315, 72, "Z");
    outtextxy(312, 122, "AA");
    outtextxy(312, 172, "AB");
    outtextxy(312, 222, "AC");
    outtextxy(312, 272, "AD");
    outtextxy(312, 322, "AE");
    outtextxy(312, 372, "AF");
    outtextxy(312, 422, "AG");
    setcolor(9);
    line(335, 80, 355, 80);  /* flecha (Z -> AH) */
    line(335, 130, 355, 130);  /* flecha (AA -> AI) */
    line(335, 180, 355, 180);  /* flecha (AB -> AJ) */
    line(335, 280, 355, 280);  /* flecha (AD -> AK) */
    line(335, 330, 355, 330);  /* flecha (AE -> AL) */
    setcolor(11);
	outtextxy(340, 62, "t");
    outtextxy(340, 112, "n");
    outtextxy(340, 162, "g");
    outtextxy(340, 262, "b");
    outtextxy(340, 312, "n");
    
    
	setcolor(9);
    circle(370, 80, 15);      /* AH -	'f1' */
    circle(370, 130, 15);      /* AI -	'f2' */
    circle(370, 180, 15);      /* AJ -	'f3' */

    circle(370, 280, 15);      /* AK -	'f5' */
    circle(370, 330, 15);      /* AL -	'f6' */
    
	setcolor(15);
	outtextxy(362, 72, "AH");
    outtextxy(362, 122, "AI");
    outtextxy(362, 172, "AJ");
    outtextxy(362, 272, "AK");
    outtextxy(362, 322, "AL");
	setcolor(9);
    line(385, 80, 405, 80);  /* flecha (AH -> AM) */
    line(385, 130, 405, 130);  /* flecha (AI -> AN) */
    line(385, 180, 405, 180);  /* flecha (AJ -> AO) */
    line(385, 280, 405, 280);  /* flecha (AK -> AP) */
    line(385, 330, 405, 330);  /* flecha (AL -> AQ) */
    setcolor(11);
	outtextxy(390, 62, "u");
    outtextxy(390, 112, "c");
    outtextxy(390, 162, "i");
    outtextxy(390, 262, "o");
    outtextxy(390, 312, "c");
	setcolor(9);
    circle(420, 80, 15);      /* AM -	'g1' */
    circle(420, 130, 15);      /* AN -	'g2' */
    circle(420, 180, 15);      /* AO -	'g3' */

    circle(420, 280, 15);      /* AP -	'g5' */
    circle(420, 330, 15);      /* AQ -	'g6' */
    setcolor(15);
	outtextxy(412, 72, "AM");
    outtextxy(412, 122, "AN");
    outtextxy(412, 172, "AO");
    outtextxy(412, 272, "AP");
    outtextxy(412, 322, "AQ");
	setcolor(9);
    line(435, 80, 455, 80);  /* flecha (AM -> AR) */
    line(435, 130, 455, 130);  /* flecha (AN -> AS) */
    line(435, 180, 455, 180);  /* flecha (AO -> AT) */
    line(435, 280, 455, 280);  /* flecha (AP -> AU) */
    line(435, 330, 455, 330);  /* flecha (AQ -> AV) */
    setcolor(11);
	outtextxy(440, 62, "r");
    outtextxy(440, 112, "i");
    outtextxy(440, 162, "o");
    outtextxy(440, 262, "c");
    outtextxy(440, 312, "i");
	setcolor(9);
    circle(470, 80, 15);      /* AR -	'h1' */
    circle(470, 130, 15);      /* AS -	'h2' */
    circle(470, 180, 15);      /* AT -	'h3' */
    circle(470, 180, 12);

    circle(470, 280, 15);      /* AU -	'h4' */
    circle(470, 330, 15);
	setcolor(15);      /* AV -	'h6' */
    outtextxy(462, 72, "AR");
    outtextxy(462, 122, "AS");
    outtextxy(462, 172, "AT");
    outtextxy(462, 272, "AU");
    outtextxy(462, 322, "AV");
	setcolor(9);
    line(488, 80, 505, 80);  /* flecha (AR -> AW) */
    line(485, 130, 505, 130);  /* flecha (AS -> AX) */
    line(485, 280, 505, 280);  /* flecha (AU -> AY) */
    line(485, 330, 505, 330);  /* flecha (AV -> AZ) */
    setcolor(11);
	outtextxy(490, 62, "a");
    outtextxy(490, 112, "o");
    outtextxy(490, 262, "a");
    outtextxy(490, 312, "a");

	setcolor(9);
    circle(520, 80, 15);      /* AW -	'i1' */
    circle(520, 80, 12);
    circle(520, 130, 15);      /* AX -	'i2' */
    circle(520, 130, 12);

    circle(520, 280, 15);      /* AY -	'i5,b1,b2' */
    circle(520, 330, 15);      /* AZ -	'i6' */
    circle(520, 330, 12);
    setcolor(15);
	outtextxy(512, 72, "AW");
    outtextxy(512, 122, "AX");
    outtextxy(512, 272, "AY");
    outtextxy(512, 322, "AZ");
	setcolor(9);
    line(535, 280, 555, 280);  /* flecha (AY -> BA) */
    setcolor(15);
	outtextxy(540, 262, "s");
	setcolor(9);
    circle(570, 280, 15);      /* BA -	'j5' */
    circle(570, 280, 12);
    setcolor(15);
	outtextxy(562, 272, "BA");


    // Conexiones entre estados : 
    setcolor(12);
    circle(105, 205, 2);
    circle(105, 355, 2);      /* B - 	'a6,a7' */
    circle(105, 430, 2);      /* C -   'a8' */
    circle(155, 105, 2);      /* D -   'b1,b2' */
    circle(155, 205, 2);      /* E -   'b3,b4' */
    circle(155, 280, 2);      /* F -   'b5' */
    circle(155, 330, 2);      /* G -   'b6' */
    circle(155, 380, 2);      /* H -   'b7' */
    circle(155, 430, 2);      /* I -	'b8' */
    circle(205, 80, 2);      /* J -	'c1' */
    circle(205, 130, 2);      /* K -	'c2' */
    circle(205, 180, 2);      /* L -	'c3' */
    circle(205, 230, 2);      /* M -	'c4' */
    circle(205, 280, 2);      /* N -	'c5' */
    circle(205, 330, 2);      /* O -	'c6' */
    circle(205, 380, 2);      /* P -	'c7' */
    circle(205, 430, 2);      /* Q -	'c8' */
    circle(255, 80, 2);      /* R -	'd1' */
    circle(255, 130, 2);      /* S -	'd2' */
    circle(255, 180, 2);      /* T -	'd3' */
    circle(255, 230, 2);      /* U -	'd4' */
    circle(255, 280, 2);      /* V -	'd5' */
    circle(255, 330, 2);      /* W -	'd6' */
    circle(255, 380, 2);      /* X -	'd7' */
    circle(255, 430, 2);      /* Y -	'd8' */
    circle(305, 80, 2);      /* Z -	'e1' */
    circle(305, 130, 2);      /* AA -	'e2' */
    circle(305, 180, 2);      /* AB -	'e3' */
    circle(305, 230, 2);      /* AC -	'e4' */
    circle(305, 280, 2);      /* AD -	'e5' */
    circle(305, 330, 2);      /* AE -	'e6' */
    circle(305, 380, 2);      /* AF -	'e7' */
    circle(305, 430, 2);      /* AG -	'e8' */
    circle(355, 80, 2);      /* AH -	'f1' */
    circle(355, 130, 2);      /* AI -	'f2' */
    circle(355, 180, 2);      /* AJ -	'f3' */
    circle(355, 280, 2);      /* AK -	'f5' */
    circle(355, 330, 2);      /* AL -	'f6' */
    circle(405, 80, 2);      /* AM -	'g1' */
    circle(405, 130, 2);      /* AN -	'g2' */
    circle(405, 180, 2);      /* AO -	'g3' */
    circle(405, 280, 2);      /* AP -	'g5' */
    circle(405, 330, 2);      /* AQ -	'g6' */
    circle(455, 80, 2);      /* AR -	'h1' */
    circle(455, 130, 2);      /* AS -	'h2' */
    circle(455, 180, 2);      /* AT -	'h3' */
    circle(455, 280, 2);      /* AU -	'h4' */
    circle(455, 330, 2);      /* AV -	'h6' */
    circle(505, 80, 2);      /* AW -	'i1' */
    circle(505, 130, 2);      /* AX -	'i2' */
    circle(505, 280, 2);      /* AY -	'i5,b1,b2' */
    circle(505, 330, 2);      /* AZ -	'i6' */
    circle(555, 280, 2);      /* BA -	'j5' */


    setcolor(11);
    // Retornos de AN:
    outtextxy(405, 105, "*");
    // Retornos de AU:
    outtextxy(455, 255, "*");
    // Retornos de AQ:
    outtextxy(405, 305, "*");



    setcolor(10);
    // Retornos de AJ:
    outtextxy(355, 155, "*");

    // Retornos de AC:
    setcolor(14);
    outtextxy(305, 205, "*");

    // Retornos de AY:
    setcolor(9);
    outtextxy(505, 255, "*");

    setcolor(15);
    outtextxy(40, 500, "Los estados marcados con un * pueden ir a los estados con circulo del mismo color que el *");
	outtextxy(40, 510, "Los estados pueden regresar al estado inicial si el caracter no se encuentran dentro de la función de transcisión");
}

int main(){
    int gd=DETECT, gm;
    //int gd = 700, gm = 600;
    //initgraph(&gd, &gm, (char*)"");
    initwindow(700, 550);
    dibujoAutomataPalabras();
    getch();
    closegraph();

    return 0;
}
