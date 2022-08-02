import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
le = LabelEncoder()
# print(tf.__version__)


# Reading data.csv
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values
print("Data\n", x)

#encoding gender
x[:, 2] = le.fit_transform(x[:, 2])
print("Encoding Gender\n", x)

#Endoding country
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print("Encoding Country\n", x)

#Separando conjunto de dados de treino do conjunto de teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print("Treino")
print(x_train, len(x_train))
print("Teste")
print(x_test, len(y_train))

#Feature Scaling
print("Feature Scaling")
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

print(x_train)
print(y_test)

#Building the ANN

ann = tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=6,activation='relu')) # Adicionando uma camada de neuronios
ann.add(tf.keras.layers.Dense(units=6,activation='relu')) # Adicionando mais uma

# Camada de saída (um neuronio pois a saída é binaria e função sigmoid pois queremos a porcentagem do cliente sair)
# se fosse um resultado não binario, activation seria softmax
ann.add(tf.keras.layers.Dense(units=1,activation='sigmoid')) # Adicionando mais uma

# adam = gradiante descendente estocastico
# se fosse um resultado não binario, loss seria category_crossentropy
ann.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])

#Training ann
ann.fit(x_train, y_train, batch_size = 32, epochs = 40)

# Testing
print("Predict: ")
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])))
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)


# Testando todos os valores
y_pred = ann.predict(x_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test),1)),1))

#Métricas
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
print(accuracy_score(y_test, y_pred))

