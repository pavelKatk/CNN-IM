import numpy as np 
from keras.utils import plot_model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras.models import model_from_json

def model(train_data, train_result, test_data):
	model = Sequential()
	model.add(Conv1D(filters=15, kernel_size=3,activation='relu',input_shape=(600 , 3)))
	model.add(MaxPooling1D(pool_size = 2))
	model.add(Dropout(0.2))
	model.add(Conv1D(filters=10, kernel_size=3,activation='relu'))
	model.add(MaxPooling1D(pool_size = 2))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(25, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
	model.fit(np.array(train_data), np.array(train_result), epochs = 45, batch_size = 8, verbose=1)
	pred = model.predict(np.array(np.array(test_data[:]).reshape(1,600,3)),verbose = 0)
	print(pred)
	return pred