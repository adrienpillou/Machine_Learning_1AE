import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random
import csv

MODEL_NAME='mlsr_model-8_nodes-3_epochs-60acc.model'
CATEGORIES=["cercle", "carré", "triangle"]#0-Cercle/ 1-Carre/ 2-Triangle
TESTSET_DIM=999
IMG_SIZE=32

#Prépare l'image à rentrer dans le cnn :
def prepare(filepath, index):
        img_array=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)#Ouverture de l'image
        img_array=255.0-img_array#Inversion noir et blanc
        new_array=cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))#Modification de la taille de l'image
        plt.subplot(3,4,index+1)
        plt.imshow(new_array, cmap='gray')
        plt.axis('off')
        return new_array.reshape(-1,IMG_SIZE,IMG_SIZE)#Retourne une matrice représentant l'image


#Renvoie la réponse à la prédicition :
def get_answer(image_index):
        with open('./testset/testset_data.csv','r') as file:#Ouverture du csv en mode lecture
                mycsv=csv.reader(file,delimiter=',')
                table=list(mycsv)
                cell_value=table[image_index+1][1]
                category_index=int(cell_value,10)-1#Conversion de la valeur de la cellule en nombre entier
                return CATEGORIES[category_index]#Valeur de la réponse 
        
model=tf.keras.models.load_model('./models/'+MODEL_NAME)#Chargement du model 

#Prédictions de 12 images tirées au sort dans la testset :
for i in range(12):
        random_image=random.randint(0,TESTSET_DIM)
        prediction=model.predict([prepare('./testset/test_'+str(random_image)+'.png',i)])#Prédiction d'une image grâce au model
        prediction_index=np.argmax(prediction)#Sélection de la plus grande valeur du vecteur de prédiction
        output=CATEGORIES[prediction_index]#Conversion de l'index en chaine de caractère
        answer=get_answer(random_image)
        #Vérification de la prédiction : 
        if answer==output:
                plt.title(str(random_image)+' : '+output)#Titre de l'image
        else:
                plt.title("Erreur",color='r')#Titre de l'image
plt.show()#Affichage

