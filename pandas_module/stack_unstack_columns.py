# %%
import pandas as pd

data = [
    {
        "ano": 2000,
        "abrigo": "a",
        "cachorros-castrados": 0,
        "cachorros-adotado": 10,
        "cachorros-salvos": 15,
    },
    {
        "ano": 2010,
        "abrigo": "b",
        "cachorros-castrados": 3,
        "cachorros-adotado": 15,
        "cachorros-salvos": 5,
    },
    {
        "ano": 2015,
        "abrigo": "c",
        "cachorros-castrados": 2,
        "cachorros-adotado": 5,
        "cachorros-salvos": 31,
    },
]

df = pd.DataFrame(data)
df.head()
# %%
index_cols = ["ano", "abrigo"]
df = df.set_index(index_cols)
df = df.stack().reset_index().rename(columns={"level_2": "status", 0: "qt"})

df.head()

# %%
# df.columns = ["ano", "abrigo", "status"]
df = df.set_index(["ano", "abrigo", "status"]).unstack().reset_index()

status_list = df["qt"].columns.tolist()
status_list
# %%
columns_list = df.columns.droplevel(1).tolist()[
    :2
]  # Value will change according of columns size
df.columns = columns_list + status_list
df
# %%
