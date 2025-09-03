import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj plik CSV z podfolderu 'data'
df = pd.read_csv('data/normalized_isomir_counts.csv')

# Usuń ewentualne spacje w nazwach kolumn
df.columns = df.columns.str.strip()

# Sprawdź, czy kolumny istnieją
if 'WT' in df.columns and 'category' in df.columns:
    # Usuń wiersze, gdzie brakuje wartości w WT lub category
    df = df.dropna(subset=['WT', 'category'])

    # Zsumuj liczbę zliczeń dla każdej kategorii
    category_sums = df.groupby('category')['WT'].sum()

    # Przetłumacz nazwy kategorii na język polski (opcjonalnie)
    labels = {
        'canonical': 'kanoniczne',
        'NT tail': 'ogonek NT',
        'trimmed': 'przycięte',
        'ambiguous tail': 'niejednoznaczny ogon'
    }
    category_sums.rename(index=labels, inplace=True)

    # Styl wykresu
    plt.style.use('seaborn-v0_8-pastel')
    category_sums.plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        figsize=(6, 6),
        ylabel='',
        title='Udział zliczeń miRNA (kolumna WT) wg kategorii'
    )

    plt.tight_layout()
    plt.show()

else:
    print("Brakuje kolumn 'WT' lub 'category' w pliku CSV.")
