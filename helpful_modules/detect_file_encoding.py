# %%
import pandas as pd

# %% Check encoding of given file
import charset_normalizer

with open("datasets/dataset_1.csv", "rb") as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

print(result)
df_ascii = pd.read_csv("datasets/dataset_1.csv", encoding="ascii")
