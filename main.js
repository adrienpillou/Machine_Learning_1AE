/*Code .js du Projet*/

/*
CODE COULEUR :
Rouge => information importante
Jaune => information
Vert => information constat
*/

var isRunning=false;

function Training(){
      if(!isRunning){
        isRunning=true;
        document.getElementById('visual_console').innerHTML+="<p>>> Entrainement</p>";
      }else{
        document.getElementById('visual_console').innerHTML+="<p style='color:green;'>Le programme est actuellement en cours...</p>";
      }
}

function Launch(){
    if(!isRunning){
      isRunning=true;
      document.getElementById('visual_console').innerHTML+="<p>>> Lancement</p>";
    }else{
      document.getElementById('visual_console').innerHTML+="<p style='color:green;'>Le programme est actuellement en cours...</p>";
    }
}

//Nettoie la console
function ClearConsole(){
    document.getElementById('visual_console').innerHTML="";
}

//Quitte la tâche en cours
function KillTask(){
  if(isRunning){
    isRunning=false;
    document.getElementById('visual_console').innerHTML+="<p style='color:red;'>>> Le programme a été forcé à quitter</p>";
  }else{
    document.getElementById('visual_console').innerHTML+="<p style='color:yellow;'>>> Aucun programme n'a été lancé</p>";
  }
}

//Ajoute une nouvelle ligne de texte à la console
function AddConsoleLine(message, color){
  if(color==null)color='white';//Si la couleur n'a pas été renseigné
  document.getElementById('visual_console').innerHTML+="<p style='color:" + color + ";'>" + message + "</p>";
}
