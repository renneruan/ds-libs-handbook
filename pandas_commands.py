# With this cell structure only the last command will show as result
# %%
import pandas as pd
df = pd.read_csv('datasets/dataset_1.csv')
# df.to_csv('name')

# %% Create dataframe and series with specific labels
example_df = pd.DataFrame({'Bob': [1,'I liked it.', 'It was awful.'], 
              'Sue': [2,'Pretty good.', 'Bland.']},
             index=['Test','Product A', 'Product B'])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
pd.set_option('display.max_rows', 5)

example_df.set_index("Bob") # Create as column

# %% Retrieve first elements
df.head().T
df.tail()
df.head()

# %% Dataframe structure and size commands
df.shape
len(df)
df.size
df.dtypes

df.columns
df.columns.tolist()

# %% Get summary information of dataframe
df.info()
df.describe()
df.describe(include='O')

# %% Verify null information
df.isnull()
df.isnull().sum()
df.isnull().mean() # mean of booleans is the percentage 
df.isna()
df.isna().sum() * 100 / len(df)
round(df.isna().sum() * 100 / len(df), 2)

# %% Commands for values informations
df.idade.nunique()
df.idade.unique()
df.idade.value_counts()

# %% Selection commands
df.index
df.iloc[0] # Supports index like lists 0:10, -1 and list of indexes
df.iloc[0, 0:2] # Retrieve row and columns

df.loc[0] # Work with index, while iloc with position
df.loc[df['idade'] == 37]
df.loc[(df['estado_civil'] == 'divorced') & (df['idade'] < 27)]

# %% Changing values and drop information
# df.loc[condition, target] = value

df.loc[df['duracao'].isnull(), 'duracao'] = round(df['duracao'].mean())
df.drop(df.loc[df['idade'].isnull()].index, inplace=False) # Inplace false to prevent change df

map_yes_no = {'no': 0, 'yes': 1}
cols = ['possui_casa', 'emprestimo']
df[cols] = df[cols].fillna("no")
df[cols] = df[cols].replace(map_yes_no)
df[cols] = df[cols].astype(int)

# df[cols].fillna(method='bfill', axis=0).fillna(0)

# %% Statistic functions
df.duracao.median()
df.duracao.mode()
df.duracao.mean()
df.duracao.max()
df.duracao.min()

# %% Conversion functions (After data treatment)
df.educacao = pd.to_numeric(df.educacao)

# %%
df_r = pd.read_csv('datasets/dataset_5.csv')
# %% Lambda functions (map)
review_points_mean = df_r.points.mean()
df_r.points.map(lambda p: p - review_points_mean)

# %% Apply function map
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

df_r.apply(remean_points, axis='columns')
# %% Return format manipulation
df_r.country + " - " + df_r.region_1

# %% Groupby needed for aggregate functions like count or sum
df_r.groupby('points').points.count()
df_r.groupby('points').price.min()
df_r.groupby('winery').apply(lambda df: df.description.iloc[0])
df_r.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
df_r.groupby(['country']).price.agg([len, min, max])

# %% Multi index operation
mi_df = df_r.groupby(['country', 'province']).description.agg([len])
mi_df.reset_index()

# %% Sort values
mi_df.sort_values(by='len')
mi_df.sort_values(by='len', ascending=False)
mi_df.sort_index()
mi_df.sort_values(by=['country', 'len'])

# %% Rename
df_r.rename(columns={'points': 'score'})
df_r.rename(index={0: 'firstEntry', 1: 'secondEntry'})
df_r.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# %%
pd.concat([df_r, df])

# %% Join reminder, check documentation for more detail
df.join(df_r, lsuffix='_CAN', rsuffix='_UK')
# df.merge(df_r) Commented because there is no common column

# %% Date parse
df_l = pd.read_csv('datasets/dataset_4.csv')
df_l['date_parsed'] = pd.to_datetime(df_l['date'], format="%m/%d/%y")
days = df_l['date_parsed'].dt.day

# %%
days.tolist()
days[:15].to_dataframe()
# %%
