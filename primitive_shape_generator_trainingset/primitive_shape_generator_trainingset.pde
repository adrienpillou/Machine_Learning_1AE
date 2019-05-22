/*Ce programme permet de génerer des images 
de formes primitives de manière aléatoire.*/

//References P3 : https://processing.org/reference

/*Palette : */
color[] colorArray={#1ABC9C, #2ECC71,
                    #3498DB, #8E44AD,
                    #F1C40F, #D35400, 
                    #C0392B};
/*---------------------------------------------*/

String categories[] = {"cercle", "carré", "triangle"}; 

/*Variables globales : */
color currentColor;
String currentShape;
String savePath="./Snapshots/";
int index;
int imageToGenerate = 100;
int shapeCode=2;
/*-----------------------------*/

void setup(){
  noStroke();
  size(32,32);//Taille de l'image générée (canvas)
  background(255);
}

void draw(){
  clear();
  background(255);
  if(index<imageToGenerate){
    PVector pivot = new PVector(width/2,width/2);//Modification del'origine du repère
    translate(pivot.x,pivot.y);
    rectMode(CENTER);
    rotate(random(-.99,.99));
    int colorCode=(int)random(0,colorArray.length);
    fill(colorArray[colorCode]);
    int r,x1,x2,x3,y1,y2,y3;//Variables nécessaires au dessin
    PVector offset = new PVector(random(-1,1), random(-1,1));
    offset.x*=width*.1;
    offset.y*=width*.1;
    
    switch(shapeCode){//Selectionne le type de forme géometrique
      case 0:
      currentShape="Circle";
      r = (int)random(width*.1,width*.75);
      ellipse(offset.x, offset.y, r, r);
      break;
      
      case 1:
      currentShape="Square";
      int rectWidth=(int)random(width*.1,width*.5);
      rect(offset.x, offset.y, rectWidth, rectWidth);
      break;
      
      case 2:
      currentShape="Triangle";
      int sideLength=(int)random(width*.1,width*.5);
      x1 = (int)(cos(radians(0))*sideLength);
      x2 = (int)(cos(radians(120))*sideLength);
      x3 = (int)(cos(radians(240))*sideLength);
      y1 = (int)(sin(radians(0))*sideLength);
      y2 = (int)(sin(radians(120))*sideLength);
      y3 = (int)(sin(radians(240))*sideLength);
      triangle(x1+offset.x, y1+offset.y, x2+offset.x, y2+offset.y, x3+offset.x, y3+offset.y);
      break;
    }
    println(imageToGenerate-index+" images restantes.");
    saveFrame(savePath +"/"+ categories[shapeCode] +"/training_"+index+".png");//Enregistrement de l'image
    index++;
  }else{
    println("Terminé.\n"+imageToGenerate+" images sauvegardées dans "+savePath);
    exit();
  }
  delay(15);//Ajout d'un délai pour la visibilité (ms)
}
