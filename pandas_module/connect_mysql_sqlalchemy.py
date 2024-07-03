# %% Example to connect with MySQL DB using SQL Alchemy
# Necessary the package pip install mysql-connector-python
# TODO: Necessary database creation file
import pandas as pd
import sqlalchemy

# %%
# MySQL Connection
MYSQL_USER = "root"
MYSQL_PASSWORD = "1234"
MYSQL_HOST_IP = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_DATABASE = "bd_livro01"

# Connect to localhost db with given options
engine = sqlalchemy.create_engine(
    "mysql+mysqlconnector://"
    + MYSQL_USER
    + ":"
    + MYSQL_PASSWORD
    + "@"
    + MYSQL_HOST_IP
    + ":"
    + str(MYSQL_PORT)
    + "/"
    + MYSQL_DATABASE,
    echo=False,
)
engine.connect()

# %% Read entire books table
# This command is not recommended with large tables
df_books = pd.read_sql_table("tb_livro", engine)
df_books.head()
# %% Using select to return data from table
query = """
    SELECT liv.titulo, YEAR(liv.dt_Livro) AS ano_livro, edt.editora
    FROM tb_livro liv
    INNER JOIN tb_editora edt ON liv.cd_editora = edt.cd_editora
    ORDER BY ano_livro, edt.editora, liv.titulo
    """
df_books_with_year = pd.read_sql_query(query, engine)
df_books_with_year

# %%
insert_data = {
    "isbn": [9, 10],
    "titulo": ["Fundamentos da Física", "Estatística Básica"],
    "cd_editora": [1, 3],
    "cd_genero": [2, 2],
    "preco": [50, 98],
    "dt_livro": ["2024-07-02", "2024-07-01"],
}
df_inserted = pd.DataFrame(insert_data)
df_inserted.to_sql(
    "tb_livro", engine, index=False, if_exists="replace"
)  # Change to append if first time inserting

# %%
