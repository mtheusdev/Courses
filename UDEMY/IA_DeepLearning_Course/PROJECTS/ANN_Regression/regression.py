import numpy as np
from sklearn.metrics import mean_squared_error
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split


print(tf.__version__)

dataset = pd.read_excel('Data.xlsx')

print(dataset)

x = dataset.iloc[:, : -1].values
print(x)
y = dataset.iloc[:, -1].values
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

ann = tf.keras.models.Sequential()

#Hidden layers
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

#Output layer
ann.add(tf.keras.layers.Dense(units=1))

#Compiling ann
ann.compile(optimizer='adam', loss='mean_squared_error')

#Training ann
ann.fit(x_train, y_train, batch_size=32,epochs=50)

#Predict 

y_pred = ann.predict(x_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
