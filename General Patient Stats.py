import pandas as pd
# Alle Spalten anzeigen
pd.set_option('display.max_columns', None)
# CSV einlesen
Pat_Data = pd.read_csv("C:/Users/Chris/OneDrive - Universität Heidelberg/Bachelorarbeit/Finale/Patient Data_final.csv", sep=";")

# Relevante Spalten in numerisch umwandeln
cols_to_numeric = ["frequency", "area", "monocrypt", "oligocrypt", "polycrypt", "number_DC"]
Pat_Data[cols_to_numeric] = Pat_Data[cols_to_numeric].apply(pd.to_numeric, errors="coerce")

# Gruppieren und aggregieren
Stats = Pat_Data.groupby("organ").agg(
    mean_frequency=("frequency", "mean"),
    sum_area=("area", "sum"),
    sum_monocrypt=("monocrypt", "sum"),
    sum_oligocrypt=("oligocrypt", "sum"),
    sum_polycrypt=("polycrypt", "sum"),
    sum_number_DC=("number_DC", "sum")
).reset_index()

# Ausgabe
print(Stats)
Stats.to_excel("C:/Users/Chris/OneDrive - Universität Heidelberg/Bachelorarbeit/Finale/Stats.xlsx", index=False)

