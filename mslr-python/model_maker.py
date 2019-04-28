import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
#TensorBoardhttp://localhost:6006
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

NAME="mlsr_model-{}".format(int(time.time()))
iterations=100#Nombre d' 'epochs'

conv_layers=3
nodes=64
dense_layers=0

pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open("Y.pickle","rb")
Y=pickle.load(pickle_in)

X=X/255.0

#Structure du réseau cnn : 
model=Sequential()
board=TensorBoard(log_dir='logs/{}'.format(NAME))

#Couche noeuds :
for i in range(conv_layers):
        print('convolutional layer added !')
        model.add(Conv2D(nodes, (3, 3), input_shape=X.shape[1:]))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
#Couche densification :
for n in range(dense_layers):
        print('densification layer added !')
        model.add(Dense(nodes))
        model.add(Activation('relu'))

#Sortie :
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",optimizer="adam",metrics=['accuracy'])
model.fit(X, Y, batch_size=32, epochs=iterations, validation_split=.3, callbacks=[board])
model.save('./models/'+NAME+'.model')








