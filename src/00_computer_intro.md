
Bab 0: Pengenalan Komputer
==========================

```{figure} _static/images/00_computer_intro.svg
:alt: Ilustrasi komputer.
:align: center

Ilustrasi komputer.
```

Sebelum melangkah ke dasar-dasar pengolah kata, ada baiknya untuk mempelajari cara mengoperasikan komputer dan
pengelolaan berkas terlebih dahulu. Komputer merupakan perangkat elektronik yang berfungsi mengolah data. Dengan 
menggunakan komputer, pekerjaan yang mulanya rumit, membosankan, memakan waktu, dan memerlukan banyak tenaga manusia 
kini menjadi semakin mudah, singkat, dan dapat dikerjakan oleh satu atau dua orang saja.

0.1. Menggunakan Keyboard
-------------------------

Keyboard merupakan perangkat keras yang digunakan untuk mengetik atau menjalankan perintah di komputer. Keyboard terdiri
dari tombol huruf, angka, tanda baca, dan tombol khusus yang memiliki fungsinya tersendiri. Di Indonesia, tata letak
keyboard yang digunakan adalah tata letak standar Amerika Serikat.

```{figure} _static/images/Keyboard.svg
:alt: Tata letak keyboard AS untuk PC, dengan ukuran penuh.

Tata letak keyboard AS untuk PC, dengan ukuran penuh.
```

Jika komputer kamu adalah sebuah Mac, baik itu MacBook, iMac, atau Mac mini, tata letak keyboard-nya sedikit berbeda 
dari yang di atas.

```{figure} _static/images/MacKeyboard.svg
:alt: Tata letak keyboard AS untuk Mac (Magic Keyboard biasa).

Tata letak keyboard AS untuk Mac (Magic Keyboard biasa).
```

### 0.1.1. Dasar-Dasar Keyboard

Untuk menggunakan keyboard :
1. **Tekan tombol huruf satu kali**, seperti tombol <kbd>A</kbd> untuk memasukkan huruf di depan kursor (berupa garis 
   tegak atau persegi di dalam kolom teks). Jika ditekan bersamaan dengan tombol <kbd>Shift</kbd>, huruf yang dimasukkan 
   menjadi huruf besar.
   ```{figure} _static/images/fig-00-01_press-a-key.svg
   :alt: Ilustrasi memasukkan huruf kecil dan kapital. Atas: menekan tombol A; Bawah: menekan tombol Shift dan A secara bersamaan
   
   Ilustrasi memasukkan huruf kecil (atas) dan huruf kapital (bawah)
   ```
2. **Tekan tombol angka maupun tanda baca satu kali** untuk memasukkan angka atau tanda baca yang dicetak di bawah
   tombol. Jika ditekan bersamaan dengan tombol <kbd>Shift</kbd>, kamu akan memasukkan tanda baca yang tercetak di 
   atasnya.
   ```{figure} _static/images/fig-00-02_press-a-number-key.svg
   :alt: Ilustrasi menekan tombol angka. Atas: menekan tombol 2; Bawah: menekan tombol Shift dan 2 secara bersamaan
   
   Ilustrasi memasukkan angka yang tercetak di bawah tombol (atas) dan tanda baca yang tercetak di atas tombol (bawah)
   ```
3. **Tekan tombol <kbd>Backspace</kbd>** (atau <kbd>delete</kbd> di keyboard Mac) untuk menghapus karakter di belakang 
   kursor. **Tekan tombol Delete** (atau tekan <kbd>Delete</kbd> bersama tombol <kbd>Fn</kbd>/<kbd>🌐</kbd> di keyboard
   Mac) untuk menghapus karakter di depan kursor. Tahan tombol untuk menghapus lebih banyak karakter.
   ```{figure} _static/images/fig-00-03_delete-characters.svg
   :alt: Ilustrasi menghapus karakter. Atas: menghapus karakter di belakang kursor dengan Backspace; Bawah: menghapus karakter di depan kursor dengan Delete/Del.
   
   Ilustrasi menghapus karakter di belakang kursor (atas) dan di depan kursor (bawah).
   ```
4. **Tekan tombol Enter atau Return** untuk memulai baris baru atau menyetujui apa yang baru kamu masukkan.
5. **Tekan dan tahan tombol Shift dan tekan tombol panah** untuk menyorot teks. Tahan tombol Ctrl atau Option untuk
   menyorot satu kata utuh. Mengetiklah untuk mengganti teks yang disorot. Tekan tombol Backspace untuk menghapusnya.

### 0.1.2. Menggunakan Pintasan

Kamu juga dapat melakukan lebih banyak hal di keyboard kamu, seperti menyalin teks, memotong teks, menempelkan teks, dan
sebagainya. Untuk melakukannya, kamu perlu menekan tombol Ctrl, Alt, dan/atau Shift (tombol Command, Option, dan/atau 
Shift di Mac), bersamaan dengan tombol tertentu. Teknik ini disebut sebagai pintasan (*keyboard shortcut*).

Pertama-tama, **kamu harus memahami notasinya.** Pintasan keyboard seringkali ditulis seperti "Ctrl + Shift + Z", yang
berarti "tekan dan tahan tombol Ctrl dan Shift, tekan Z, lalu lepaskan semuanya," atau "⌘A" yang berarti "tekan dan
tahan tombol berlambang ⌘, tekan A, lalu lepaskan semuanya."

Berikut ini adalah pintasan-pintasan keyboard yang sering digunakan :

|          Pintasan PC           |  Pintasan Mac  | Untuk                                                        |
|:------------------------------:|:--------------:|--------------------------------------------------------------|
| <kbd>Ctrl</kbd> + <kbd>C</kbd> | <kbd>⌘C</kbd>  | Menyalin teks yang disorot                                   |
| <kbd>Ctrl</kbd> + <kbd>X</kbd> | <kbd>⌘X</kbd>  | Memotong teks yang disorot (menyalin teks lalu menghapusnya) |
| <kbd>Ctrl</kbd> + <kbd>V</kbd> | <kbd>⌘V</kbd>  | Menempel (memasukkan) teks yang disalin/dipotong             |
| <kbd>Ctrl</kbd> + <kbd>A</kbd> | <kbd>⌘A</kbd>  | Menyorot semua teks di dalam kolom                           |
| <kbd>Ctrl</kbd> + <kbd>Z</kbd> | <kbd>⌘Z</kbd>  | Mengurungkan apa yang kamu ketik sebelumnya (tidak jadi)     |
| <kbd>Ctrl</kbd> + <kbd>Y</kbd> | <kbd>⌘⇧Z</kbd> | Mengembalikan apa yang kamu urungkan (jadi lagi)             |
| <kbd>Ctrl</kbd> + <kbd>O</kbd> | <kbd>⌘O</kbd>  | Membuka sebuah berkas atau dokumen                           |
| <kbd>Ctrl</kbd> + <kbd>S</kbd> | <kbd>⌘S</kbd>  | Menyimpan berkas atau dokumen yang sedang dikerjakan         |

```{admonition} Bagi Pengguna Mac
Jika kamu menggunakan keyboard PC di komputer Mac, tombol berlogo Windows berfungsi sebagai tombol Command, dan tombol
Alt berfungsi sebagai tombol Option.
```

0.2. Menggunakan Mouse
----------------------

Mouse adalah sebuah perangkat berbentuk menyerupai tikus yang digunakan untuk menggerakkan panah kursor di layar 
komputer. Panah kursor digunakan untuk berinteraksi dengan apa yang ada di layar komputer dengan mengekliknya (menunjuk
sesuatu dan menekan tombol mouse).

Perangkat yang memberi fungsi serupa adalah *trackpad*. *Trackpad* adalah permukaan yang sensitif terhadap sentuhan dan
pergerakan jari di atasnya. Karena praktis dan mudah digunakan, *trackpad* digunakan di hampir semua laptop (komputer 
lipat). 


0.?. Pengelolaan Berkas
-----------------------

Pengelolaan berkas adalah teknik dimana pengguna komputer mengorganisir berkas-berkas dan *folder* yang ada di
komputernya. Pengelolaan berkas meliputi membuat, memindahkan, menyalin, mengganti nama, dan menghapus berkas atau
*folder*. *Folder* adalah ibarat sebuah map yang berisi berkas dan/atau map lainnya.