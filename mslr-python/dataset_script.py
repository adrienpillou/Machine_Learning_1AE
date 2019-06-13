#https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle as pck

DATASETDIR="./dataset/trainingset"
CATEGORIES=["carres","cercles","triangles"]#0-Carré/ 1-Cercle/ 2-Triangle
IMG_SIZE=32
training_data=[]

def create_training_data():
        for category in CATEGORIES:
                path=os.path.join(DATASETDIR,category)
                class_num = CATEGORIES.index(category)
                for img in os.listdir(path):
                        try:
                                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                                img_array=(255-img_array)
                                new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                                training_data.append([new_array,class_num])
                        except Exception as e:
                                pass

create_training_data()#Création des données d'entrainement

#print(len(training_data))#dimension de la dataset training
'''
random.shuffle(training_data)
for sample in training_data[:12]:
        print(sample[1])'''
        
X=[]#Features
Y=[]#Labels

#Attribution des features et des labels : 
for features,label in training_data:
        X.append(features)
        Y.append(label)

'''
for i in range(12):        
        plt.subplot(2,6,i+1)        
        plt.imshow(X[i],cmap='gray')
        plt.axis('off')
plt.show()'''

#Matrice 32x32 en Matrice 1x1024
X=np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE)

#Sauvegarde des features et labels de la dataset : 
pickle_out=open("X.pickle","wb")
pck.dump(X,pickle_out)
pickle_out.close()

pickle_out=open("Y.pickle","wb")
pck.dump(Y,pickle_out)
pickle_out.close()








                
