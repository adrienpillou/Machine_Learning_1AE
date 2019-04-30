''' 
Ce programme effectue 9 prédiction MNIST à partir 
du model tf-keras dans situé dans le répertoire 'models'.
'''

import tensorflow as tf
import matplotlib.pyplot as plt
import cv2 #Gestion des images 
import numpy as np #Gestion des arrays
import random #Géneration de nombre aléatoires

#Chargement de la dataset MNIST :
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()

#Chargement du model :
model=tf.keras.models.load_model('./models/mnist_model.model')

#Affichage de quelques prédictions : 
for i in range(9):
    random_index=random.randint(0,len(x_test))
    random_image=x_test[random_index] #Choix d'une image parmis le testset
    img_array=random_image.reshape(-1,28,28) #mise en forme de l'image
    prediction=model.predict(img_array) #Prédiction à partir du model chargé
    output=np.argmax(prediction[0]) #Mise en forme de la prédiction
    answer=y_test[random_index] #Récupération de la réponse dans l'array des labels
    plt.subplot(3,3,i+1) #Split des affichages
    plt.axis("off") #Désactivation des axes
    if output==answer: #Vérification de la prédiction
        plt.title('Correct',color='g') #Prédiction correcte -> texte vert
    else:
        plt.title('Error : '+str(output),color='r') #Prédiction incorrecte -> texte rouge et affichage de la réponse
    plt.imshow(random_image,cmap='gray_r') #Affichage de l'image sélectionnée
plt.show()#Affichage Matplot