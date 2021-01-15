import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout,LSTM,TimeDistributed,Conv1D,MaxPooling1D
from tensorflow.keras.optimizers import Adam

def LSTM_input(X,y):
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0,stratify=y)
    X_train=X_train.reshape(1584,80,3)
    X_test=X_test.reshape(396,80,3)
    return X_train,X_test,y_train,y_test

def model(X_train,X_test,y_train,y_test,epochs_num):
	model = Sequential()
	model.add(LSTM(100, input_shape=(80,3)))
	model.add(Dropout(0.5))
	model.add(Dense(100, activation='relu'))
	model.add(Dense(6, activation='softmax'))
	model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.003), metrics=['accuracy'])
	# fit network
	history=model.fit(X_train, y_train,epochs=epochs_num,validation_data=(X_test,y_test),verbose=1,batch_size=64)
	return history,model