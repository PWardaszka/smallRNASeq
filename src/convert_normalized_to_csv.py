import pandas as pd

# Ścieżka do pliku Excel
excel_path = "C:\\Users\\patry\\OneDrive\\Dokumenty\\smallRNASeq\\data\\Supplemental_Table2 (1).xlsx"

# Wczytaj arkusz z pominięciem dwóch pierwszych wierszy
df = pd.read_excel(excel_path, sheet_name='Normalized isomiR counts', skiprows=2)

# Zapisz do pliku CSV
df.to_csv('normalized_isomir_counts.csv', index=False)

print("Plik CSV został zapisany jako 'normalized_isomir_counts.csv'")
