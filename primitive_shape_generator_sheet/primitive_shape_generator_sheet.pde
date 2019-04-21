/*Ce programme permet de générer des images 
de formes primitives de manière aléatoire.*/

//References P3 : https://processing.org/reference

/*Palette : */
color[] colorArray = {#1ABC9C, #2ECC71,
                      #3498DB, #8E44AD,
                      #F1C40F, #D35400, 
                      #C0392B};
/*---------------------------------------------*/

/*Variables globales : */
String savePath = "./sheets/";
final String sheetFormat=".png";
String sheetId;
color currentColor;
String currentShape;
int index;
int shapeSize = 64;//taille d'une forme (16,32,64 ou 128 px)
PVector pivot;
PVector currentPos;
JSONObject jsonObject;
JSONArray jsonArray;
/*-----------------------------*/

void setup(){
  smooth(2);//antialiasing x2
  noStroke();
  size(2560,2560);//Taille de l'image générée (canvas)
  background(255);
  pivot = new PVector(shapeSize/2,shapeSize/2);
  rectMode(CENTER);
  sheetId=str(day())+str(month())+str(year())+str(hour())+str(minute());
  CreateJSONArray();
}

void draw(){
  translate(pivot.x,pivot.y);//Modification de l'origine du repère
  rotate(random(-.99,.99));
  int colorCode=(int)random(0,colorArray.length);
  int shapeCode=(int)random(1,4);
  fill(colorArray[colorCode]);//Sélection de la couleur
  int r,x1,x2,x3,y1,y2,y3;//Variables nécessaire au dessin
    
  switch(shapeCode){//Selectionne le type de forme géometrique
      case 1:
      currentShape="cercle";
      r = (int)random(shapeSize*.1,shapeSize*.75);
      ellipse(0,0,r,r);
      break;
      
      case 2:
      currentShape="carre";
      int rectWidth=(int)random(shapeSize*.1,shapeSize*.5);
      rect(0,0,rectWidth,rectWidth);
      break;
      
      case 3:
      currentShape="triangle";
      int sideLength=(int)random(shapeSize*.1,shapeSize*.5);
      x1 = (int)(cos(radians(0))*sideLength);
      x2 = (int)(cos(radians(120))*sideLength);
      x3 = (int)(cos(radians(240))*sideLength);
      y1 = (int)(sin(radians(0))*sideLength);
      y2 = (int)(sin(radians(120))*sideLength);
      y3 = (int)(sin(radians(240))*sideLength);
      triangle(x1, y1, x2, y2, x3, y3);
      break;
    }
  //println((index+1) + " formes générées sur la feuille.");
  String currentId = currentShape+"_"+index;
  AddJSONObject(currentId,currentShape);
  index++;
  pivot.x+=shapeSize;
   if(pivot.x>=width){
     if(pivot.y<height){
       pivot.y+=shapeSize;
       pivot.x=shapeSize/2;
   }else{
       saveFrame(savePath + "generated_sheet"+sheetFormat);//Enregistrement de l'image
       println("Terminé.\n"+index+" images sauvegardées dans "+savePath);
       exit();
   }
   }
  //delay(0);//Ajout d'un délai pour la visibilité (ms)
}

//https://github.com/shiffman/LearningProcessing/tree/master/chp18_data
/*.JSON : */
void CreateJSONArray(){
  jsonArray=new JSONArray();
  saveJSONArray(jsonArray,"./data/shapesheet_"+sheetId+"_data.json");
}

void AddJSONObject(String objectId, String objectType){
  jsonObject = new JSONObject();
  jsonObject.setString("id",objectId);
  jsonObject.setString("type",objectType);
  jsonArray.append(jsonObject);
  saveJSONArray(jsonArray,"./data/shapesheet_"+sheetId+"_data.json");
}
