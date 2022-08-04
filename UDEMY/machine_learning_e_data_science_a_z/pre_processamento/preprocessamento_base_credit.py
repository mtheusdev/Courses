# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# %%
base_credit = pd.read_csv('../bases/credit_data.csv')

print(base_credit.head(10))
print(base_credit.describe())
print(base_credit[base_credit['loan'] <= 1.377630])
print(base_credit[base_credit['income'] >= 69995.685578])
print(np.unique(base_credit['default'], return_counts=True))

# %% [markdown]
# Plotando graficos

# %%
sns.countplot(x = base_credit['default'])
plt.show()

plt.hist(x = base_credit['age'])
plt.show()

plt.hist(x = base_credit['income'])
plt.show()

plt.hist(x = base_credit['loan'])
plt.show()

grafico = px.scatter_matrix(base_credit, dimensions=['age','income', 'loan'], color='default')
grafico.show()

# %% [markdown]
# Processo de localização e atualização de valores inconsistentes

# %%
base_credit.loc[base_credit['age'] < 0]

# %%
base_credit[base_credit['age'] < 0]

# %%
#Apagar a coluna inteira pois só existem 3
base_credit2 = base_credit.drop('age', axis = 1)
base_credit2

# %%
#Apagar só os registros com valores inconcistentes
base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
base_credit3

# %%
base_credit3.loc[base_credit3['age'] < 0]

# %%
#Preencer os valores inconcistentes manualmente

# %%
#Preencher os valores faltantes com a média
print(base_credit.mean())
base_credit['age'].mean()

# %%
base_credit['age'][base_credit['age'] > 0].mean()

# %%
base_credit.loc[base_credit['age'] < 0, 'age'] = base_credit['age'][base_credit['age'] > 0].mean()

# %%
base_credit.loc[base_credit['age'] < 0]

# %%
base_credit.head(27)

# %%
sns.countplot(x = base_credit['default'])
plt.show()

plt.hist(x = base_credit['age'])
plt.show()

plt.hist(x = base_credit['income'])
plt.show()

plt.hist(x = base_credit['loan'])
plt.show()

grafico = px.scatter_matrix(base_credit, dimensions=['age','income', 'loan'], color='default')
grafico.show()

# %% [markdown]
# Removendo valores faltantes

# %%

base_credit.isnull()

# %%
base_credit.isnull().sum()

# %%
base_credit.loc[pd.isnull(base_credit['age'])]

# %%
base_credit['age'].fillna(base_credit['age'].mean(), inplace=True)

# %%
base_credit.loc[pd.isnull(base_credit['age'])]

# %%
base_credit.loc[base_credit['clientid'] == 29 ] 

# %%
base_credit.loc[base_credit['clientid'].isin([29,31,32])]

# %% [markdown]
# Divisão entre previsores e classe

# %%
X_credit = base_credit.iloc[:, 1:4].values

# %%
X_credit

# %%
type(X_credit)

# %%
Y_credit = base_credit.iloc[:, 4].values

# %%
Y_credit

# %%
type(Y_credit)

# %%
X_credit[:, 0]

# %%
X_credit[:, 0].min(), X_credit[:, 1].min(), X_credit[:, 2].min()

# %%
X_credit[:, 0].max(), X_credit[:, 1].max(), X_credit[:, 2].max()

# %% [markdown]
# Escalonamento dos dados (Padronização dos dados)

# %%
from sklearn.preprocessing import StandardScaler
scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)

# %%
X_credit[:, 0].min(), X_credit[:, 1].min(), X_credit[:, 2].min()

# %%
X_credit[:, 0].max(), X_credit[:, 1].max(), X_credit[:, 2].max()

# %%
X_credit


