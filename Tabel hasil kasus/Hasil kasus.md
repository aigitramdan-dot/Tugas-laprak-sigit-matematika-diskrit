# TABEL PENGUJIAN KASUS 

Tabel pengujian di bawah ini digunakan untuk menguji studi kasus tambahan dengan berbagai kombinasi kondisi `True` dan `False`.

## 1. Sistem Login (Username & Password) - AND

Logika `AND`: Login hanya berhasil jika username dan password keduanya diisi dengan benar (`True`).

| username_benar | password_benar | Hasil |
| :--- | :--- | :--- |
| True | True | Login berhasil |
| False | True | Login gagal |
| True | False | Login gagal |
| False | False | Login gagal |

## 2. Kelulusan Mahasiswa - AND

Logika `AND`: Mahasiswa hanya lulus jika nilai dan kehadiran keduanya memenuhi syarat (`True`).

| nilai_lulus | kehadiran_cukup | Hasil |
| :--- | :--- | :--- |
| True | True | Mahasiswa lulus |
| False | True | Mahasiswa tidak lulus |
| True | False | Mahasiswa tidak lulus |
| False | False | Mahasiswa tidak lulus |

---

## 3. Akses Perpustakaan - OR

Logika `OR`: Akses diberikan jika memiliki salah satu kartu atau keduanya (`True`).

| kartu_mahasiswa | kartu_perpustakaan | Hasil |
| :--- | :--- | :--- |
| True | True | Boleh masuk perpustakaan |
| False | True | Boleh masuk perpustakaan |
| True | False | Boleh masuk perpustakaan |
| False | False | Tidak boleh masuk perpustakaan |

## 4. Akses Sistem - OR

Logika `OR`: Akses diterima menggunakan password yang benar ATAU sidik jari yang cocok.

| password_benar | sidik_jari_cocok | Hasil |
| :--- | :--- | :--- |
| True | True | Akses diterima |
| False | True | Akses diterima |
| True | False | Akses diterima |
| False | False | Akses ditolak |

## 5. Nilai Tambahan - OR

Logika `OR`: Nilai tambahan didapat jika tugas selesai ATAU nilai ujian tinggi.

| tugas_selesai | nilai_ujian_tinggi | Hasil |
| :--- | :--- | :--- |
| True | True | Mendapat nilai tambahan |
| False | True | Mendapat nilai tambahan |
| True | False | Mendapat nilai tambahan |
| False | False | Tidak mendapat nilai tambahan |

---

## 6. Koneksi Internet - XOR

Logika `XOR`: Hanya boleh tepat satu koneksi yang aktif agar tidak terjadi bentrok.

| wifi_aktif | data_aktif | Hasil |
| :--- | :--- | :--- |
| True | True | Tidak tepat satu koneksi yang aktif |
| False | True | Satu koneksi internet aktif |
| True | False | Satu koneksi internet aktif |
| False | False | Tidak tepat satu koneksi yang aktif |

## 7. Pemilihan Kelas - XOR

Logika `XOR`: Mahasiswa harus memilih tepat satu kelas (pagi atau sore), tidak boleh keduanya atau tidak memilih sama sekali.

| kelas_pagi | kelas_sore | Hasil |
| :--- | :--- | :--- |
| True | True | Pilih salah satu kelas |
| False | True | Kelas berhasil dipilih |
| True | False | Kelas berhasil dipilih |
| False | False | Pilih salah satu kelas |

## 8. Metode Pembayaran - XOR

Logika `XOR`: Pembayaran hanya berhasil jika memilih satu metode (cash atau transfer).

| bayar_cash | bayar_transfer | Hasil |
| :--- | :--- | :--- |
| True | True | Pilih salah satu metode pembayaran |
| False | True | Pembayaran berhasil |
| True | False | Pembayaran berhasil |
| False | False | Pilih salah satu metode pembayaran |
