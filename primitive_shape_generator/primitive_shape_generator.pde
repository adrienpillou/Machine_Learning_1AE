/*Ce programme permet de génerer des images 
de formes primitives de manière aléatoire.*/

//References P3 : https://processing.org/reference

/*Palette :*/
color vert = color(60,174,163);
color jaune = color(246,213,92);
color rouge = color(237,85,59);
color bleu = color(32,99,155);
/*------------------------------*/

color currentColor;
String currentShape;
String savePath="./Snapshots/";
int index;
int imageToGenerate = 10;
color[] colorArray={vert,jaune,rouge,bleu};

void setup(){
 noStroke();
 size(64,64);//Taille de l'image générée
 background(255);
}

void draw(){
  clear();
  background(255);
  if(index<imageToGenerate){
    PVector pivot = new PVector(width/2,width/2);/*!!!*/
    translate(pivot.x,pivot.y);
    rectMode(CENTER);
    rotate(random(-.99,.99));
    int colorCode=(int)random(0,colorArray.length);
    int shapeCode=(int)random(1,4);
    fill(colorArray[colorCode]);
    int r,x1,x2,x3,y1,y2,y3;//Variables nécessaire au dessin
    
    switch(shapeCode){//Selectionne le type de forme géometrique
      case 1:
      currentShape="cercle";
      r = (int)random(width*.1,width*.75);
      ellipse(0,0,r,r);
      break;
      
      case 2:
      currentShape="carre";
      int rectWidth=(int)random(width*.1,width*.33);
      rect(0,0,rectWidth,rectWidth);
      break;
      
      case 3:
      currentShape="triangle";
      int sideLength=(int)random(width*.1,width*.5);
      x1 = (int)(cos(radians(0))*sideLength);
      x2 = (int)(cos(radians(120))*sideLength);
      x3 = (int)(cos(radians(240))*sideLength);
      y1 = (int)(sin(radians(0))*sideLength);
      y2 = (int)(sin(radians(120))*sideLength);
      y3 = (int)(sin(radians(240))*sideLength);
      triangle(x1, y1, x2, y2, x3, y3);
      break;
    }
    println(currentShape, index);//Affichage console
    saveFrame(savePath + currentShape+"_"+index+".png");//Enregistrement de l'image
    index++;
  }else{
    exit();
  }
  delay(100);
}
