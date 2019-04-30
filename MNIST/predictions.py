import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random

mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()

model=tf.keras.models.load_model('./models/mnist_model.model')

for i in range(9):
    random_index=random.randint(0,len(x_test))
    random_image=x_test[random_index]
    img_array=random_image.reshape(-1,28,28)
    prediction=model.predict(img_array)
    output=np.argmax(prediction[0])
    answer=y_test[random_index]
    plt.subplot(3,3,i+1)
    plt.axis("off")
    if output==answer:
        plt.title('Correct',color='g')
    else:
        plt.title('Error : '+str(output),color='r')
    plt.imshow(random_image,cmap='gray_r')
plt.show()