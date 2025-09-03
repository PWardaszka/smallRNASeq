import pandas as pd

# Ścieżka do Twojego pliku Excel
excel_path = "C:\\Users\\patry\\OneDrive\Dokumenty\\smallRNASeq\\data\\Supplemental_Table2 (1).xlsx"

# Wczytanie konkretnego arkusza
df = pd.read_excel(excel_path, sheet_name='Differential isomiR expression')

# Ścieżka docelowa CSV
csv_path = "C:\\Users\\patry\\OneDrive\Dokumenty\\smallRNASeq\\data\\differential_isomir_expression.csv"

# Zapis do pliku CSV
df.to_csv(csv_path, index=False)

print(f"Zapisano plik CSV do: {csv_path}")
