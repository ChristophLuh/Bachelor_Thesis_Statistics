import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Platzhalter: Hier später deine Pfade einsetzen
image_files = {
    'A': {'HE': 'Images/Hux_021_B_HE_1.ome.tif', 'MLH1': 'Images/Hux_021_B_MLH1_1.ome.tif', 'MSH2': 'Images/Hux_021_B_MSH2_1.ome.tif'},
    'B': {'HE': 'Images/Hux_021_B_HE_2.ome.tif', 'MLH1': 'Images/Hux_021_B_MLH1_2.ome.tif', 'MSH2': 'Images/Hux_021_B_MSH2_2..ome.tif'},
    'C': {'HE': 'Images/Hux_021_C_HE_1.ome.tif', 'MLH1': 'Images/Hux_021_C_MLH1_1.ome.tif', 'MSH2': 'Images/Hux_021_C_MSH2_1.ome.tif'},
    'D': {'HE': 'Images/Hux_021_C_HE_2.ome.tif', 'MLH1': 'Images/Hux_021_C_MLH1_2.ome.tif', 'MSH2': 'Images/Hux_021_C_MSH2_2.ome.tif'}
}

output_dir = "C:/Users/Chris/PycharmProjects/Bachelor_Thesis_Statistics/Images/"
os.makedirs(output_dir, exist_ok=True)

stains = ['HE', 'MLH1', 'MSH2']
frame_px = 6
dpi = 300

for sample, stain_paths in image_files.items():
    # Bilder laden
    imgs = {stain: Image.open(stain_paths[stain]).convert('RGB') for stain in stains}

    # Kleinste Breite und Höhe im Set bestimmen
    min_width = min(img.width for img in imgs.values())
    min_height = min(int(img.height * min_width / img.width) for img in imgs.values())

    processed = []
    for stain in stains:
        img = imgs[stain]
        # proportional auf min_width skalieren
        new_height = int(img.height * min_width / img.width)
        img_resized = img.resize((min_width, new_height))

        if new_height > min_height:
            # Abschneiden (oben)
            img_cropped = img_resized.crop((0, 0, min_width, min_height))
        else:
            # Vertikal mittig auffüllen mit weißem Hintergrund
            top_padding = (min_height - new_height) // 2
            canvas = Image.new('RGB', (min_width, min_height), (255, 255, 255))
            canvas.paste(img_resized, (0, top_padding))
            img_cropped = canvas

        # Rahmen hinzufügen
        bordered = ImageOps.expand(img_cropped, border=frame_px, fill='black')
        processed.append(bordered)

    # Panel zeichnen
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.5), facecolor='white')
    for idx, ax in enumerate(axes):
        ax.imshow(processed[idx])
        ax.axis('off')
        ax.set_title(stains[idx], fontsize=20, fontweight='bold', fontname='Arial')

    plt.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.02, wspace=0.04)
    output_path = os.path.join(output_dir, f"panel_{sample}.png")
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close()