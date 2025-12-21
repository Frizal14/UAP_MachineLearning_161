\#🐟 Fish Classifier Pro

\### Dashboard Analisis Klasifikasi Citra Ikan (UAP Machine Learning)



\[!\[Streamlit App](https://static.streamlit.io/badges/streamlit\_badge\_svg.svg)](https://github.com/Frizal14/UAP\_MachineLearning\_161)

\[!\[TensorFlow 2.16.1](https://img.shields.io/badge/TensorFlow-2.16.1-orange.svg)](https://www.tensorflow.org/)

\[!\[Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)



\##📝 Deskripsi Proyek

\*\*Fish Classifier Pro\*\* adalah sistem klasifikasi citra berbasis \*Deep Learning\* yang dikembangkan untuk memenuhi \*\*Ujian Akhir Praktikum (UAP) Pembelajaran Mesin\*\*. Proyek ini bertujuan untuk mengklasifikasikan 5 jenis ikan secara otomatis menggunakan antarmuka web interaktif berbasis Streamlit.



Sistem ini membandingkan performa antara model yang dibangun dari awal (\*Custom CNN\*) dengan model \*Transfer Learning\* (\*VGG16\* dan \*MobileNetV2\*) untuk menganalisis efektivitas arsitektur terhadap dataset ikan.



---



\##📊 Dataset dan Preprocessing

Dataset yang digunakan bersumber dari Kaggle: \*\*\[My Fish Dataset](https://www.kaggle.com/datasets/srajangoyal1808/my-fish-dataset)\*\*.



\* \*\*Jumlah Data:\*\* > 5.000 citra (termasuk augmentasi).

\* \*\*Kelas (Label):\*\*

&nbsp;   1.  \*\*Archer Fish\*\* (Ikan Pemanah)

&nbsp;   2.  \*\*Betta Fish\*\* (Ikan Cupang)

&nbsp;   3.  \*\*Blue Tang\*\* (Dory)

&nbsp;   4.  \*\*Clown Sword Trigger Fish\*\*

&nbsp;   5.  \*\*Yellow Tang\*\*

\* \*\*Preprocessing:\*\*

&nbsp;   \* \*Resizing:\* Citra diubah ukurannya menjadi \*\*128x128 pixel\*\* (atau sesuaikan dengan input model Anda).

&nbsp;   \* \*Normalization:\* Nilai pixel dinormalisasi ke rentang \[0, 1].

&nbsp;   \* \*Augmentation:\* Random rotation, zoom, dan flip untuk memperbanyak variasi data latih.



---



\##🧠 Model yang Digunakan

Sesuai ketentuan UAP, proyek ini mengimplementasikan 3 model:



\###1. Custom CNN (Non-Pretrained)

Model \*Convolutional Neural Network\* yang dibangun dari awal (\*from scratch\*). Terdiri dari beberapa lapis \*Conv2D\*, \*MaxPooling\*, dan \*Dropout\* untuk mengekstraksi fitur ikan secara mandiri tanpa bobot bawaan.



\###2. VGG16 (Transfer Learning)

Menggunakan arsitektur VGG16 dengan bobot \*ImageNet\*. Layer atas (\*top layers\*) dibekukan (\*freeze\*), dan ditambahkan \*Dense Layer\* baru untuk klasifikasi 5 kelas ikan. Model ini dipilih karena kemampuannya menangkap fitur visual yang detail.



\###3. MobileNetV2 (Transfer Learning)

Menggunakan arsitektur MobileNetV2 yang dikenal ringan (\*lightweight\*) dan efisien. Sangat cocok untuk implementasi pada aplikasi web karena ukuran model yang kecil namun tetap memiliki akurasi tinggi.



---



\##📈 Hasil Evaluasi dan Analisis Perbandingan

Berikut adalah tabel perbandingan performa ketiga model berdasarkan pengujian pada data test:



| Model | Akurasi | Precision | Recall | F1-Score |

| :--- | :---: | :---: | :---: | :---: |

| \*\*Custom CNN\*\* | \*\*100%\*\* | 1.00 | 1.00 | 1.00 |

| \*\*MobileNetV2\*\* | \*\*97%\*\* | 0.97 | 0.97 | 0.97 |

| \*\*VGG16\*\* | \*\*92%\*\* | 0.92 | 0.92 | 0.92 |



\###🔍 Analisis Hasil

1\.  \*\*Custom CNN\*\*: Mencapai akurasi sempurna (100%) pada data uji, namun saat diuji coba pada data \*real-time\* (gambar baru dari internet), model ini terkadang salah memprediksi (misal: \*Betta Fish\*). Ini mengindikasikan adanya kecenderungan \*\*Overfitting\*\* karena model terlalu menghafal data latih.

2\.  \*\*MobileNetV2\*\*: Memberikan keseimbangan terbaik antara akurasi (97%) dan kecepatan. Model ini lebih stabil (Generalisasi baik) saat memprediksi gambar baru dibandingkan Custom CNN.

3\.  \*\*VGG16\*\*: Memiliki akurasi terendah (92%) di antara ketiganya, kemungkinan karena arsitekturnya yang terlalu kompleks untuk dataset yang relatif sederhana ini, atau memerlukan \*fine-tuning\* lebih lanjut.



> \*\*Kesimpulan:\*\* Untuk implementasi aplikasi, \*\*MobileNetV2\*\* adalah pilihan terbaik karena ringan dan memiliki generalisasi yang stabil.



\### Visualisasi Performa

| Confusion Matrix (CNN) | Grafik Training (CNN) |

| :---: | :---: |

| !\[Matrix CNN](Assets/images/cnn\_confusion\_matrix.png) | !\[Plot CNN](Assets/images/cnn\_plot.png) |



\*(Gambar visualisasi model lain dapat dilihat di folder `Assets/images`)\*



---



\##📂 Struktur Folder Proyek

Struktur direktori repository ini disusun sebagai berikut:

