import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
Crypt_Data = pd.read_csv("C:/Users/Chris/OneDrive - Universität Heidelberg/Bachelorarbeit/Finale/Single Crypt Data.csv", sep=";")

plt.figure(figsize=(10, 5))

# Farben und Einstellungen
colors = ['navy', 'rebeccapurple']  # Pastelltöne
box_width = 0.6
padding_factor = 0.25  # 25% Abstand links/rechts

left_limit = 1 - box_width / 2 - padding_factor * box_width
right_limit = 1 + box_width / 2 + padding_factor * box_width

# Boxplot für Size
plt.subplot(1, 2, 1)
box1 = plt.boxplot(Crypt_Data['Size'].dropna(), positions=[1], patch_artist=True, widths=box_width)
for patch in box1['boxes']:
    patch.set_facecolor(colors[0])
for median in box1['medians']:
    median.set_color('white')
    median.set_linewidth(2)
plt.title('Area of MMR-DC')
plt.ylabel('Size')
plt.xlim(left_limit, right_limit)
plt.xticks([1], ['Size'])

# Boxplot für Diameter
plt.subplot(1, 2, 2)
box2 = plt.boxplot(Crypt_Data['Diameter'].dropna(), positions=[1], patch_artist=True, widths=box_width)
for patch in box2['boxes']:
    patch.set_facecolor(colors[1])
for median in box2['medians']:
    median.set_color('white')
    median.set_linewidth(2)
plt.title('Diameter of MMR-DC')
plt.ylabel('Diameter')
plt.xlim(left_limit, right_limit)
plt.xticks([1], ['Diameter'])

plt.tight_layout()
plt.show()
