Nama    : Cheryl Raynasya Adenan
NPM     : 2406437571
Kelas   : PBP A

Link    : https://cheryl-raynasya-foobakickz.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    = Dalam mengimplementasikan checklist pada tugas 2 ini, langkah-langkah yang saya lakukan adalah sebagai berikut:
    - Sebelum memulai, saya melakukan inisiasi repositori di GitHub dan menghubungkannya dengan repositori lokal untuk memastikan version control terkelola dengan baik.
    - Pertama, saya mengaktifkan virtual environment. Setelah itu, saya membuat aplikasi baru bernama main dengan perintah python manage.py startapp main, lalu mendaftarkannya ke dalam INSTALLED_APPS di settings.py agar aplikasi dapat dikenali oleh Django. 
    - Langkah berikutnya adalah melakukan routing. Saya menambahkan konfigurasi pada urls.py di proyek utama untuk mengarahkan request ke urls.py milik aplikasi main.
    - Kemudian, saya membuat model bernama Product di dalam models.py pada aplikasi main, dengan atribut-atribut yang telah ditentukan dalam tugas, seperti name, price, description, thumbnail, category, dan is_featured. Saya juga menambahkan beberapa atribut tambahan sesuai kebutuhan untuk melengkapi informasi produk. 
    - Kemudian, saya membuat fungsi pada views.py yang mengembalikan data berisi nama aplikasi serta identitas saya. Data tersebut ditampilkan melalui file template HTML yang saya buat dan isi, yaitu main.html. Fungsi di views.py kemudian dipetakan ke URL melalui urls.py di aplikasi main agar dapat diakses melalui browser. 
    - Setelah semua bagian dasar selesai, saya melakukan proses migrasi database untuk menyimpan struktur model ke dalam database menggunakan python manage.py makemigrations dilanjutkan dengan python manage.py migrate. 
    - Terakhir, saya melakukan deployment proyek ke PWS agar aplikasi dapat diakses secara online, dan membuat file README.md yang berisi link aplikasi sekaligus jawaban atas pertanyaan-pertanyaan refleksi.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    =   Berikut link bagan: ristek.link BaganRequestClientTI2
    
    Ketika browser mengirimkan HTTP request, Django akan memprosesnya melalui urls.py untuk mencocokkan pola URL dan memanggil view yang sesuai. Setelah itu, views.py akan menjalankan logika aplikasi, termasuk jika perlu berinteraksi dengan models.py untuk mengambil atau menyimpan data di database. Setelah data diperoleh, view akan meneruskannya ke template HTML untuk dirender menjadi halaman web. Hasil render kemudian dikirim kembali ke browser sebagai respons, sehingga pengguna dapat melihat tampilan sesuai dengan permintaan.

3. Jelaskan peran settings.py dalam proyek Django!

    = File settings.py adalah file konfigurasi utama untuk seluruh proyek Django. File ini berisi semua pengaturan tingkat proyek, yang mendefinisikan bagaimana proyek berjalan dan berinteraksi dengan komponen lain. Peran utamanya meliputi:
    - INSTALLED_APPS: Mendefinisikan daftar semua aplikasi Django yang aktif dalam proyek. Django hanya akan mengenali model, URL, dan template dari aplikasi yang terdaftar di sini.
    - DATABASES:  Berisi detail konfigurasi untuk koneksi ke satu atau lebih database. Di sinilah kita memberi tahu Django di mana data harus disimpan.
    - MIDDLEWARE: Daftar middleware yang memproses request dan response secara global. Ini digunakan untuk fungsionalitas seperti manajemen sesi, otentikasi, dan proteksi keamanan.
    - SECRET_KEY: Kunci kriptografi unik yang digunakan untuk keamanan, seperti proteksi sesi dan CSRF.
    - DEBUG: Sebuah flag boolean yang mengaktifkan atau menonaktifkan mode debug. Ketika True, Django akan menampilkan informasi debugging yang terperinci saat terjadi error.
    - STATIC_URL: URL dasar yang digunakan untuk menyajikan file-file statis dan file yang diunggah pengguna.

4. Bagaimana cara kerja migrasi database di Django?

    = Migrasi adalah sistem yang memungkinkan Django untuk mengelola perubahan skema database secara terstruktur dan terotomatisasi. Proses ini memastikan bahwa definisi model dalam kode (models.py) selalu sinkron dengan struktur tabel di database. Cara kerjanya terbagi dalam dua perintah utama:
    - python manage.py makemigrations. 
    Perintah ini mendeteksi perubahan yang dilakukan pada file models.py sejak migrasi terakhir dibuat. Django membandingkan kondisi models.py saat ini dengan file migrasi terakhir yang pernah dibuat. Jika ada perbedaan, Django akan menghasilkan sebuah file Python baru di dalam direktori migrations/. Outputnya, File migrasi ini berisi serangkaian operasi yang secara deskriptif menjelaskan perubahan skema yang harus dilakukan. File ini belum mengubah database.
    - python manage.py migrate.  
    Perintah ini menerapkan file-file migrasi yang belum dijalankan ke database. Django memeriksa file-file migrasi tersebut, menerjemahkan instruksi Python di dalamnya menjadi perintah SQL yang sesuai. Outputnya, perintah SQL tersebut dieksekusi pada database, sehingga skema database sekarang cocok dengan definisi di models.py.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    = Berikut alasan mengapa menurut saya framework Django cocok untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak:
    - Kelengkapan fitur built-in: 
    Django menyediakan banyak alat dan fitur siap pakai seperti sistem autentikasi pengguna, panel admin, dan ORM untuk mengelola database. Hal ini mempermudah pemula karena tidak perlu menyusun semua komponen dari awal.
    - Struktur terorganisir: 
    Framework Django memiliki pola pengembangan yang jelas dan teratur dengan pemisahan bagian logika data, tampilan, dan kontrol. Struktur tersebut mengajarkan cara membangun aplikasi dengan tata kelola kode yang baik.
    - Konsep dasar terjangkau: 
    Django memperkenalkan prinsip-prinsip inti pengembangan web seperti operasi CRUD (Create, Read, Update, Delete), manajemen routing, dan mekanisme keamanan dasar secara terintegrasi dan mudah dipelajari.
    - Bahasa Python yang mudah: 
    Menggunakan Python yang dikenal dengan sintaksnya yang mudah dipelajari, sehingga pemula dapat lebih berkonsentrasi pada konsep pengembangan perangkat lunak.
    - Dukungan dokumentasi: 
    Django didukung oleh dokumentasi resmi yang sangat terperinci, sehingga memudahkan pemula dalam mencari solusi dan pemahaman lebih lanjut.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? 

    = Menurut saya, tutorial 1 kemarin sangat membantu dalam mengerjakan tugas 2 saat ini. Penjelasannya cukup jelas dan langkah-langkahnya runtut, sehingga saya lebih mudah memahami alur kerja Django, mulai dari membuat project, app, hingga memahami konsep MVT. Tutorial tersebut juga memberi gambaran awal yang memudahkan saat saya mengimplementasikan model, view, dan template dalam tugas 2 ini.