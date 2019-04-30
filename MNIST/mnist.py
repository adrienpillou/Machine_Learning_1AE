''' 
Ce programme permet de créer et sauvegarder un model tf-keras
dédié à MNIST.

32 nodes @ 1 epochs : 85% acc
128 nodes @ 3 epochs : 95% acc
'''

import tensorflow as tf #Librairie TensorFlow
import matplotlib.pyplot as pyplot  #Librairie affichage graphique

mnist = tf.keras.datasets.mnist #Dataset MNIST
nodes=128 #Nombre de noeuds constituant la couche dense
epochs_number=3

#Chargement de la dataset : 
(x_train, y_train),(x_test, y_test) = mnist.load_data() #Parsing de la dataset et répartition features/labels
x_train, x_test = x_train / 255.0, x_test / 255.0 # Conversion gris(0-255)->gris(0-1)

#Structure du model cnn : 
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)), #Conversion Matrice(28x28)/Vecteur(1x784)
  tf.keras.layers.Dense(nodes, activation='relu'), #Couche de traitement dense
  tf.keras.layers.Dropout(0.2), #???
  tf.keras.layers.Dense(10, activation='softmax') #Couche de sortie constitué de 10 neuronnes
])
#Compilation, entrainement et évaluation : 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']) #Compilation du model et réglages pour l'utilisation

model.fit(x_train, y_train, epochs=epochs_number) #Entrainement du model
model.evaluate(x_test, y_test) #Evaluation du model sur des images inconnues
model.save('./models/mnist_model.model') #Sauvegarde du model dans le répertoire 'models'



