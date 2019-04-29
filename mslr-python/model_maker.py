import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time


iterations=10#Nombre d' 'epochs'
nodes=128
NAME="mlsr_model-{}_nodes-{}_epochs-{}".format(nodes, iterations, int(time.time()))

#Chargement de la dataset d'entrainement
pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)
pickle_in=open("Y.pickle","rb")
Y=pickle.load(pickle_in)

X=X/255.0#Conversion gris(0-255) en gris(0-1)

#Structure du réseau de neurones : 
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(32, 32)),
  tf.keras.layers.Dense(nodes, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(3, activation='softmax')
])

board=TensorBoard(log_dir='logs/{}'.format(NAME))#Tensorboard->http://localhost:6006
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])#Compilation
model.fit(X, Y, epochs=iterations,callbacks=[board])#Session d'entrainement
model.save('./models/'+NAME+'.model')#Sauvegarde du model 












