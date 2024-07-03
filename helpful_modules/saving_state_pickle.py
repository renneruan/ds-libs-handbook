# %%
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("../datasets/dados_bancarios.csv")

# %% Save label encoder with pickle
col_name = "emprego"
le = LabelEncoder()
df[col_name] = le.fit_transform(df.emprego)
le.classes_
with open(f"{col_name}.pkl", "wb") as file:
    # Usando a função dump do pickle, serializamos e gravamos o objeto "le" no arquivo.
    pickle.dump(le, file)
# %%
