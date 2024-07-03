# %% Example of google cloud usage to retrieve queries
# This file need google cloud authentication to properly work
from google.cloud import bigquery

# %%
client = bigquery.Client()

QUERY = (
    "SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` "
    'WHERE state = "TX" '
    "LIMIT 100"
)
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
# %%
query = """
        SELECT score, title
        FROM `bigquery-public-data.hacker_news.full`
        WHERE type = "job" 
        """

dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)
tables = list(client.list_tables(dataset))
for table in tables:
    print(table.table_id)
table_ref = dataset_ref.table("full")
table = client.get_table(table_ref)
table.schema
client.list_rows(table, max_results=5).to_dataframe()

ONE_MB = 1000 * 1000
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_MB)
safe_query_job = client.query(query, job_config=safe_config)
safe_query_job.to_dataframe()
