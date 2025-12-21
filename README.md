\# 🐟 Fish Classifier Pro  

\## Multi-Model Deep Learning Analytics Dashboard



\[!\[Streamlit App](https://static.streamlit.io/badges/streamlit\_badge\_svg.svg)](https://github.com/Frizal14/UAP\_MachineLearning\_161)

\[!\[Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

\[!\[TensorFlow 2.16.1](https://img.shields.io/badge/TensorFlow-2.16.1-orange.svg)](https://www.tensorflow.org/)



\*\*Fish Classifier Pro\*\* adalah aplikasi \*\*dashboard analisis klasifikasi citra ikan berbasis Deep Learning\*\* yang dikembangkan untuk memenuhi \*\*Ujian Akhir Praktikum (UAP) Machine Learning\*\*.



Aplikasi ini membandingkan performa \*\*tiga model Convolutional Neural Network (CNN)\*\*:



\- 🔹 \*\*Custom CNN\*\*

\- 🔹 \*\*VGG16 (Transfer Learning)\*\*

\- 🔹 \*\*MobileNetV2 (Pretrained \& Lightweight)\*\*



Fokus utama proyek ini adalah \*\*menganalisis perbedaan akurasi, stabilitas, dan generalisasi model CNN\*\* pada klasifikasi citra multi-kelas.



---



\## 📑 Daftar Isi

1\. \[Dataset \& Kategori](#-dataset--kategori)

2\. \[Model yang Digunakan](#-model-yang-digunakan)

3\. \[Hasil Evaluasi Model](#-hasil-evaluasi-model)

4\. \[Visualisasi \& Dokumentasi Asset](#-visualisasi--dokumentasi-asset)

5\. \[Struktur Folder Proyek](#-struktur-folder-proyek)

6\. \[Unduh Model (Weights)](#-unduh-model-weights)

7\. \[Panduan Instalasi \& Penggunaan](#-panduan-instalasi--penggunaan)

8\. \[Informasi Pengembang](#-informasi-pengembang)



---



\## 📊 Dataset \& Kategori

Dataset yang digunakan adalah \*\*My Fish Dataset\*\* dari Kaggle yang terdiri dari \*\*5 kelas ikan\*\*:



\- \*\*Archer Fish\*\* – Ikan pemanah dengan kemampuan menyemprotkan air

\- \*\*Betta Fish\*\* – Ikan cupang dengan warna dan sirip kontras

\- \*\*Blue Tang\*\* – Ikan laut berwarna biru

\- \*\*Clown Sword Trigger Fish\*\* – Ikan berpola kompleks

\- \*\*Yellow Tang\*\* – Ikan laut berwarna kuning cerah



🔗 \*\*Dataset\*\*:  

\[My Fish Dataset (Kaggle)](https://www.kaggle.com/datasets/srajangoyal1808/my-fish-dataset)



---



\## 🧠 Model yang Digunakan



| Model | Pendekatan | Deskripsi |

|-----|-----------|----------|

| Custom CNN | From Scratch | Arsitektur CNN sederhana buatan sendiri |

| VGG16 | Transfer Learning | Model pretrained dengan performa stabil |

| MobileNetV2 | Pretrained | Model ringan dan efisien |



---



\## 🚀 Hasil Evaluasi Model



| Model | Accuracy | Precision | Recall | F1-Score |

|------|----------|-----------|--------|---------|

| \*\*Custom CNN\*\* | \*\*1.00\*\* | 1.00 | 1.00 | 1.00 |

| \*\*VGG16\*\* | 0.92 | 0.92 | 0.92 | 0.92 |

| \*\*MobileNetV2\*\* | 0.97 | 0.97 | 0.97 | 0.97 |



⚠️ \*\*Catatan Analisis\*\*  

Meskipun \*\*Custom CNN\*\* mencapai skor sempurna pada data uji, pengujian prediksi real-time menunjukkan adanya kesalahan pada kelas tertentu (khususnya \*\*Betta Fish\*\*).  

Hal ini menunjukkan indikasi \*\*overfitting\*\*, sehingga model pretrained cenderung lebih stabil.



---



\## 🖼️ Visualisasi \& Dokumentasi Asset



\### 1️⃣ Confusion Matrix – Custom CNN

Menunjukkan distribusi prediksi benar dan salah untuk setiap kelas ikan pada model Custom CNN.



!\[CNN Confusion Matrix](Assets/images/cnn\_confusion\_matrix.png)



---



\### 2️⃣ Grafik Training Custom CNN

Grafik akurasi dan loss selama proses training dan validation Custom CNN.



!\[CNN Training Plot](Assets/images/cnn\_plot.png)



---



\### 3️⃣ Confusion Matrix – VGG16 \& MobileNetV2

Perbandingan performa klasifikasi antara dua model pretrained.



!\[Confusion Matrix VGG \& MobileNet](Assets/images/confusion\_matrix\_vgg\_mobilenet.png)



---



\### 4️⃣ Hasil Prediksi Acak – Custom CNN

Contoh hasil prediksi citra uji secara acak menggunakan Custom CNN.



!\[Random Prediction CNN](Assets/images/hasil\_prediksi\_acak\_cnn.png)



---



\### 5️⃣ Grafik Training VGG16 \& MobileNetV2

Visualisasi performa training dan validation kedua model pretrained.



!\[Plot VGG \& MobileNet](Assets/images/plot\_vgg\_mobilenet.png)



---



\### 6️⃣ Prediksi 2 Model Pretrained

Perbandingan hasil prediksi antara VGG16 dan MobileNetV2 pada citra yang sama.



!\[Prediksi 2 Model](Assets/images/prediksi\_2\_model\_pretrained.png)



---



\### 7️⃣ Struktur Folder VS Code

Struktur folder proyek saat pengembangan di VS Code.



!\[Struktur Folder VS Code](Assets/images/susunan\_folder\_vscode.png)



---



\### 8️⃣ Tampilan Awal Aplikasi

Tampilan halaman utama aplikasi Streamlit sebelum input gambar.



!\[Tampilan Awal](Assets/images/tampilan\_awal.png)



---



\### 9️⃣ Tampilan Prediksi 3 Model Sekaligus

Fitur utama aplikasi yang menampilkan hasil prediksi \*\*Custom CNN, VGG16, dan MobileNetV2 secara bersamaan\*\*.



!\[Prediksi 3 Model](Assets/images/tampilan\_prediksi\_3\_model.png)



---



\## 📂 Struktur Folder Proyek

```text

UAP\_MachineLearning\_161/

│

├── app.py

├── README.md

│

├── notebooks/

│   └── UAP\_ML\_C\_2022\_161.ipynb

│

├── Assets/

│   └── images/

│

└── models/

&nbsp;   └── README.md



\## 💾 Unduh Model, Instalasi, \& Informasi Pengembang



\### 📥 Unduh Model (Weights)

Karena keterbatasan ukuran file di GitHub, \*\*file model tidak disertakan langsung di dalam repository\*\*.  

Seluruh model dapat diunduh melalui Google Drive berikut:



\- \[Google Drive – Custom CNN Model](https://drive.google.com/drive/folders/1NOwoV9h9xUN17H8yYlRmD5Pfl\_3x5FNm)

\- \[Google Drive – VGG16 \& MobileNetV2 Models](https://drive.google.com/drive/folders/1nC7vPMUW\_5nIsZq7z5cIaPIo-DF7ypRF)



📌 \*\*Catatan\*\*:

\- Pastikan file model ditempatkan sesuai path yang digunakan di `app.py`

\- \*\*Google Colab\*\*: gunakan path `/content/drive/MyDrive/...`

\- \*\*Lokal / VS Code\*\*: gunakan path relatif sesuai struktur proyek



---



\### 🛠️ Tutorial Instalasi \& Penggunaan



\#### 1. Clone Repository



git clone https://github.com/Frizal14/UAP\_MachineLearning\_161.git

cd UAP\_MachineLearning\_161



\### 2. Instalasi Library

Disarankan menggunakan \*\*TensorFlow versi 2.16.1\*\* agar kompatibel dengan model yang digunakan.

pip install tensorflow==2.16.1 streamlit pillow numpy pandas plotly



\### 3. Menjalankan Aplikasi



Aplikasi akan terbuka otomatis melalui browser.



---



\### 👨‍💻 Informasi Pengembang

Nama : Ferdy Rizal Mahendra Putra



NIM : 202210370311161



Mata Kuliah : Machine Learning C



Program Studi : Informatika



Universitas : Universitas Muhammadiyah Malang



📌 Repository ini dibuat untuk memenuhi Ujian Akhir Praktikum (UAP) Machine Learning.



