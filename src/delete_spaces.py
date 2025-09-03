import os
import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import StringIO

# === 2. Dane S3 ===
bucket_name = 'small-rna'
object_key = 'differential_isomir_expression.csv'

# === 3. Pobranie danych z S3 ===
s3 = boto3.client('s3')

# Wczytaj plik CSV jako string
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)

# Przekonwertuj na DataFrame, z nagłówkiem w drugim wierszu (header=1)
body = csv_obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(body), header=1)

# Usuń spacje z nazw kolumn
df.columns = df.columns.str.strip()

# Sprawdź kolumny i pierwsze wiersze
print(df.columns)
print(df.head())

# === 4. Liczenie kategorii ===
category_counts = df['category'].value_counts()

# Opcjonalnie: ładniejsze etykiety
labels = {
    'trimmed': 'przycięte',
    'ambiguous tail': 'niejednoznaczny ogon',
    'NT tail': 'ogonek NT',
    'canonical': 'kanoniczne'
}
category_counts.rename(index=labels, inplace=True)

# === 5. Tworzenie wykresu kołowego ===
plt.style.use('seaborn-pastel')

category_counts.plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    figsize=(6, 6),
    ylabel='',
    title='Udział kategorii miRNA (category)'
)

plt.tight_layout()
plt.show()
