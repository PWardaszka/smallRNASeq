import boto3
import pandas as pd
from io import StringIO

# dane S3
bucket_name = 'small-rna'  # <- ZMIEŃ na własną nazwę bucketa
object_key = 'differential_isomir_expression.csv'  # <- Ścieżka do pliku w bucketcie


# 1. Stwórz klienta S3
s3 = boto3.client('s3')

# 2. Pobierz plik jako obiekt
csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)

# 3. Odczytaj zawartość pliku do Pandas
body = csv_obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(body))

# 4. Wyświetl pierwsze 5 wierszy
print(df.head())
