Nama: RIKI AGIL SAPUTRA


NIM: 2225250026


Kelas: 3A
## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.
## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py
## Algoritma Tugas 3
loop luar memiliki peran untuk menajalankan kode program perulangan utama. Proses di dalam perulangan loop luar akan diatur oleh loop dalam. Seluruh hasil diperoleh akan diakumulasikan oleh akumulator dan proses perulangan yang terjadi akan dihitung oleh counter.
## Hasil Pengujian

# Dokumentasi Tugas

| No | Input | Keluaran yang Diharapkan | | | Keluaran Aktual | | | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | |
| 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | Sesuai |
| 2 | 2 | 4 | 9 | 3 | 4 | 9 | 3 | Sesuai |
| 3 | 3 | 9 | 36 | 5 | 9 | 36 | 5 | Sesuai |
| 4 | 4 | 16 | 100 | 12 | 16 | 100 | 12 | Sesuai |
| 5 | 5 | 25 | 225 | 16 | 25 | 225 | 16 | Sesuai |

## Analisis Efisiensi
badan loop dalam akan berjalan sebanyak range yang dimasukkan pada fungsi. jika kita memasukkan range dalam fungsi for misalkan for i in range (1, 5), maka badan loop akan berjalan sebanyak 4 kali dengan tidak memasukkan batas atas range yaitu 5.
## Refleksi
kesalahan yang saya temukan adalah bahwa saya meletakkan deklarasi variabel misalkan total_baris = 0 setelah loop dalam, sehingga hasilnya akan selalu kereset. Saya menanganinya dengan mengubah letak total_baris = 0 menjadi di awal.
## REFERENSI
Di dalam menyelesaikan tugas ini, saya menggunakan bantuan Ai Gemini untuk mengecek kode yang error dan membantu dalam membuat tabel di readme.