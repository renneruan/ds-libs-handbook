# Handbook with multiple pandas commands
# Simple usage only to consult syntax of multiple functions
#
# With this cell structure only the last command will show as result

# %%
import pandas as pd

df = pd.read_csv("../datasets/dataset_1.csv")
# df.to_csv('name')

# %% Create dataframe and series with specific labels
example_df = pd.DataFrame(
    {"Bob": [1, "I liked it.", "It was awful."], "Sue": [2, "Pretty good.", "Bland."]},
    index=["Test", "Product A", "Product B"],
)

pd.Series(
    [30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product A"
)
pd.set_option("display.max_rows", 5)

example_df.set_index("Bob")  # Create as column

# %% Retrieve elements on the beginning or ending of dataset
df.head().T
df.tail()
df.head()

# %% Functions to retrieve DataFrame structure and size
# Like number of cells, columns, types and overall shape
df.shape
len(df)
df.size
df.dtypes

df.columns
df.columns.tolist()

# %% Summarize information of DataFrame, very useful for start insight
df.info()
df.describe()
df.describe(include="O")

# %% Check for null information
# It's important to check the percentage of null information and how this impact our goal
df.isnull()
df.isnull().sum()
df.isnull().mean()  # Mean of booleans equals the percentage
df.isna()
df.isna().sum() * 100 / len(df)
round(df.isna().sum() * 100 / len(df), 2)

# %% Commands for summarize values information
df.idade.nunique()
df.idade.unique()
df.idade.value_counts()
df.idade.quantile(0.75)

# %% Data access commands
# iloc and loc are the core to access and manipulate our information
df.index
df.iloc[0]  # Supports index like lists 0:10, -1 and list of indexes
df.iloc[0, 0:2]  # Retrieve row and columns

df.loc[0]  # Work with index, while iloc with position
df.loc[df["idade"] == 37]
df.loc[(df["estado_civil"] == "divorced") & (df["idade"] < 27)]

# %% Example of how change values with loc
# Dropping information with null cells
# General value change loc syntax df.loc[condition, target] = value

df.loc[df["duracao"].isnull(), "duracao"] = round(df["duracao"].mean())
df.drop(
    df.loc[df["idade"].isnull()].index, inplace=False
)  # Inplace false to prevent change the DataFrame

map_yes_no = {"no": 0, "yes": 1}
cols = ["possui_casa", "emprestimo"]
df[cols] = df[cols].fillna("no")
df[cols] = df[cols].replace(map_yes_no)
df[cols] = df[cols].astype(int)

df.drop_duplicates(subset="possui_casa", keep="first")
# df[cols].fillna(method='bfill', axis=0).fillna(0)

# %% Statistic functions to use on columns/series
df.duracao.median()
df.duracao.mode()
df.duracao.mean()
df.duracao.max()
df.duracao.min()

# %% Conversion functions used after data treatment
df.emprestimo = pd.to_numeric(df.emprestimo)

# %%
