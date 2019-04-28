import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random

MODEL_NAME='mlsr_model_1024-nodes_50-epochs.model'
CATEGORIES=["cercle", "carré", "triangle"]#0-Cercle/ 1-Carre/ 2-Triangle
TESTSET_DIM=999
IMG_SIZE=32

def prepare(filepath, index):
        img_array=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        img_array=255.0-img_array
        new_array=cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        plt.subplot(3,4,index+1)
        plt.imshow(new_array, cmap='gray')
        plt.axis('off')
        return new_array.reshape(-1,IMG_SIZE,IMG_SIZE)

model=tf.keras.models.load_model('./models/'+MODEL_NAME)

for i in range(12):
        prediction=model.predict([prepare('./testset/test_'+str(random.randint(0,TESTSET_DIM))+'.png',i)])
        prediction_index=np.argmax(prediction)
        output=CATEGORIES[prediction_index]
        plt.title(str(i+1)+' : '+output)
        print ("L' image n° "+str(i+1)+" est probablement un "+output+'.')

plt.show()

