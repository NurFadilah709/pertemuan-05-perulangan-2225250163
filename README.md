# Pertemuan 05 – Perulangan

## Identitas

* **Nama:** Shofwatunnida
* **NIM:** 2225250074
* **Program Studi:** Pendidikan Matematika
* **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

1. Memahami penggunaan perulangan `for` dan `while` dalam Python.
2. Menerapkan perulangan untuk menyelesaikan permasalahan sederhana.
3. Menggunakan kondisi untuk mengontrol perulangan.
4. Melakukan pengujian program menggunakan beberapa kasus uji.

## Struktur Folder

```text
pertemuan-05-perulangaan-2225250074/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
└── kuis/
    └── kuis2_deret_aritmetika.py
```

## Daftar Latihan

### 1. Tabel Perkalian

Program menampilkan tabel perkalian dari bilangan yang dimasukkan pengguna menggunakan perulangan `for`.

### 2. Jumlah Bilangan

Program menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan `for`.

### 3. Validasi Input

Program memeriksa apakah nilai yang dimasukkan berada dalam rentang 0–100. Jika tidak valid, pengguna diminta memasukkan nilai kembali menggunakan `while`.

### 4. Menghitung Bilangan Genap

Program menghitung banyaknya bilangan genap dari 1 sampai n menggunakan perulangan `for` dan kondisi `if`.

## Kuis 2 – Deret Aritmetika

Program menghitung setiap suku dan jumlah deret aritmetika berdasarkan suku pertama, beda, dan banyak suku yang dimasukkan pengguna. Program menggunakan `while` untuk memvalidasi banyak suku agar bernilai positif dan `for` untuk menghitung deret secara bertahap.

## Cara Menjalankan

1. Buka folder tugas di Visual Studio Code.
2. Pilih file Python yang ingin dijalankan.
3. Klik **Run Python File**.
4. Masukkan input sesuai instruksi pada terminal.

## Hasil Pengujian

| Program               | Input                   | Hasil yang Diharapkan       |
| --------------------- | ----------------------- | --------------------------- |
| Tabel Perkalian       | n = 4                   | Tabel perkalian 4 dari 1–10 |
| Jumlah Bilangan       | n = 5                   | Jumlah = 15                 |
| Validasi Input        | 120, -5, 75             | Nilai diterima: 75          |
| Bilangan Genap        | n = 10                  | Banyak bilangan genap = 5   |
| Kuis Deret Aritmetika | a = 2, d = 3, n = 5     | Jumlah = 40.00              |
| Kuis Deret Aritmetika | a = 10, d = -2, n = 4   | Jumlah = 28.00              |
| Kuis Deret Aritmetika | a = 1.5, d = 0.5, n = 3 | Jumlah = 6.00               |

## Refleksi

Melalui praktikum ini, saya mempelajari penggunaan perulangan `for` dan `while` dalam bahasa Python. Saya memahami bahwa perulangan `for` dapat digunakan untuk mengulang proses dengan jumlah pengulangan tertentu, sedangkan `while` dapat digunakan untuk mengulang proses selama kondisi masih terpenuhi. Saya juga belajar menerapkan validasi input dan melakukan pengujian untuk memastikan program berjalan sesuai dengan yang diharapkan.
