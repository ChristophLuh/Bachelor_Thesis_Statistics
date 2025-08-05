import pandas as pd
import numpy as np
from scipy.stats import kruskal



patient_data = pd.read_csv("C:/Users/Chris/OneDrive - Universität Heidelberg/Bachelorarbeit/Finale/Patient Data.csv", sep = ";", na_values=['N/A ', 'NA', 'NaN', ''])


# Gruppiere die Daten nach Organ
grouped = patient_data.groupby('PV')['frequency'].apply(list)

# Führe den Kruskal-Wallis-Test aus
stat, p_value = kruskal(*grouped)

print(f"Kruskal-Wallis-Statistik: {stat:.3f}")
print(f"p-Wert: {p_value:.4f}")
print(grouped)
