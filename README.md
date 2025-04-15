
# Örüntü Tespiti - Wavelet Scattering ile Tekrar Eden Kumaş Desenleri

Bu proje, bir kumaş üretim hattında sıralı olarak çekilen görüntülerden, **Wavelet Scattering Network (WSN)** kullanarak **örüntünün tekrar ettiği anları** tespit eder. İlk olarak "örüntü başı" olarak alınan görsel, klasördeki tüm diğer görsellerle karşılaştırılır. Benzerliği belirli bir eşikten küçük olanlar tekrar eden desenler olarak değerlendirilir ve kaydedilir.

---

## 📂 Klasör Yapısı

```
WSN-Wavelet-scattering-network/
│
├── desen_donus_gorselleri/         # İlk filtrelenmiş, örüntünün başa döndüğü kareler
├── tekrar_desenler_kararli/        # Bu script ile yakalanan tekrar eden örüntü kareleri
├── kumasv3.py                      # Bu script (tekrar tespiti yapar)
├── kaydetme.py / kumasv1.py       # Ön aşamalarda kullanılan diğer scriptler
└── README.md                       # Açıklama dosyası
```

---

## ⚙️ Kullanım

### 1. Ortam Kurulumu

Aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

```bash
pip install kymatio numpy opencv-python matplotlib
```

### 2. Script'i Çalıştır

```bash
python kumasv3.py
```

---

## 🧠 Algoritma Açıklaması

- **Wavelet Scattering** kullanılarak her görselden öznitelik çıkarılır
- İlk kare referans alınır (`frame 0`)
- Diğer tüm karelerle **L2 mesafesi (Euclidean distance)** hesaplanır
- Eğer mesafe `threshold` değerinin altındaysa, o kare tekrar eden örüntü olarak kabul edilir

```python
threshold = 4.0  # Bu değer ile hassasiyet ayarlanır
```

> Örnek çıktı:
```
Frame 0 ile Frame 5: 3.82
Frame 0 ile Frame 6: 6.14
...
```

---

## ✅ Sonuç

- Tespit edilen tekrar kareleri `tekrar_desenler_kararli/` klasörüne `.png` olarak kaydedilir
- Script sonunda toplam kaç örüntü tespit edildiği yazdırılır

---

## 👤 Geliştirici

**Erhan Baran**  
📌 [LinkedIn](https://www.linkedin.com/in/erhanbaran)  
📧 erhanbaran.dev [@] gmail.com  
