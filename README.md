<div align="center">

# 🐟 Fish Classifier Pro
### Dashboard Analisis Klasifikasi Citra Ikan (UAP Machine Learning)


![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16.1-orange?style=for-the-badge&logo=tensorflow&logoColor=white)

<br>

<p align="center">
  <b>Klasifikasi Ikan End-to-End dengan Perbandingan 3 Model Deep Learning</b><br>
  Custom CNN | VGG16 | MobileNetV2
</p>

</div>

---

## 📝 Deskripsi Proyek
**Fish Classifier Pro** adalah sistem klasifikasi citra berbasis *Deep Learning* yang dikembangkan untuk memenuhi **Ujian Akhir Praktikum (UAP) Pembelajaran Mesin**. Proyek ini bertujuan untuk mengklasifikasikan 5 jenis ikan secara otomatis menggunakan antarmuka web interaktif berbasis Streamlit.

Sistem ini membandingkan performa antara model yang dibangun dari awal (*Custom CNN*) dengan model *Transfer Learning* (*VGG16* dan *MobileNetV2*) untuk menganalisis efektivitas arsitektur terhadap dataset ikan.

---

## 📊 Dataset dan Preprocessing
Dataset yang digunakan bersumber dari Kaggle: **[My Fish Dataset](https://www.kaggle.com/datasets/srajangoyal1808/my-fish-dataset)**.

* **Jumlah Data:** > 5.000 citra (termasuk augmentasi).
* **Kelas (Label):**
    1.  `Archer Fish` (Ikan Pemanah)
    2.  `Betta Fish` (Ikan Cupang)
    3.  `Blue Tang` (Dory)
    4.  `Clown Sword Trigger Fish`
    5.  `Yellow Tang`
* **Preprocessing:**
    * **Resizing:** Citra diubah menjadi **128x128 pixel**.
    * **Augmentation:** Rotasi, Zoom, dan Flip untuk variasi data latih.
    * **Normalization:** Pixel dinormalisasi ke rentang 0-1.

---

## 🧠 Model yang Digunakan
Sesuai ketentuan UAP, proyek ini mengimplementasikan 3 model untuk perbandingan:

| Tipe Model | Nama Model | Deskripsi |
| :--- | :--- | :--- |
| **Non-Pretrained** | **Custom CNN** | Arsitektur CNN sederhana yang dibangun *from scratch* (Conv2D, MaxPooling, Dropout). |
| **Transfer Learning** | **VGG16** | Model *State-of-the-art* dengan bobot ImageNet. Layer atas di-*freeze*. |
| **Transfer Learning** | **MobileNetV2** | Model ringan (*lightweight*) yang efisien, cepat, dan akurat untuk deployment web. |

---

## 📈 Hasil Evaluasi dan Analisis Perbandingan
Berikut adalah tabel perbandingan performa ketiga model berdasarkan pengujian pada data test:

| Nama Model | Akurasi | Precision | Recall | Hasil Analisis |
| :--- | :---: | :---: | :---: | :--- |
| **Custom CNN** | **1.00** | 1.00 | 1.00 | Sangat akurat pada data uji, namun terindikasi **Overfitting**. Saat dicoba prediksi gambar dari internet, terkadang salah (khususnya *Betta Fish*). |
| **MobileNetV2** | **0.97** | 0.97 | 0.97 | **Model Terbaik.** Memberikan keseimbangan performa dan kecepatan. Generalisasi sangat baik pada data baru/asing. |
| **VGG16** | **0.92** | 0.92 | 0.92 | Akurasi terendah. Model ini sangat kompleks (berat) dan mungkin memerlukan *fine-tuning* lebih mendalam untuk dataset yang spesifik ini. |

> **Kesimpulan:** Untuk implementasi aplikasi nyata, **MobileNetV2** dipilih karena ukurannya kecil (<20MB) dan akurasinya stabil di 97%.

### 🖼️ Visualisasi Performa
Berikut adalah bukti visualisasi hasil pelatihan (Confusion Matrix & Grafik Loss).

**1. Analisis Custom CNN**
| Confusion Matrix | Grafik Training |
| :---: | :---: |
| ![Matrix CNN](Assets/cnn-confusion_matrix.png) | ![Plot CNN](Assets/CNN_plot.png) |

**2. Analisis Model Pretrained (VGG16 & MobileNetV2)**
| Perbandingan Matrix | Perbandingan Grafik |
| :---: | :---: |
| ![Matrix VGG MobileNet](Assets/confusion_matrix_vgg_mobilenet.png) | ![Plot VGG MobileNet](Assets/plot_vgg_mobilenet.png) |

---

## 💻 Tampilan Aplikasi
Aplikasi dibangun menggunakan **Streamlit**. Berikut adalah antarmuka saat melakukan prediksi multi-model:
![Tampilan Awal Dashboard](Assets/tampilan-awal.png)
![Tampilan Prediksi](Assets/tampilan-prediksi-3-model.png)

## 💻 Struktur Kode VSCODE
Tampilan Struktur isi **VSCODE**. Berikut adalah antarmuka saat melakukan prediksi multi-model:
![Tampilan Awal Dashboard](Assets/susunan-folder-vscode.png)

---

## 📂 Struktur Folder Proyek
Struktur direktori repository ini disusun sesuai standar pengumpulan:

```text
UAP_MachineLearning_161/
├── Assets/
│   └──                       # Aset gambar untuk dokumentasi
├── notebooks/
│   └── UAP_ML_C_2022_161.ipynb  # Source code pelatihan model (Jupyter)
├── app.py                    # File utama aplikasi Streamlit
├── requirements.txt          # Daftar library yang dibutuhkan
└── README.md                 # Dokumentasi proyek
