import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
#TensorBoard => http://localhost:6006
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

iterations=15#Nombre d' 'epochs'

dense_layers=[0,1,2]
layer_sizes=[32,64,128]
conv_layers=[1,2,3]

'''default
dense_layers=[0,1,2]
layer_sizes=[32,64,128]
conv_layers=[1,2,3]'''

pickle_in=open("X.pickle","rb")
X=pickle.load(pickle_in)

pickle_in=open("Y.pickle","rb")
Y=pickle.load(pickle_in)

X=(255-X)/255

for dense_layer in dense_layers:
        for layer_size in layer_sizes:
                for conv_layer in conv_layers:
                        NAME="{}_conv-{}_nodes-{}_dense-{}".format(conv_layer,layer_size,dense_layer,int(time.time()))
                        board=TensorBoard(log_dir='logs/{}'.format(NAME))
                        model=Sequential()
                        
                        #Couche 1 :
                        model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
                        model.add(Activation('relu'))
                        model.add(MaxPooling2D(pool_size=(2,2)))

                        for i in range(conv_layer-1):
                                #Couche i-1 :
                                model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
                                model.add(Activation('relu'))
                                model.add(MaxPooling2D(pool_size=(2,2)))        

                        model.add(Flatten())
                        for i in range(dense_layer):
                                #Couche dense :
                                model.add(Dense(layer_size))
                                model.add(Activation('relu'))

                        #Sortie :
                        model.add(Dense(1))
                        model.add(Activation('sigmoid'))

                        model.compile(loss="binary_crossentropy",optimizer="adam",metrics=['accuracy'])
                        model.fit(X, Y, batch_size=32, epochs=iterations, validation_split=.3,callbacks=[board])
                        model.save('./models/'+NAME+'.model')
                        














