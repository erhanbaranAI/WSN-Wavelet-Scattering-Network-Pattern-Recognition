from kymatio import Scattering2D
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Ayıklanmış örüntülerin bulunduğu klasör
input_folder = "desen_donus_gorselleri"
output_folder = "tekrar_desenler_kararli"
os.makedirs(output_folder, exist_ok=True)

sc = Scattering2D(J=2, shape=(256, 256))
features = []
file_list = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])

# Tüm görsellerden Wavelet özniteliklerini çıkar
for file in file_list:
    img = cv2.imread(os.path.join(input_folder, file), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256)).astype(np.float32) / 255.0
    feat = sc(img).reshape(-1)
    features.append(feat)

features = np.array(features)

# Karşılıklı uzaklık matrisi hesapla
num = len(features)
dist_matrix = np.zeros((num, num))

for i in range(num):
    for j in range(num):
        dist_matrix[i, j] = np.linalg.norm(features[i] - features[j])

# Her karenin kendine çok benzeyen tekrarlarını bul
# İlk kareyi referans al, ona çok benzeyenleri seç
threshold = 4.0  # Bu değeri gerekirse düşür veya artır
repeat_indexes = []

for i in range(1, num):  # 0 zaten referans
    dist = dist_matrix[0, i]
    print(f"Frame 0 ile Frame {i}: {dist:.2f}")
    if dist_matrix[0, i] < threshold:
        repeat_indexes.append(i)

# Kayıt
for idx in repeat_indexes:
    src = os.path.join(input_folder, file_list[idx])
    dst = os.path.join(output_folder, f"repeat_match_{idx:04d}.png")
    img = cv2.imread(src)
    cv2.imwrite(dst, img)

print(f"{len(repeat_indexes)} tekrar eden örüntü bulundu ve '{output_folder}' klasörüne kaydedildi.")
