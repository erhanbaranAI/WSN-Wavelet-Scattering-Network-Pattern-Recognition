from kymatio import Scattering2D
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Scattering nesnesi tanımla
sc = Scattering2D(J=2, shape=(256, 256))

feature_vectors = []

# Görsellerden öznitelik çıkar
for file in sorted(os.listdir("deneme")):
    if file.endswith(".tiff"):
        img = cv2.imread(f"deneme/{file}", cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (256, 256)).astype(np.float32) / 255.0
        feat = sc(img).reshape(-1)
        feature_vectors.append(feat)

# Ardışık kareler arası benzerlik (L2 mesafe)
similarities = []
for i in range(len(feature_vectors)-1):
    dist = np.linalg.norm(feature_vectors[i] - feature_vectors[i+1])
    similarities.append(dist)

# Dönüş noktalarını bul (minimumlar)
inverted_sim = -1 * np.array(similarities)
peaks, _ = find_peaks(inverted_sim, distance=5, prominence=0.05)

# Grafik çiz
plt.figure(figsize=(10, 5))
plt.plot(similarities, label="Distance")
plt.plot(peaks, np.array(similarities)[peaks], "rx", label="Pattern Reset Points")
plt.title("Desen Dönüş Noktaları")
plt.xlabel("Frame Index")
plt.ylabel("Feature Distance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Konsola yaz
print("Desenin başa döndüğü tespit edilen index'ler:", peaks, sep=",")
