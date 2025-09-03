import os
import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import StringIO

# === Dane S3 ===
bucket_name = 'small-rna'
object_key = 'differential_isomir_expression.csv'

# Pobranie danych z S3
s3 = boto3.client('s3')
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body'].read().decode('utf-8')

# Wczytanie do DataFrame z pominięciem zbędnych linii (header zaczyna się od 3-ciego wiersza)
df = pd.read_csv(StringIO(body), header=3)
print("Nagłówki kolumn:", df.columns)
print(df.head())

# Filtracja: tylko wiersze, gdzie 'significant' == 'significant'
df_significant = df[df['significant'] == 'significant']

# Liczenie kategorii dla filtrowanych danych
category_counts = df_significant['category'].value_counts()

# Opcjonalnie: ładniejsze etykiety
labels = {
    'trimmed': 'przycięte',
    'ambiguous tail': 'niejednoznaczny ogon',
    'NT tail': 'ogonek NT',
    'canonical': 'kanoniczne'
}
category_counts.rename(index=labels, inplace=True)

# Tworzenie wykresu kołowego
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
