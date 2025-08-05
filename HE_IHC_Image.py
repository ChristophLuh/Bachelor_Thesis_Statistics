import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import os

# Neuer Exportpfad mit "2" am Ende
export_path = r"C:\Users\Chris\PycharmProjects\Bachelor_Thesis_Statistics\Images\panel_output2.png"

# Bildpfade
image_files = {
    'HE': [
        'Images/Hux_021_C_HE.ome.ome.tif',
        'Images/Hux_023_B_HE.ome.tif',
        'Images/Hux_053_F_HE.ome.ome.tif'
    ],
    'MLH1': [
        'Images/Hux_021_C_MLH1.ome.tif',
        'Images/Hux_023_B_MLH1.ome.tif',
        'Images/Hux_053_F_MLH1.ome.tif'
    ],
    'MSH2': [
        'Images/Hux_021_C_MSH2.ome.ome.ome.tif',
        'Images/Hux_023_B_MSH2.ome.tif',
        'Images/Hux_053_F_MSH2.ome.ome.tif'
    ]
}

column_titles = ['A', 'B', 'C']
row_labels = ['H&E', 'MLH1', 'MSH2']

loaded_images = {stain: [] for stain in image_files}
min_width, min_height = float('inf'), float('inf')

# Bilder einlesen und kleinste Größe bestimmen
for stain in image_files:
    for path in image_files[stain]:
        img = Image.open(path).convert('RGB')
        loaded_images[stain].append(img)
        w, h = img.size
        min_width = min(min_width, w)
        min_height = min(min_height, h)

image_border_px = 6

# Plot erstellen
fig, axes = plt.subplots(3, 3, figsize=(12, 12), facecolor='white')
stains = ['HE', 'MLH1', 'MSH2']

for row_idx, stain in enumerate(stains):
    for col_idx in range(3):
        ax = axes[row_idx, col_idx]
        img = loaded_images[stain][col_idx]

        # MLH1 Bild in der Mitte drehen
        if stain == 'MLH1' and col_idx == 1:
            img = img.rotate(180)

        # Bilder an kleinste Größe anpassen
        img_resized = img.resize((min_width, min_height))
        canvas = Image.new('RGB', (min_width, min_height), (255, 255, 255))
        offset_x = (min_width - img_resized.width) // 2
        offset_y = min_height - img_resized.height
        canvas.paste(img_resized, (offset_x, offset_y))

        # Rahmen hinzufügen
        bordered_img = ImageOps.expand(canvas, border=image_border_px, fill='black')

        # Anzeige im Subplot
        ax.imshow(bordered_img)
        ax.axis('off')

        # Spaltentitel A, B, C
        if row_idx == 0:
            ax.set_title(column_titles[col_idx],
                         fontsize=28, fontname='Arial', fontweight='bold', color='black', pad=20)

        # Zeilenbeschriftung (H&E, MLH1, MSH2)
        if col_idx == 0:
            ax.set_ylabel(row_labels[row_idx],
                          fontsize=16, rotation=90, labelpad=10, color='black', fontname='Arial', fontweight='bold')

# Layoutanpassung (angepasst für genügend Platz!)
plt.subplots_adjust(left=0.06, right=0.96, top=0.93, bottom=0.05, hspace=0.12, wspace=0.0125)

# Speichern
plt.savefig(export_path, dpi=300, facecolor='white', bbox_inches='tight')
plt.show()

print(f"Panel erfolgreich gespeichert unter:\n{export_path}")
