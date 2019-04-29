import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random

MODEL_NAME='mlsr_model-512-nodes_30-epochs.model'
CATEGORIES=["cercle", "carré", "triangle"]#0-Cercle/ 1-Carre/ 2-Triangle
TESTSET_DIM=999
IMG_SIZE=32

def prepare(filepath, index):
        img_array=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)#Ouverture de l'image
        img_array=255.0-img_array#Inversion noir et blanc
        new_array=cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))#Modification de la taille de l'image
        plt.subplot(3,4,index+1)
        plt.imshow(new_array, cmap='gray')
        plt.axis('off')
        return new_array.reshape(-1,IMG_SIZE,IMG_SIZE)#Retourne une matrice représentant l'image

model=tf.keras.models.load_model('./models/'+MODEL_NAME)#Chargement du model 

for i in range(12):
        prediction=model.predict([prepare('./testset/test_'+str(random.randint(0,TESTSET_DIM))+'.png',i)])#Prédiction d'une image grâce au model
        prediction_index=np.argmax(prediction)#Sélection de la plus grande valeur du vecteur de prédiction
        output=CATEGORIES[prediction_index]#Conversion de l'index en chaine de caractère
        plt.title(str(i+1)+' : '+output)#Titre de l'image
        print ("L' image n° "+str(i+1)+" est probablement un "+output+'.')

plt.show()#Affichage du plot

