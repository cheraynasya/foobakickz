Nama    : Cheryl Raynasya Adenan
NPM     : 2406437571
Kelas   : PBP A

Link    : https://cheryl-raynasya-foobakickz.pbp.cs.ui.ac.id/

### PERTANYAAN TUGAS 2:
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

### PERTANYAAN TUGAS 3:
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
        - Langkah paling awal adalah merancang struktur data produk. Saya membuka main/models.py dan membuat kelas Product yang berisi semua field yang dibutuhkan, seperti name, price, description, stock, dan sebagainya. Saya juga menambahkan field tambahan seperti created_at yang otomatis menyimpan waktu saat data produk dibuat, serta views untuk menghitung jumlah orang yang sudah membuka detail produk tersebut. Selain itu, saya menambahkan sebuah method bernama increment_views yang berfungsi untuk menambah nilai pada field views setiap kali detail produk diakses. Setelah selesai mendefinisikan struktur datanya, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate agar tabel produk otomatis terbentuk di dalam database.

        - Agar pengguna bisa menambahkan data produk dengan lebih mudah, saya membuat sebuah ModelForm bernama ProductForm di file forms.py. Form ini secara otomatis mengikuti field yang sudah saya definisikan di model Product, sehingga tidak perlu lagi membuat form dari nol. Di dalam view create_product yang saya tulis di file views.py, saya memanggil ProductForm tersebut untuk menampilkan form sekaligus memproses data yang dikirim melalui metode POST. Jika data yang dimasukkan valid sesuai aturan form, maka objek produk baru akan disimpan ke database. Untuk bagian tampilan, saya menambahkan file create_product.html yang berisi form dengan {% csrf_token %} untuk keamanan. URL dengan path /create-product/ kemudian saya daftarkan ke dalam urls.py agar pengguna bisa mengakses halaman ini langsung dari browser.

        - Untuk halaman utama, saya membuat view show_main yang mengambil semua data produk dari database menggunakan Product.objects.all().  Data ini kemudian saya kirimkan ke template main.html. Di dalam template, saya menggunakan perulangan {% for product in products %} untuk menampilkan setiap produk, lengkap dengan tombol "Add Product" dan tombol "Detail" untuk setiap item. 

        - Untuk memenuhi kebutuhan data delivery, saya membuat empat endpoint baru di file views.py. Dua endpoint pertama (show_json dan show_xml) mengembalikan seluruh produk yang ada di database dalam format JSON dan XML menggunakan fungsi serializers.serialize dari Django. Dua endpoint berikutnya (show_json_by_id dan show_xml_by_id) juga melakukan hal yang sama tetapi hanya untuk satu produk tertentu berdasarkan ID yang diberikan. Supaya lebih aman, saya menggunakan filter() alih-alih get(), sehingga jika produk dengan ID tersebut tidak ditemukan maka server akan mengembalikan kode status 404. Semua endpoint ini kemudian saya daftarkan di file urls.py, masing-masing dengan alamat /json/, /xml/, /json/<int:id>/, dan /xml/<int:id>/.

        - Terakhir, saya membuat halaman detail untuk setiap produk. Di dalam view show_product, saya menggunakan get_object_or_404 untuk mengambil produk berdasarkan ID. Jika produk tersebut ada, maka method increment_views dijalankan untuk menambah jumlah view produk. Setelah itu, detail produk ditampilkan melalui template product_detail.html, yang berisi informasi lengkap seperti nama produk, harga, deskripsi, kategori, jumlah stok, jumlah views, hingga gambar jika ada. URL untuk halaman ini dibuat dinamis dengan pola product/<int:id>/, sehingga setiap produk bisa diakses secara individual. Dengan langkah ini, pengguna tidak hanya bisa melihat daftar produk, tetapi juga informasi detail dari masing-masing item.

    6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
        = Menurut saya, tutorial 2 kemarin membantu saya dalam memahami cara membuat form di Django serta menampilkan dan mengirim data dalam format XML dan JSON. Saya jadi lebih paham peran serializers, penggunaan csrf_token untuk keamanan, dan bagaimana mengambil data berdasarkan ID. Hal tersebut membuat saya lebih mudah memahami alur pengolahan data di Django dan menerapkannya langsung pada tugas 3 ini.


    Berikut ini link untuk screenshot hasil akses URL Postman: https://docs.google.com/document/d/167VLB9dLsno-KjxPCkMExkK_7tTaN3LtlrznhF0zwBU/edit?usp=sharing

### PERTANYAAN TUGAS 4:
        1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

            = Django AutenticationForm adalah  adalah sebuah form bawaan dari Django yang secara khusus dirancang untuk proses login pengguna. Form ini secara default memiliki dua field, yaitu username dan password. 
            
                Kelebihan: mudah dipakai (tinggal impor dan render), sudah menyediakan validasi kredensial, dan bekerja aman bersama middleware Django (mis. CSRF).

                Kekurangan: kurang fleksibel jika mau ubah cara login (mis. login pakai email) atau menambah logika validasi dasarnya, tampilan default-nya juga sangat dasar sehingga memerlukan penyesuaian CSS agar terlihat menarik dan sesuai dengan desain aplikasi.
        
        2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

            = Autentikasi (Authentication) adalah proses untuk memverifikasi identitas seseorang. Menjawab pertanyaan, "Siapa kamu?". Contohnya adalah saat memasukkan username dan password untuk login. Jika benar, sistem mengenali kamu sebagai pengguna yang sah.

            Otorisasi (Authorization) adalah proses untuk menentukan hak akses yang dimiliki oleh pengguna yang sudah terautentikasi. Menjawab pertanyaan, "Apa yang boleh kamu lakukan?". Contohnya, setelah login, hanya pengguna dengan status "admin" yang boleh menghapus produk, sedangkan pengguna biasa hanya bisa melihat.  
            
            Implementasi pada Django:

                Autentikasi: Django memiliki sistem autentikasi bawaan yang kuat (django.contrib.auth). Sistem ini menyediakan model User, form seperti AuthenticationForm dan UserCreationForm, serta view decorators seperti @login_required untuk memastikan hanya pengguna terautentikasi yang bisa mengakses halaman tertentu.

                Otorisasi: Django mengimplementasikan otorisasi melalui Permissions and Groups Framework. Kita bisa memberikan izin (misalnya, can_add_product, can_delete_product) kepada pengguna secara individu atau mengelompokkannya ke dalam groups (misalnya, "Admin", "Editor") yang memiliki izin tertentu.

        3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

            = Cookies:

                Kelebihan: Mudah dibuat dan diakses baik dari sisi server maupun client (JavaScript). Bisa diatur agar tetap tersimpan di browser pengguna bahkan setelah browser ditutup, cocok untuk fitur seperti "Ingat Saya".

                Kekurangan: Data disimpan di sisi client dalam bentuk teks biasa, sehingga rentan dimanipulasi atau dicuri (Cross-Site Scripting - XSS). Tidak cocok untuk menyimpan data sensitif. Ukuran cookie sangat terbatas (sekitar 4 KB). Cookies dikirimkan pada setiap HTTP request, yang bisa sedikit memperlambat komunikasi jika datanya besar.

            Session:

                Kelebihan: Data disimpan di sisi server. Browser hanya menyimpan session ID (sebuah token acak) di dalam cookie. Ini jauh lebih aman karena data sensitif tidak pernah meninggalkan server. Kapasitas penyimpanan jauh lebih besar dibandingkan cookies karena bergantung pada penyimpanan server.

                Kekurangan: Karena data disimpan di server, ini dapat memakan memori atau ruang database jika jumlah pengguna sangat banyak. Pengelolaannya sedikit lebih rumit dibandingkan cookies biasa (meskipun Django membuatnya sangat mudah).

        
        4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

            = Tidak, penggunaan cookies tidak otomatis aman secara default. Terdapat beberapa risiko, yaitu: 

            Cross-Site Scripting (XSS): Script jahat di sebuah situs dapat mencuri data dari cookies.

            Cross-Site Request Forgery (CSRF): Pengguna bisa ditipu untuk melakukan aksi di situs lain tanpa sepengetahuan mereka, dengan memanfaatkan cookies login mereka.

            Session Hijacking: Jika session ID dalam cookie dicuri (misalnya melalui jaringan Wi-Fi publik yang tidak aman), penyerang bisa mengambil alih sesi login pengguna.

            Cara Django menangani:
                CSRF Protection: Django memiliki middleware CSRF yang aktif secara default. Setiap request POST harus menyertakan CSRF token yang unik, mencegah serangan CSRF.

                HttpOnly Cookies: Untuk session ID dan CSRF token, Django secara default mengatur flag HttpOnly pada cookie. Ini mencegah cookie diakses melalui JavaScript, sehingga mitigasi risiko XSS.

                Secure Cookies: Django juga menyediakan pengaturan SESSION_COOKIE_SECURE = True yang akan memastikan cookie hanya dikirim melalui koneksi HTTPS, mencegah pencurian di jaringan yang tidak aman.

                Session Data Hashing: Data session di server ditandatangani secara kriptografis untuk mencegah manipulasi.
 
        5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
        
            = Langkah pertama yang saya lakukan adalah menghubungkan model Product dengan User. Saya memodifikasi main/models.py dengan menambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE, null=True). Penggunaan ForeignKey menciptakan hubungan many-to-one (satu pengguna bisa memiliki banyak produk). Opsi on_delete=models.CASCADE saya pilih agar semua produk yang terkait dengan seorang pengguna akan ikut terhapus jika pengguna tersebut dihapus, menjaga integritas data. Setelah memodifikasi model, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk menerapkan perubahan skema ini ke dalam database.

            Langkah kedua adalah mempersiapkan antarmuka pengguna (UI) untuk autentikasi. Saya membuat dua file template baru di dalam direktori main/templates/: register.html dan login.html. Template register.html dirancang untuk merender UserCreationForm dari Django, yang menyediakan field untuk membuat akun baru. Sementara itu, login.html digunakan untuk merender AuthenticationForm yang menangani proses login. Keduanya menggunakan tag {% csrf_token %} untuk keamanan dari serangan CSRF dan {{ form.as_table }} untuk menampilkan form dengan cepat dan terstruktur.

            Langkah ketiga, dan yang paling inti, adalah mengimplementasikan logika autentikasi pada main/views.py. Saya menambahkan tiga fungsi baru: register, login_user, dan logout_user. Fungsi register menangani validasi dan penyimpanan data dari UserCreationForm. Fungsi login_user memvalidasi kredensial pengguna melalui AuthenticationForm dan jika berhasil, fungsi ini akan memanggil login() dari Django untuk membuat sesi (session). Di sinilah saya mengimplementasikan penggunaan cookies dengan membuat HttpResponseRedirect dan menyisipkan cookie last_login berisi timestamp saat ini menggunakan response.set_cookie(). Fungsi logout_user memanggil logout() untuk menghapus sesi pengguna dan juga menghapus cookie last_login melalui response.delete_cookie(). Selain itu, saya memodifikasi fungsi yang sudah ada. Pada create_product, saya mengubah logikanya agar setiap produk baru secara otomatis terasosiasi dengan pengguna yang sedang login (product.user = request.user). Pada show_main, saya menambahkan decorator @login_required untuk memproteksi halaman, mengambil data last_login dari request.COOKIES, dan mengimplementasikan logika filter untuk menampilkan semua produk atau hanya produk milik pengguna yang sedang aktif.

            Langkah keempat, saya mengonfigurasi routing URL dan memperbarui template. Saya mendaftarkan path untuk /register/, /login/, dan /logout/ di dalam main/urls.py, menghubungkan setiap URL ke fungsi view yang telah dibuat. Selanjutnya, saya memperbarui main.html untuk menampilkan informasi pengguna secara dinamis ({{ name }} yang kini berisi request.user.username) dan waktu login terakhir ({{ last_login }}). Saya juga menambahkan tombol Logout serta tombol filter "All Products" dan "My Products". Pada template product_detail.html, saya menambahkan baris kode untuk menampilkan nama pembuat produk ({{ product.user.username }}).

            Langkah terakhir, saya membuat dua akun pengguna yang berbeda melalui halaman registrasi. Kemudian, saya login menggunakan masing-masing akun dan membuat tiga dummy data produk untuk setiap akun. Ini memastikan bahwa setiap produk memiliki pemilik yang jelas. Setelah itu, saya melakukan pengujian menyeluruh: memastikan halaman utama tidak bisa diakses sebelum login, memverifikasi bahwa cookie last_login muncul dan diperbarui setelah login, dan menguji fungsionalitas tombol filter "My Products" yang berhasil menampilkan produk sesuai dengan pengguna yang sedang login.

### PERTANYAAN TUGAS 5:
        1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

            = Ketika terdapat style yang bertentangan untuk satu elemen, browser akan mengikuti aturan Specificity (Spesifisitas). Urutan prioritas dari tertinggi ke terendah adalah:
            !important (Sebaiknya dihindari)

            Inline Styles (style="...")

            ID Selector (#id)

            Class Selector, Attribute Selector, Pseudo-class (.class, [attr], :hover)

            Element Selector dan Pseudo-element (p, div, ::after)

            Universal Selector (*)
        
        2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

            = Responsive Design adalah praktik memastikan layout web dapat menyesuaikan diri secara otomatis dan optimal di berbagai ukuran layar (dari smartphone hingga desktop).

            Mengapa Penting: Mayoritas pengguna mengakses web melalui ponsel, sehingga responsive design sangat penting untuk pengalaman pengguna (UX) yang baik dan SEO (mesin pencari memprioritaskan situs mobile-friendly).

            Contoh: Situs berita Google News (responsive) mengubah layout multi-kolom di desktop menjadi kolom tunggal di ponsel; sementara situs web lama (tidak responsive) akan memaksa pengguna untuk zoom dan scroll horizontal di ponsel.
        
        3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

            = Margin, border, dan padding adalah bagian dari box model:

            Padding: ruang di dalam elemen, antara konten dan border. Gunakan padding untuk memberi jarak antara teks/gambar dengan tepi kotak. Contoh: padding: 12px; atau Tailwind p-3.

            Border: garis yang mengelilingi kotak, berada di luar padding, sebelum margin. Digunakan untuk memberi garis tepi: border: 2px solid #ccc; atau Tailwind border-2 border-gray-300.

            Margin: ruang di luar border, memisahkan elemen dari elemen lain. Contoh: margin: 16px 0; atau Tailwind mt-4 mb-4.
        
        4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

            = Flexbox (Flexible Box): solusi untuk tata letak satu dimensi (satu baris atau satu kolom). Gunakan display: flex; lalu atur flex-direction, justify-content, align-items, flex-wrap. Flexbox sangat cocok untuk navbar, centering horizontal/vertikal, dan komponen yang butuh distribusi ruang adaptif. Contoh: membuat baris tombol yang rapi atau men-center konten di card.

            Grid Layout: solusi untuk tata letak dua dimensi (baris & kolom sekaligus). Gunakan display: grid; lalu grid-template-columns, grid-gap, grid-template-rows, grid-area. Grid cocok untuk layout halaman utama (catalog/galleries) yang butuh kontrol baris + kolom secara eksplisit.
            Keduanya saling melengkapi: gunakan flex untuk elemen internal (mis. tombol di card) dan grid untuk struktur utama (mis. grid produk 3 kolom di desktop, 1 kolom di HP). Di Tailwind kamu bisa memakai flex, justify-between, grid grid-cols-3 md:grid-cols-2 sm:grid-cols-1, dll.
        
        5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

            = Langkah pertama saya mengubah model dengan menghubungkan Product ke User (menambahkan user = ForeignKey(User, on_delete=models.CASCADE, null=True) di main/models.py) lalu menjalankan python manage.py makemigrations dan python manage.py migrate. saya menjelaskan bahwa awalnya pakai null=True supaya migrasi tidak memaksa default pada baris lama; setelah tabel bersih atau data lama ditangani, bisa diubah lagi jika mau non-nullable.

            Langkah kedua saya menambahkan fitur autentikasi: membuat view register menggunakan UserCreationForm, view login_user menggunakan AuthenticationForm + login() yang juga membuat cookie last_login, serta view logout_user yang memanggil logout() dan menghapus cookie last_login. saya daftarkan route register/, login/, dan logout/ di main/urls.py dan menyiapkan template register.html dan login.html yang sudah distyling dengan Tailwind.

            Langkah ketiga saya ubah view show_main supaya menerima filter (?filter=my vs all), mengambil last_login dari request.COOKIES.get('last_login', 'Never'), dan memasukkan npm, name, class ke context sehingga navbar dan halaman utama bisa menampilkan username, npm, kelas, dan last login. saya juga memasang decorator @login_required di view yang butuh proteksi sesuai kebutuhan (ingat kalau mau publik, jangan pasang decorator).

            Langkah keempat saya membuat fungsi create/edit/delete untuk product: create_product menyimpan product.user = request.user sebelum save(); edit_product menggunakan ProductForm(request.POST or None, instance=product) dan menyimpan perubahan jika valid; delete_product mengambil object dengan get_object_or_404 lalu .delete() dan redirect kembali ke daftar. semua route edit/delete ditambahkan di urls.py dan saya batasi tombol Edit/Delete di template agar hanya muncul jika user.is_authenticated and p.user == user.

            Langkah kelima saya menyiapkan dua akun dan dummy data. saya sarankan dua cara: membuat akun melalui form register di web lalu menambah tiga produk tiap akun, atau menggunakan Django shell (createsuperuser/create_user + Product.objects.create(...)) untuk langsung menambahkan enam dummy product. saya juga jelaskan cara menghapus dummy lewat shell (Product.objects.filter(user__username='user1').delete()).

            Langkah keenam saya mengimplementasikan cookies dan session: ketika berhasil login saya redirect menggunakan HttpResponseRedirect(reverse('main:show_main')) lalu response.set_cookie('last_login', str(datetime.now())); di logout saya response.delete_cookie('last_login'). pada halaman utama saya menampilkan Last login: {{ last_login }} dari context untuk memperlihatkan cookie tersebut.

            Langkah ketujuh saya melakukan styling dengan Tailwind: menambahkan CDN Tailwind dan link ke static/css/global.css di base.html, membuat global.css untuk aturan form kustom, dan mengubah template main.html, create_product.html, edit_product.html, product_detail.html, login.html, register.html menjadi responsif dan menarik menggunakan kelas Tailwind serta card grid untuk daftar produk. saya pastikan ada kondisi empty state yang menampilkan gambar no-product.png dan pesan kalau belum ada produk.

            Langkah kedelapan saya membuat navbar.html yang responsif: brand di kiri, menu di tengah untuk desktop, dan user info + npm + class + tombol Logout di kanan; untuk mobile saya buat tombol hamburger yang toggles menu (JS singkat) sehingga saat diklik muncul menu vertikal yang juga menampilkan username, npm, class, dan tombol logout. navbar ini di-include di base.html sehingga konsisten di semua halaman.

            Langkah kesembilan saya melakukan pengujian: jalankan python manage.py runserver, coba register dua akun, login masing-masing, buat 3 produk per akun, cek ?filter=my dan ?filter=all, pastikan tombol edit/delete hanya terlihat oleh pemilik, cek cookie last_login di DevTools, dan pastikan endpoint JSON/XML berfungsi bila diperlukan. jika ada error migrasi terkait field user non-nullable, saya sarankan tetap pakai null=True lalu bersihkan data sebelum mengubah ke non-nullable.