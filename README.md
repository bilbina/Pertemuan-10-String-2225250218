# Pertemuan 10 - String dan Pengolahan Teks

**Nama:** Bilbina Azizi Amarinova  
**NIM:** 2225250218  
**Kelas:** 3A  

## Tujuan

Mengolah dan menormalisasi data teks menggunakan string Python agar data menjadi lebih rapi, konsisten, dan mudah digunakan.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

Jika menggunakan Windows dan `python3` tidak tersedia, gunakan:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

Proses normalisasi data dilakukan dengan beberapa langkah:

1. Menerima input nama dan kode kelas dari pengguna.
2. Menghapus spasi yang tidak diperlukan pada awal dan akhir teks menggunakan `strip()`.
3. Menghilangkan spasi berlebih di antara kata menggunakan `split()` dan `join()`.
4. Mengubah nama menjadi format huruf kapital pada awal setiap kata menggunakan `title()`.
5. Mengambil huruf pertama dari setiap kata untuk membuat inisial nama.
6. Mengubah kode kelas menjadi huruf kapital menggunakan `upper()`.
7. Menghapus spasi pada kode kelas agar format kode menjadi lebih rapi.
8. Menampilkan hasil normalisasi nama, inisial, dan kode kelas.

## Test Case

| No. | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `  bilbina azizi amarinova  ` | `Bilbina Azizi Amarinova` | `Bilbina Azizi Amarinova` | Berhasil |
| 2 | `  bilbina   azizi   amarinova  ` | `Bilbina Azizi Amarinova` | `Bilbina Azizi Amarinova` | Berhasil |
| 3 | Kode kelas: ` 3a ` | `3A` | `3A` | Berhasil |

## Refleksi

Masalah teks yang ditemukan adalah adanya **spasi berlebih** pada data nama, baik di awal dan akhir teks maupun di antara kata. Masalah tersebut diperbaiki menggunakan `strip()` untuk menghapus spasi di awal dan akhir, serta `split()` dan `join()` untuk merapikan spasi di antara kata.

Saya juga memahami bahwa normalisasi teks penting agar data memiliki format yang konsisten dan lebih mudah diproses oleh program.