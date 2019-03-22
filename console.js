/*Code .js de la console du projet*/

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
        AddConsoleLine('>> Entrainement');
    }else{
        AddConsoleLine('Le programme est actuellement en cours...','green');
    }
}

function Launch(){
    if(!isRunning){
      isRunning=true;
      AddConsoleLine('>> Lancement');
    }else{
      AddConsoleLine('Le programme est actuellement en cours...','green');
    }
}

//Nettoyage de la console
function ClearConsole(){
    document.getElementById('visual_console').innerHTML="";
}

//Quitte la tâche en cours
function KillTask(){
  if(isRunning){
    isRunning=false;
    AddConsoleLine('>> Le programme a été forcé à quitter','red');
  }else{
    AddConsoleLine('Aucun programme n\'a été lancé','yellow');
  }
}

//Ajoute une nouvelle ligne de texte à la console
function AddConsoleLine(message, color){
	if(color==null)color='white';//Si la couleur n'a pas été renseigné
  var console=document.getElementById('visual_console');
  console.innerHTML+="<p style='color:" + color + ";'>" + message + "</p>";
  console.scrollTop = console.scrollHeight - console.clientHeight;
}
