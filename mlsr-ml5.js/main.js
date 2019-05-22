let features = ml5.featureExtractor('MobileNet', modelReady);
features.numClasses=3;
const classifier= features.classification();



//#region features
var circles=new Array();
var squares=new Array();
var triangles=new Array();
var tests=new Array();

var testImage = new Image();
var drawnImage= document.getElementById("preview");
var readyToClassify = false;

for(i=0;i<100;i++){
    squares[i]=new Image();
    squares[i].src="mlsr_dataset/training_set/carrés/training_"+i+".png";
    classifier.addImage(squares[i],'carré');
}
for(i=0;i<100;i++){
    circles[i]=new Image();
    circles[i].src="mlsr_dataset/training_set/cercles/training_"+i+".png";
    classifier.addImage(circles[i],'cercle');
}
for(i=0;i<100;i++){
    triangles[i]=new Image();
    triangles[i].src="mlsr_dataset/training_set/triangles/training_"+i+".png";
    classifier.addImage(triangles[i],'triangle');
}

for(i=0;i<100;i++){
    tests[i]=new Image();
    tests[i].src="mlsr_dataset/testing_set/test_"+i+".png";
}
testImage=tests[0];
console.log('Feeding done.');
//#endregion

//#region chart
function chartSetup(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data:[2,1,.33,.25,.12],
    });
}
//#endregion

function modelReady(){
    console.log('Mobilenet properly loaded !');
    
}

function trainModel(){
    console.log('Now training...');
    document.getElementById("train_button").disabled=true;
    classifier.train(whileTraining);

}

function classify(){
    if(readyToClassify)classifier.classify(testImage, gotResults);
}

function changeImage(){
    var index = Math.floor(Math.random()*100);
    testImage=tests[index];
    document.getElementById('preview').src=tests[index].src;
}

function whileTraining(loss) {
    if (loss == null) {
        console.log('Training Complete !');
        classifier.classify(testImage, gotResults);
        document.getElementById("change_image_button").disabled=false;
        readyToClassify=true;
    } else {
        console.log(loss);
        document.getElementById("change_image_button").disabled=true;
    }
}

function gotResults(err, result) {
    if (err) {
      console.error(err);
    }
    console.log(result);
    document.getElementById('result').innerText=result;
}