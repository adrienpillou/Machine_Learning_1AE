import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import random

MODEL_NAME='mlsr_model-1556441977.model'
CATEGORIES=["Circle", "Square", "Triangle"]
TESTSET_DIM=999
IMG_SIZE=32


def prepare(filepath, index):
        img_array=cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
        new_array=255-new_array
        plt.subplot(2,6,index+1)
        plt.imshow(new_array,cmap='gray')
        plt.axis('off')
        return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,1)

model=tf.keras.models.load_model('./models/'+MODEL_NAME)


for i in range(12):
        prediction=model.predict([prepare('./testset/test_'+str(random.randint(0,TESTSET_DIM))+'.png',i)])
        #print(prediction)
        output=CATEGORIES[int(prediction[0][0])]
        print ('Image n° '+str(i+1)+' is probably a '+output+'.')

plt.show()
quit()

