import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

NAME="mlsr_model-{}".format(int(time.time()))
iterations=50#Nombre d' 'epochs'
nodes=512

pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open("Y.pickle","rb")
Y=pickle.load(pickle_in)

X=X/255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(32, 32)),
  tf.keras.layers.Dense(nodes, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(3, activation='softmax')
])

board=TensorBoard(log_dir='logs/{}'.format(NAME))#http://localhost:6006
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X, Y, epochs=iterations,callbacks=[board])
model.save('./models/'+NAME+'.model')












