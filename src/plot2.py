import pandas as pd
import boto3
from io import StringIO
import matplotlib.pyplot as plt

bucket_name = 'small-rna'
object_key = 'differential_isomir_expression.csv'

s3 = boto3.client('s3')
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body'].read().decode('utf-8')

# Pomijamy dwa pierwsze wiersze, bo to tytuły
df = pd.read_csv(StringIO(body), skiprows=2, header=0)

# Usuwamy ewentualne spacje w nazwach kolumn
df.columns = df.columns.str.strip()

print("Nagłówki kolumn:")
print(df.columns)

print("\nPierwsze 5 wierszy:")
print(df.head())

# Filtrowanie tylko tych wierszy, gdzie 'significant' == 'significant'
if 'category' in df.columns and 'significant' in df.columns:
    filtered_df = df[df['significant'].str.strip().str.lower() == 'significant']

    category_counts = filtered_df['category'].value_counts()

    labels = {
        'trimmed': 'przycięte',
        'ambiguous tail': 'niejednoznaczny ogon',
        'NT tail': 'ogonek NT',
        'canonical': 'kanoniczne'
    }
    category_counts.rename(index=labels, inplace=True)

    plt.style.use('seaborn-v0_8-pastel')
    category_counts.plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        figsize=(6, 6),
        ylabel='',
        title='Udział kategorii miRNA (tylko significant)'
    )
    plt.tight_layout()
    plt.show()
else:
    print("Kolumna 'category' lub 'significant' nie istnieje w dataframe.")
