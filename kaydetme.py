import os
import cv2

# Tespit edilen desen başlama indexleri
pattern_indexes = [ 7,  13,  19,  24,  29,  39,  44,  54,  60,  70,  75,  81,  86,  92, 102, 111, 116, 122,
 128, 133, 138, 143, 149, 154, 164, 169, 179, 185, 195, 201, 206, 211, 218, 226, 231, 237, 242,
 247, 252, 262, 273]

input_folder = "deneme"
output_folder = "desen_donus_gorselleri"
os.makedirs(output_folder, exist_ok=True)

files = [f for f in os.listdir(input_folder) if f.endswith(".tiff")]

for idx in pattern_indexes:
    if idx < len(files):
        file_name = files[idx]
        img = cv2.imread(os.path.join(input_folder, file_name))
        output_path = os.path.join(output_folder, f"reset_{idx:04d}.png")
        cv2.imwrite(output_path, img)

print(f"{len(pattern_indexes)} adet desen başlangıç görseli '{output_folder}' klasörüne kaydedildi.")
