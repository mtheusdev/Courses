# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# %%
base_census = pd.read_csv('../bases/census.csv')

# %%
base_census

# %%
base_census.describe()

# %%
base_census.isnull().sum()

# %%
np.unique(base_census['income'], return_counts=True)

# %%
sns.countplot(x = base_census['income'])

# %%
plt.hist(x = base_census['age'])

# %%
plt.hist(x = base_census['education-num'])

# %%
plt.hist(x = base_census['hour-per-week'])

# %%
grafico = px.treemap(base_census, path=['workclass', 'age'])
grafico.show()

# %%
grafico = px.treemap(base_census, path=['occupation', 'relationship', 'age'])
grafico.show()

# %%
grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'] )
grafico.show()

# %%
grafico = px.parallel_categories(base_census, dimensions=['workclass', 'occupation', 'income'] )
grafico.show()

# %%
grafico = px.parallel_categories(base_census, dimensions=['income', 'occupation'] )
grafico.show()

# %%
grafico = px.parallel_categories(base_census, dimensions=['income', 'education'] )
grafico.show()

# %% [markdown]
# Divisão de previsores e classe

# %%
X_census = base_census.iloc[:, 0:14].values

# %%
X_census

# %%
X_census[0]

# %%
Y_census = base_census.iloc[:, 14].values

# %%
Y_census

# %% [markdown]
# Tratamento de dados categóricos (Transformar de string para numero)

# %% [markdown]
# Label encoder

# %%
from sklearn.preprocessing import LabelEncoder

# %%
X_census[:, 1]

# %%
label_encoder_teste = LabelEncoder()
teste = label_encoder_teste.fit_transform(X_census[:,1])

# %%
teste

# %%
label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

# %%
X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])
X_census[:,3] = label_encoder_education.fit_transform(X_census[:,3])
X_census[:,5] = label_encoder_marital.fit_transform(X_census[:,5])
X_census[:,6] = label_encoder_occupation.fit_transform(X_census[:,6])
X_census[:,7] = label_encoder_relationship.fit_transform(X_census[:,7])
X_census[:,8] = label_encoder_race.fit_transform(X_census[:,8])
X_census[:,9] = label_encoder_sex.fit_transform(X_census[:,9])
X_census[:,13] = label_encoder_country.fit_transform(X_census[:,13])


# %%
X_census[0]

# %%
X_census

# %% [markdown]
# OneHotEconder

# %%
len(np.unique(base_census['workclass']))

# %%
len(np.unique(base_census['occupation']))

# %%
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# %%
onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder='passthrough')

# %%
X_census = onehotencoder_census.fit_transform(X_census).toarray()

# %%
X_census

# %%
X_census[0]

# %%
X_census.shape

# %% [markdown]
# Escalonando os dados

# %%
from sklearn.preprocessing import StandardScaler
scaler_census = StandardScaler()
X_census = scaler_census.fit_transform(X_census)
X_census[0]

# %% [markdown]
# Divisão de bases de treinamento e teste

# %%
from sklearn.model_selection import train_test_split

# %%
X_census_treinamento, X_census_teste, Y_census_treinamento, Y_census_teste = train_test_split(X_census, Y_census, test_size=0.15, random_state=0)

# %%
X_census_treinamento.shape, Y_census_treinamento.shape

# %%
X_census_teste.shape, Y_census_teste.shape

# %%
import pickle

# %%
with open('census.pkl', mode="wb") as f:
    pickle.dump([X_census_treinamento, Y_census_treinamento, X_census_teste, Y_census_teste], f)


