# %% Example of join, concatenate and lambda function using pandas
import pandas as pd

df_l = pd.read_csv("../datasets/dataset_4.csv")
df_r = pd.read_csv("../datasets/dataset_5.csv")

# %% Lambda functions iterate over entire dataframe
review_points_mean = df_r.points.mean()
df_r.points.map(lambda p: p - review_points_mean)


# %% Usage similar to lambda function but for more complex operations
def remean_points(row):
    row.points = row.points - review_points_mean
    return row


df_r.apply(remean_points, axis="columns")
# %% We can manipulate columns simple as that
df_r.country + " - " + df_r.region_1

# %% GroupBy needed for aggregate functions like count or sum
df_r.groupby("points").points.count()
df_r.groupby("points").price.min()
df_r.groupby("winery").apply(lambda df: df.description.iloc[0])
df_r.groupby(["country", "province"]).apply(lambda df: df.loc[df.points.idxmax()])
df_r.groupby(["country"]).price.agg([len, min, max])

# %% GroupBy will generate a new index returning a multi index DataSet
mi_df = df_r.groupby(["country", "province"]).description.agg([len])
mi_df.reset_index()  # Needed to reset index after the group by

# %% Funcitons to sort values
mi_df.sort_values(by="len")
mi_df.sort_values(by="len", ascending=False)
mi_df.sort_index()
mi_df.sort_values(by=["country", "len"])

# %% Renaming columns and axis
df_r.rename(columns={"points": "score"})
df_r.rename(index={0: "firstEntry", 1: "secondEntry"})
df_r.rename_axis("wines", axis="rows").rename_axis("fields", axis="columns")

# %% Concatenation of two datasets
pd.concat([df_r, df_l])

# %% Join simple usage, check documentation for more detail
df_l.join(df_r, lsuffix="_CAN", rsuffix="_UK")
# df.merge(df_r) Commented because there is no common column

# %% Date parse example
df_l["date_parsed"] = pd.to_datetime(df_l["date"], format="%m/%d/%y")
days = df_l["date_parsed"].dt.day
print(days)
days = days.tolist()
# days[:15].to_dataframe()
# %%
