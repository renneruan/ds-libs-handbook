# %% Follow the cells in order to correct execution
# Reading dataset from dataset_3, dropping the id column
# Mapping bolean columns to replace with 0 or 1
import pandas as pd

df = pd.read_csv("../datasets/dataset_3.csv")
df.drop("id_cliente", inplace=True, axis=1)
map_yes_no = {"nao": 0, "sim": 1}

columns_with_yes = [
    "idoso",
    "casado",
    "dependentes",
    "servico_de_telefone",
    "varias_linhas",
    "seguranca_online",
    "backup_online",
    "protecao_de_dispositivo",
    "suporte_tecnico",
    "tv",
    "streaming_de_filmes",
    "fatura_sem_papel",
    "cancelou",
]

df[columns_with_yes] = df[columns_with_yes].replace(map_yes_no).astype(int)

# %% Proceeding using DataFrame df
# Label encoder to replace text values automatically
from sklearn.preprocessing import LabelEncoder

columns_with_object = df.select_dtypes(include=["object"]).columns.tolist()
le = LabelEncoder()
for coluna in columns_with_object:
    df[coluna] = le.fit_transform(df[coluna])

# %% Splitting the data for test
# X will recieve data without target column
from sklearn.model_selection import train_test_split

X = df.drop("cancelou", axis=1)
y = df[["cancelou"]]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# %% Normalization scaler
# Normalization should be done after the data split
# using only the data from the training set
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# %% Using Naive Bayes model for a predict example
from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)

# %% Example of metrics after the prediction results
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    mean_absolute_error,
)

conf_matrix = confusion_matrix(y_test, y_pred)
accuracy_sc = accuracy_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(classification_report(y_test, y_pred))
print(accuracy_sc)
print(mae)

# %%
