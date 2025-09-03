import os
import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import StringIO
from dotenv import load_dotenv

# === 1. Wczytanie zmiennych środowiskowych (.env) ===
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")  # jeśli nie masz, ustawi domyślny region

# === 2. Dane S3 ===
bucket_name = 'tsmall-rna'
object_key = 'differential_isomir_expression.csv'

# === 3. Pobranie danych z S3 ===
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Wczytaj plik CSV jako string
obj = s3.get_object(Bucket=bucket_name, Key=object_key)
csv_data = obj['Body'].read().decode('utf-8')

# Przekonwertuj na DataFrame
df = pd.read_csv(StringIO(csv_data))

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
