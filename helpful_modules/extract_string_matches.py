# %% Need to run pip install fuzzywuzzy
# Module for extract matches of given string on series
import fuzzywuzzy
from fuzzywuzzy import process
import pandas as pd

df_ascii = pd.read_csv("../datasets/dados_bancarios.csv")
matches = fuzzywuzzy.process.extract(
    "admin", df_ascii.emprego, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio
)
print(matches)
