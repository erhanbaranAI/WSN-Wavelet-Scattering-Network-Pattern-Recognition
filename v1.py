from kymatio import Scattering2D
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Veri Seti")
# 1. Veri Seti
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X = X.to_numpy().reshape(-1, 28, 28).astype(np.float32) / 255.0
y = y.astype(np.int64)

print("Scattering ile Öznitelik Çıkar")
# 2. Scattering ile Öznitelik Çıkar
scattering = Scattering2D(J=2, shape=(28, 28))
features = np.array([scattering(x) for x in X])

print("Öznitelik düzleştir")
# 3. Öznitelik düzleştir
X_feat = features.reshape(features.shape[0], -1)

print("Eğitim")
# 4. Eğitim
X_train, X_test, y_train, y_test = train_test_split(X_feat, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

print("Tahmin")
# 5. Tahmin
y_pred = clf.predict(X_test)
print("Doğruluk: ", accuracy_score(y_test, y_pred))
