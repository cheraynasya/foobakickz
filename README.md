Nama    : Cheryl Raynasya Adenan
NPM     : 2406437571
Kelas   : PBP A

Link    : https://cheryl-raynasya-foobakickz.pbp.cs.ui.ac.id/

PERTANYAAN TUGAS 2:
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

PERTANYAAN TUGAS 3:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    
    = kita membutuhkan data delivery karena platform modern butuh cara yang efisien untuk berkomunikasi antara sisi pengguna (client) dan server.  Saat pengguna berinteraksi dengan aplikasi, mereka pasti ingin pengalaman yang cepat dan mulus tanpa harus memuat ulang seluruh halaman setiap kali mengklik sesuatu. Data delivery memungkinkan hal tersebut terjadi. Server bisa mengirimkan data mentah yang dibutuhkan saja, seperti daftar produk terbaru atau detail, dalam format ringan seperti JSON atau XML. Data ini kemudian diolah oleh browser untuk memperbarui sebagian kecil dari tampilan halaman secara asynchronous.  Tanpa data delivery, setiap interaksi kecil akan memaksa reload seluruh halaman, membuat aplikasi terasa lambat.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    
    = Menurut saya, sebagian besar pengembangan web modern saat ini, JSON jelas lebih baik dan lebih unggul daripada XML. Alasan utama JSON menjadi jauh lebih populer adalah karena ia lebih ringan, cepat, dan sangat mudah digunakan, terutama dalam aplikasi berbasis JavaScript. Sintaks JSON yang berupa key-value pair secara langsung cocok dengan struktur objek JavaScript, sehingga proses konversi data di sisi browser menjadi sangat sederhana.  Sebaliknya, XML lebih bertele-tele dengan tag pembuka dan penutupnya, yang membuatnya lebih besar ukurannya dan lebih lambat untuk diurai (parse). Meskipun XML punya keunggulan dalam hal validasi skema dokumen yang kompleks, untuk pertukaran data cepat di API web, kesederhanaan dan efisiensi JSON menjadikannya pilihan yang jauh lebih praktis.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    
    = Fungsi method is_valid() pada form Django adalah sebagai gerbang validasi untuk semua data yang dikirim oleh pengguna. Saat memanggil method ini pada sebuah objek form, Django akan secara otomatis menjalankan serangkaian pemeriksaan untuk memastikan data yang aman. Pemeriksaan ini mencakup validasi apakah kolom wajib sudah diisi, apakah tipe datanya sudah benar, dan apakah data tersebut mematuhi aturan lain yang sudah ditentukan. Method ini sangat dibutuhkan untuk menjaga integritas data di database. Tanpa is_valid(), bisa berisiko menyimpan data yang tidak lengkap, salah format, atau bahkan berbahaya, yang bisa menyebabkan bug dan celah keamanan pada aplikasi. 

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    
    = Penggunaan csrf_token pada form Django merupakan langkah keamanan untuk mencegah siber bernama Cross-Site Request Forgery (CSRF). csrf_token mencegah ini dengan menyisipkan sebuah kode rahasia unik yang disisipkan ke dalam form saat halaman dirender dan diverifikasi oleh server ketika menerima request POST. Server hanya akan memproses permintaan jika kode rahasia ini ada dan cocok, sesuatu yang tidak bisa ditebak atau dipalsukan oleh situs penyerang. Jika tidak ada token, penyerang bisa memanfaatkan sesi aktif pengguna untuk mengirim request berbahaya melalui situs atau skrip di domain lain. Dengan adanya verifikasi token, Django akan menolak request yang tidak sah sehingga risiko aksi berbahaya atas nama pengguna dapat dicegah.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    = 
    - Langkah paling awal adalah merancang struktur data produk sepatu. Saya membuka main/models.py dan membuat kelas Product yang berisi semua field yang dibutuhkan, seperti name, price, description, stock, dan sebagainya. Saya juga menambahkan field tambahan seperti created_at yang otomatis menyimpan waktu saat data produk dibuat, serta views untuk menghitung jumlah orang yang sudah membuka detail produk tersebut. Selain itu, saya menambahkan sebuah method bernama increment_views yang berfungsi untuk menambah nilai pada field views setiap kali detail produk diakses. Setelah selesai mendefinisikan struktur datanya, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate agar tabel produk otomatis terbentuk di dalam database.

    - Agar pengguna bisa menambahkan data produk dengan lebih mudah, saya membuat sebuah ModelForm bernama ProductForm di file forms.py. Form ini secara otomatis mengikuti field yang sudah saya definisikan di model Product, sehingga tidak perlu lagi membuat form dari nol. Di dalam view create_product yang saya tulis di file views.py, saya memanggil ProductForm tersebut untuk menampilkan form sekaligus memproses data yang dikirim melalui metode POST. Jika data yang dimasukkan valid sesuai aturan form, maka objek produk baru akan disimpan ke database. Untuk bagian tampilan, saya menambahkan file create_product.html yang berisi form dengan {% csrf_token %} untuk keamanan. URL dengan path /create-product/ kemudian saya daftarkan ke dalam urls.py agar pengguna bisa mengakses halaman ini langsung dari browser.

    - Untuk halaman utama, saya membuat view show_main yang mengambil semua data produk dari database menggunakan Product.objects.all().  Data ini kemudian saya kirimkan ke template main.html. Di dalam template, saya menggunakan perulangan {% for product in products %} untuk menampilkan setiap produk, lengkap dengan tombol "Add Product" dan tombol "Detail" untuk setiap item. 

    - Untuk memenuhi kebutuhan data delivery, saya membuat empat endpoint baru di file views.py. Dua endpoint pertama (show_json dan show_xml) mengembalikan seluruh produk yang ada di database dalam format JSON dan XML menggunakan fungsi serializers.serialize dari Django. Dua endpoint berikutnya (show_json_by_id dan show_xml_by_id) juga melakukan hal yang sama tetapi hanya untuk satu produk tertentu berdasarkan ID yang diberikan. Supaya lebih aman, saya menggunakan filter() alih-alih get(), sehingga jika produk dengan ID tersebut tidak ditemukan maka server akan mengembalikan kode status 404. Semua endpoint ini kemudian saya daftarkan di file urls.py, masing-masing dengan alamat /json/, /xml/, /json/<int:id>/, dan /xml/<int:id>/.

    - Terakhir, saya membuat halaman detail untuk setiap produk. Di dalam view show_product, saya menggunakan get_object_or_404 untuk mengambil produk berdasarkan ID. Jika produk tersebut ada, maka method increment_views dijalankan untuk menambah jumlah view produk. Setelah itu, detail produk ditampilkan melalui template product_detail.html, yang berisi informasi lengkap seperti nama produk, harga, deskripsi, kategori, jumlah stok, jumlah views, hingga gambar jika ada. URL untuk halaman ini dibuat dinamis dengan pola product/<int:id>/, sehingga setiap produk bisa diakses secara individual. Dengan langkah ini, pengguna tidak hanya bisa melihat daftar produk, tetapi juga informasi detail dari masing-masing item.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    = Menurut saya, tutorial 2 kemarin membantu saya dalam memahami cara membuat form di Django serta menampilkan dan mengirim data dalam format XML dan JSON. Saya jadi lebih paham peran serializers, penggunaan csrf_token untuk keamanan, dan bagaimana mengambil data berdasarkan ID. Hal tersebut membuat saya lebih mudah memahami alur pengolahan data di Django dan menerapkannya langsung pada tugas 3 ini.


Berikut ini link untuk screenshot hasil akses URL Postman: https://docs.google.com/document/d/167VLB9dLsno-KjxPCkMExkK_7tTaN3LtlrznhF0zwBU/edit?usp=sharing