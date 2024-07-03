# %% Using simple imputer to handle missing values on dataset
# Other strategies can be more useful, this one is just a example
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

df_test_imputer = pd.read_csv("../datasets/melb_data.csv")
y = df_test_imputer.Price

test_predictor = df_test_imputer.drop(["Price"], axis=1)
X = test_predictor.select_dtypes(exclude=["object"])

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, test_size=0.2, random_state=0
)

imputer_test = SimpleImputer()
imputed_X_train = pd.DataFrame(imputer_test.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(imputer_test.transform(X_valid))
imputed_X_train.columns = X_train.columns  # Putting columns names back
imputed_X_valid.columns = X_valid.columns

imputed_X_train.head()
