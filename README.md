# Nama : Nadin Ananda 
# NPM : 2406351806 
# Kelas : PBP E 
# Tautan menuju aplikasi : https://nadin-ananda-streetcorner.pbp.cs.ui.ac.id/ 
                                                                                                  
<p align="center">
  TUGAS 2
</p>

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) 
Langkah pertama saya membuat repository baru di github sesuai dengan nama toko yang saya inginkan yaitu Street Corner. Setelah membuat repository baru di github, saya menghubungkan repositori lokal dengan repository github. Kemudian, masuk ke tahapan membuat sebuah proyek django baru. Pada tahap ini, saya menyiapkan segala dependencies yang berada di requirements.txt, kemudian startproject atau membuat proyek Django yang bernama Street Corner. 

Sebelum melanjutkan pembuatan direktori main dalam projek, saya melakukan konfigurasi environment variables dan proyek yaitu file .env, .env.prod, dan mengubah beberapa konfigurasi pada settings.py. Selanjutnya, saya membuat aplikasi main dengan perintah startapp main yang otomatis akan membuat direktori baru dan menambahkan ‘main’ pada INSTALLED_APPS di settings.py.

Langkah selanjutnya, saya membuat template html sederhana. Setelah membuat template HTML, saya mengisi file models.py sesuai dengan 6 atribut wajib. Setelah pembuatan model, saya melakukan migrasi model dengan perintah makemigrations lalu migrate. Kemudian untuk check list selanjutnya, saya membuat fungsi pada views.py yang akan mengembalikan ke HTML dan menampilkan nama, kelas, dan nama aplikasi. Selanjutnya, saya mengubah template html agar dapat menampilkan data yang telah diambil dari model.

Sebelum melakukan deployment ke PWS, saya membuat sebuah routing pada urls.py aplikasi main. Kemudian saya juga melengkapi rute URL dengan menambahkan urls.py pada direktori proyek street corner. Proses ini dilakukan agar proyek dapat melakukan pemetaan ke rute URL pada aplikasi main. Langkah terakhir, saya melakukan deployment ke PWS dan menyimpan segala perubahan ke GitHub. 

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan](https://www.canva.com/design/DAGyfm3r2Y8/9DU7if84nIK3juuKonjRnA/edit)

Link bagan : https://www.canva.com/design/DAGyfm3r2Y8/9DU7if84nIK3juuKonjRnA/edit

Alur: request → urls.py → views.py (query model) → models.py → database → return data to models.py → views.py (process data) → index.html (render template html) → response

Kaitan antara urls.py, views.py, models.py, dan berkas html adalah sebagai berikut: 
- urls.py (URL Configuration)
    - urls.py akan mendefinisikan pola URL dan memetakan setiap URL ke fungsi view tertentu di views.py. 
- views.py (Controller)
    - views.py dengan models.py
        - views.py akan mengimpor dan menggunakan class-class model dari models.py untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada database.
    - views.py dengan index.html
        - views.py merender template HTML dan mengirimkan data (context) ke template tersebut.
- models.py (Model)
    - Data dari models akan ditampilkan di HTML melalui perantara views. 
- Index.html (Template)
    - Menyajikan data yang dapat dilihat user. 

## 3. Jelaskan peran settings.py dalam proyek Django!
Peran settings.py dalam proyek Django adalah sebagai pusat konfigurasi untuk menyimpan semua pengaturan dalam aplikasi web. File ini berisi pengaturan seperti kunci keamanan, konfigurasi database, aplikasi yang terpasang, middleware, konfigurasi URL, template, serta pengaturan untuk file statis dan media (Supriyono, 2024). Berdasarkan pengerjaan tugas 1, terdapat beberapa perubahan dalam settings.py yaitu mendaftarkan aplikasi ‘main’ pada INSTALED_APPS, modifikasi file settings.py untuk menggunakan environment variables, mengubah isi ALLOWED_HOST sesuai dengan host dari server yang akan dijalankan, menambahkan konfigurasi PRODUCTION, dan mengubah konfigurasi database. 

## 4. Bagaimana cara kerja migrasi database di Django?
Cara kerja migrasi database di Django dimulai dari pemeriksaan apabila terjadi perubahan model pada file models.py. Kemudian, langkah selanjutnya adalah membuat file migrasi dengan perintah python manage.py makemigrations. Perintah ini bertujuan untuk menghasilkan file migrasi yang merepresentasikan perubahan pada model. Sebelum menerapkan migrasi, tinjau ulang isi file migrasi agar perubahan sesuai yang diinginkan. Langkah selanjutnya adalah melakukan migrasi ke database dengan perintah python manage.py migrate. Perintah ini akan menjalankan semua perubahan yang tercantum dalam file migrasi (UNMAHA, 2024). Django akan menyimpan status migrasi dalam tabel django_migrations di database dan menggunakan grafik migrasi untuk menjaga konsistensi serta mencegah konflik.

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, karena framework Django mampu membantu kita lebih cepat menyelesaikan pekerjaan melalui ketersediaan API, library, hingga modul dalam satu paket. Selain itu,  framework ini bersifat open source, gratis tanpa biaya lisensi, dan dapat beroperasi di berbagai platform seperti Windows, Linux, dan MacOS. Hal tersebut akan terasa lebih mudah untuk dikombinasikan dengan teknologi lain. 

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Sebelumnya, saya ingin mengucapkan terima kasih banyak untuk kakak-kakak asdos yang telah membantu ketika ada kesulitan. Pada pengerjaan tugas 2 ini, saya sempat mengalami kendala yaitu status failed saat run di pws. Namun, berkat adanya forum faq pada discord, permasalahan saya jadi mudah diselesaikan. Tutorial 1 sudah sangat informatif dan mudah dipahami. Sebagai saran untuk ke depannya, mungkin dari segi tutorial bisa dibuat berupa check list seperti yang tertera pada tugas 2. 

## Referensi
1. Tim Dosen PBP 2025. (2025b). SCELE Fakultas Ilmu Komputer Universitas Indonesia: Log in to the site. Ui.ac.id. https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf

2. Supriyono, E. (2024). Bagaimana Mengelola “settings” Pada Sebuah Proyek Berbasis Django. Kemenkeu.go.id. https://klc2.kemenkeu.go.id/kms/knowledge/bagaimana-mengelola-settings-pada-sebuah-proyek-berbasis-django-1e465638/detail/

3. UNMAHA. (2024, July). Migrasi Database Django: Langkah-langkah untuk Pengembangan. Blog | Universitas Mahakarya Asia | UNMAHA. https://blog.unmaha.ac.id/migrasi-database-django-langkah-langkah-yang-benar-untuk-pengembangan-tanpa-masalah/ 

                                                    
<p align="center">
  TUGAS 3
</p>

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Suatu komunikasi web berlangsung melalui proses HTTP request dan response, di mana browser atau aplikasi klien akan request (HTML, CSS, JPG, JD, data dalam bentuk XML atau JSON). Oleh karena itu, disini kita memerlukan data delivery untuk *menjamin seluruh request yang masuk dapat dikirim dan diterima secara cepat, akurat, dan konsisten* (Walkowiak & Kamiński, 2017). Hal tersebut dapat mendukung performa dan pengalaman pengguna yang lebih lancar. Selain pengiriman yang cepat, kita juga dapat *memastikan integritas dan keamanan data saat berpindah dari server ke klien*. Adapun manfaat lain dari data delivery adalah *mendukung komunikasi asinkronus (AJAX)*. Prosesnya adalah melalui pengiriman data ke server tanpa harus reload seluruh halaman. Melalui cara ini, pengguna akan selalu berinteraksi dengan aplikasi sembari data baru dimuat di latar belakang (Joshi et al., 2010). Selain itu, data delivery juga *mendukung integrasi dengan API*. Hal tersebut memungkinkan pertukaran data secara terstruktur antara platform dengan layanan eksternal. Dengan demikian, mekanisme ini dapat membantu pembayaran, autentikasi, atau informasi pihak ketiga dapat berjalan lancar di dalam platform. 

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, XML akan lebih unggul jika kita menyimpan beberapa tipe data yang berbeda dengan banyak variabel. XML lebih efektif dalam mengidentifikasi kesalahan dalam data yang rumit karena fokusnya adalah menyimpan data dengan cara yang mudah dibaca oleh mesin (AWS, 2025). XML disarankan untuk dokumen kompleks yang membutuhkan pertukaran data. Di sisi lain, JSON dirancang khusus untuk pertukaran data dan menawarkan format yang lebih sederhana serta efisien (AWS, 2025). JSON juga meningkatkan kinerja dan kecepatan proses komunikasi. Dengan demikian, JSON lebih disarankan untuk digunakan dalam API, aplikasi seluler, dan penyimpanan data.

Alasan JSON lebih populer dibanding XML adalah sebagai berikut: 
- Struktur yang sesuai untuk sebagian besar skenario API(Wilde, 2020)
    - JSON sangat cocok digunakan di RESTful API, aplikasi web berbasis JavaScript/AJAX, aplikasi mobile, di mana interaksi antar client-server memerlukan kecepatan dan performa yang tinggi. JSON mendukung berbagai tipe data seperti objek, array, boolean, number sehingga sangat sesuai untuk pengolahan data di sisi klien. 
- Pemrosesan bahasa pemrograman yang lebih efisien
    - JSON merupakan format asli untuk data dalam aplikasi JavaScript (Safris, n.d.). JavaScript telah menyediakan parser JSON built-in yang langsung menghasilkan objek data. Hal tersebut membuat pekerjaan lebih cepat dan mudah. Di sisi lain, XML parsing cenderung lebih berat karena DOM atau library khusus (AWS, 2025). 
- Memiliki ukuran data yang kecil atau overhead lebih rendah
    - JSON memiliki struktur yang lebih padat, lebih mudah dibaca, dan mudah ditulis (tidak banyak tag pembuka dan penutup) (AWS, 2025). Selain itu, JSON memiliki atribut yang lebih sedikit jika dibanding atribut XML dan proses pengiriman data melalui jaringan yang membuat JSON lebih cepat dan hemat penggunaan bandwidth (AWS, 2025).

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi data/informasi yang dimasukkan oleh pengguna, menghasilkan cleaned_data jika data valid atau errors jika data tidak valid (Codex, 2023). Hal tersebut dapat memastikan data yang diproses aman dan sesuai format.
Pada contoh tugas 3, setelah pembuatan form di forms.py langkah selanjutnya adalah merender formulir. Pada proses ini ada proses validasi formulir sebagai berikut:

### function def add_product di views.py
```python
if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
```

Metode permintaan pada function di atas adalah POST. Jika formulir valid, maka data akan diproses dan menampilkan pesan sukses.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Tag csrf_token pada form Django berfungsi untuk melindungi aplikasi dari serangan CSRF. CSRF atau Cross-Site Request Forgery dapat menyerang pengguna melalui tautan berupa SMS, email, atau obrolan (GeeksforGeeks, 2023). Tag tersebut bekerja dengan cara memverifikasi bahwa request POST berasal dari user yang sah. Apabila kita tidak menambahkan csrf_token, maka penyerang dapat memanfaatkan sesi pengguna untuk melakukan tindakan yang tidak sah. Penyerang dapat membuat formulir berbahaya di situs mereka sendiri, menipu pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi Django kita. Hal tersebut disebabkan karena permintaan POST akan tampak valid berkat cookie sesi yang terkirim bersamaan (GeeksforGeeks, 2023).

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Langkah pertama saya membuat fungsi views baru dalam format XML, JSON, XML by ID, dan JSON by ID di file views.py yang ada di direktori main. 
- Import HttpResponse dan Serializers
    ``` from django.http import HttpResponse ```
    ``` from django.core import serializers ```
- Membuat fungsi def show_xml, show_json, show_xml_by_id, dan show_json_by_id

Pada setiap fungsi akan return HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML. Salah satu contoh fungsi show_xml adalah sebagai berikut 
    
```python
    def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")
```

Setelah membuat fungsi views, saya menambahkan routing url untuk masing - masing views di file urls.py pada direktori main
- Import masing - masing fungsi 
``` from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id ```
- Menambahkan path url di urlpatterns 

``` path('xml/', show_xml, name='show_xml'), ```
``` path('json/', show_json, name='show_json'), ```
``` path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'), ```
``` path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'), ```

Langkah selanjutnya adalah membuat halaman untuk menampilkan data objek model
- Membuat berkas forms.py di direktori main dan membuat class ProductForm yang akan menyimpan data dari objek product 
- Menambahkan beberapa fungsi baru di views.py seperti, add_product (redirect ke halaman form melalui tommbol Add) dan show_product (menampilkan halaman detail object)
- Menambahkan urlpatterns dari masing2 fungsi yang telah dibuat 
- Mengubah tampilan main.html di direktori main/templates menjadi tampilan data produk beserta tombol "Add Product" yang kemudian akan redirect ke halaman form 
- Membuat dua berkas html baru di main/templates untuk halaman form input (create_product) dan detail product (product_detail).

Langkah terakhir adalah menambahkan csrf di settings.py yang ada di direktori root project. 

``` python 
    CSRF_TRUSTED_ORIGINS = [
    "https://nadin-ananda-streetcorner.pbp.cs.ui.ac.id"
    ]
```

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Sebelumnya, saya ingin mengucapkan terima kasih banyak untuk kakak-kakak asdos yang telah membantu ketika ada kesulitan. Pada pengerjaan tugas 3 ini, saya merasa terbantu dengan adanya tutorial yang mudah untuk dipahami. Feedback dari saya adalah terkait dengan tutorial pembuatan html. Saya masih merasa kurang paham dengan setiap perubahan html yang diberikan. Oleh karena itu, saya memiliki saran jika ada perubahan di kode html dapat dijelaskan setiap bagiannya agar tidak merasa bingung saat pengerjannya. 

## Screenshot hasil akses URL ke Postman
https://drive.google.com/file/d/1rgIvZrqjAyMd1pDKvaC54ERlmjyOVNgl/view?usp=sharing

## Referensi 
1. AWS . (2025, September 10). JSON vs XML - Perbedaan Antara Berbagai Representasi Data - AWS. Amazon Web Services, Inc. https://aws.amazon.com/id/compare/the-difference-between-json-xml/

2. Joshi, P., Dr Chetan Dudhagar, & Kumar, D. B. (2010, December 1). Performance Evaluation in Server Side Scripting Using AJAX Technology. ResearchGate. https://www.researchgate.net/publication/345441266_Performance_Evaluation_in_Server_Side_Scripting_Using_AJAX_Technology/download

3. Safris, S. (n.d.). A Deep Look at JSON vs. XML, Part 1: The History of Each. Toptal Engineering Blog. https://www.toptal.com/web/json-vs-xml-part-1

4. Walkowiak, T., & Kamiński, W. (2017). Influence of Data Delivery on Availability of Web Systems. Procedia Engineering, 178, 223–232. https://doi.org/10.1016/j.proeng.2017.01.102

5. Wilde, E. (2020, November 11). Why JSON won over XML | Discover API formats on APIfriends. Axway Blog. https://blog.axway.com/learning-center/apis/api-management/why-json-won-over-xml

6. Codex, A. C. (2023, March 31). Working with Forms in Django. Reintech.io; Reintech. https://reintech.io/blog/working-with-forms-in-django-tutorial-for-software-developers

7. GeeksforGeeks. (2023, September 26). CSRF token in Django. GeeksforGeeks. https://www.geeksforgeeks.org/python/csrf-token-in-django/ 

<p align="center">
  TUGAS 4
</p>

## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
AuthenticationForm merupakan form bawaan Django yang terdapat pada modul ```django.contrib.auth.forms```.
Form tersebut berfungsi untuk melakukan autentikasi pengguna seperti login. AuthenticationForm menyediakan beberapa primary attributes default yaitu username, password, email, first_name, dan last_name (Django, 2025). 

Menurut (SuperTokens, 2024), kelebihan dari penggunaan AuthenticationForm adalah: 
- Tidak perlu membuat form autentikasi dari nol (built-in Django). 
- Keamanan sistem akan terjaga karena form telah mendapatkan dukungan resmi dari maintainer Django sehingga pembaruan keamanan dan kompatibilitas versi otomatis akan mengikuti sistem bawaan Django. 
- Hanya berfokus pada template dan alur login. Melalui form Django, kita bisa langsung memasangkan LoginView atau view lain bawaan Django. 

Di sisi lain, kekurangan dari penggunaan AuthenticationForm adalah: 
- Struktur form terbatas pada field yang sudah ditentukan. Apabila kita membutuhkan fitur lanjutan, maka perlu adanya integrasi atau sistem tambahan. Developer diharapkan bisa melakukan kustomisasi untuk memenuhi kebutuhan yang spesifik. 
- AuthenticationForm tidak dapat diintegrasikan dengan autentikasi eksternal. Contoh autentikasi eksternal seperti, OAuth, Google, Facebook, dan SSO. Apabila kita membutuhkan autentikasi eksternal, maka perlu adanya implementasi form dan backend yang lain. 

## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memverifikasi identitas pengguna. Biasanya autentikasi berfokus pada login, logout, credential (username & password), status aktif dan sesi pengguna. Proses ini diterapkan sebelum melakukan otorisasi. 

Otorisasi adalah proses memeriksa hak akses / izin setelah identitasnya diketahui. Proses ini berfokus pada hak ases spesifik dan berlangsung setelah proses autentikasi. Sistem akan mengecek permissions untuk menentukan aksi yang diizinkan. 

Django mengimplementasikan konsep autentikasi dan otorisasi di atas session framework. Hal ini tersedia melalui rangkaian model, views, forms, decorators, middleware, template variables, dan permission flags agar bisa diimplementasikan dengan mudah dan fleksibel. 

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Sessions: 
- Kelebihan:
    - Memiliki keamanan yang baik karena klien hanya menyimpan session ID sehingga data sensitif tidak ditampilkan pada browser. 
    - Memiliki kapasitas yang besar untuk menyimpan data yang kompleks.
    - Server dapat menghapus, mengubah, dan memutus session kapan saja (logout). 
- Kekurangan: 
    - Memerlukan ruang penyimpanan yang banyak di server. 
    - Session ID yang bocor dapat disalahgunakan (session hijacking).
    - Sangat bergantung pada cookie agar server mengetahui Session ID. 
Cookies: 
- Kelebihan: 
    - Persistent cookies, saat browser ditutup cookies dapat diatur agar tidak hilang.
    - Server bisa mengakses cookie langsung dari tiap request sehingga cocok untuk autentikasi atau state yang harus diketahui server.
- Kekurangan: 
    - Keamanan yang kurang karena jika cookies tidak dikonfigurasi dengan benar maka ada risiko terkena serangan CSRF.
    - Jika data cookies sangat besar, maka bisa memperbesar overhead jaringan.
    - Memiliki privasi dan kontrol karena pengguna dapat menghapus dan memanipulasi nilai cookie. 

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies tidak sepenuhnya aman secara default karena kelemahan cookies adalah data dapat diakses atau dimanipulasi oleh pengguna jika tidak diberi perlindungan tambahan. Selain itu, penggunaan cookies rawan terjadi target serangan XSS dan persistant cookie dapat dipakai untuk melacak aktivitas dalam jangka panjang. Dalam menangani kasus ini, Django secara default menyimpan data sesi di server (database atau cache) sehingga mengurangi risiko kebocoran data sensitif. Solusi lain dari Django adalah otomatis menyertakan middleware CSRF (django.middleware.csrf.CsrfViewMiddleware) untuk mencegah Cross Site Request Forgery. Hal lainnya adalah Django tidak menyimpan password mentah di model User dan menghasilkan SECRET_KEY secara acak saat membuat proyek baru untuk mengamankan data.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya

### Implementasi fungsi registrasi
    1. Modifikasi file views.py dengan import UserCreationForm dan messages
    2. Menambah fungsi register di views.py
    3. Membuat berkas html (registe.html)
    4. Menambahkan route url 
### Implementasi fungsi login 
    1. Modifikasi file views.py dengan import authenticate, login, dan AuthenticationForm 
    2. Menambah fungsi login_user di views.py
    3. Membuat berkas html baru (login.html)
    4. Menambah route login ke URL 
### Implementasi fungsi logout
    1. Modifikasi file views.py dengan import authenticate, login, dan logout
    2. Membuat fungsi logout_user di views.py
    3. Modifikasi file main.html dengan menambahkan button logout
    4. Menambah route logout ke URL 
### Melakukan restriksi akses halaman 
    1. Modifikasi file views.py dengan mengimport 
        ```from django.contrib.auth.decorators import login_required```
    2. Menambahkan potongan kode pada fungsi show_main dan show_product
        ```@login_required(login_url='/login')``` 
### Menggunakan data dari cookies 
    1. Modifikasi file views.py dengan mengimport HttpResponseRedirect, reverse, dan datetime
    2. Mengubah isi kode pada fungsi login_user di views.py untuk menyimpan cookie bernama last_login
    3. Menambah potongan kode last_login pada fungsi show_main
    4. Mengubah fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout.
    5. Menambahkan sesi terakhir pada main.html
### Menghubungkan model Product dengan User
    1. Menambahkan model baru yaitu user di models.py 
    2. Mengubah kode add_product di views.py
    3. Modifikasi fungsi show_main dengan filter yang diambil dari query parameter filter pada URL 
    4. Modifikasi main.html dan product_detail.html

## Referensi 
1. Django. (2025). Using the Django authentication system | Django documentation. Django Project. https://docs.djangoproject.com/en/5.2/topics/auth/default/

2. SuperTokens. (2024). A comprehensive guide to Django’s user authentication system. Supertokens.com; SuperTokens. https://supertokens.com/blog/django-user-authentication 

3. MDN. (2025, April 28). Django Tutorial Part 8: User authentication and permissions - Learn web development | MDN. MDN Web Docs. https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication 

<p align="center">
  TUGAS 5
</p>

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan dari prioritas tertinggi hingga tidak ada prioritas dalam pengambilan CSS selector adalah: 
- Origin & Importance, melihat sumber deklarasi yang ditentukan oleh !important
- Spesifisitas CSS: 
1. Inline styles, contoh: <h1 style="color: pink;"> 
2. ID Selector, contoh: #navbar
3. Classes, attribute selectors and pseudo-classes, contoh: .test, [type="text"], :hover
4. Elements and pseudo-elements, contoh: h1, ::before, ::after
5. Universal selector and :where(), contoh: *, where()
- Source Order, apabila spesifisitas sama, maka aturan yang muncul belakangan akan menimpa bagian awal
- Initial & Inherited Properties (default values), elemen memakai initial atau inherit dari parent sesuai dengan sifat propertiesnya.

Sumber: https://www.w3schools.com/css/css_specificity.asp, PPT PBP "06-Web Design Using HTML5 and CSS3"

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive layout merupakan suatu pendekatan untuk membuat halaman web dengan tata letak yang fleksibel, gambar yang fleksibel dan kueri media pada style sheet. Keuntungan dari responsive design adalah informasi yang disajikan dapat diterima pengguna dengan baik. Informasi yang bisa diakses pada desktop harus ditampilkan juga pada mobile begitupun sebaliknya sehingga pengguna tidak ada yang kehilangan informasi dan terlepas akses dari perangkat mobile apapun. 

Contoh aplikasi yang sudah menerapkan responsive design adalah Google Chrome. Menurut saya,Google Chrome telah menyajikan layar dan layout tampilan sesuai dengan device pengguna masing-masing. Hal tersebut membuat pengalaman pengguna tetap nyaman untuk mengakses browser baik itu dari tablet, desktop, maupun handphone. 

Sedangkan, berdasarkan pengalaman pribadi saya contoh aplikasi yang belum menerapkan responsive design adalah Microsoft Office seperti Word, PowerPoint, dan Excel. Menurut saya, ketiga aplikasi ini dari awal dikenal dengan fungsinya khusus untuk desktop. Walaupun, saat ini aplikasi tersebut sudah tersedia di PlayStore maupun AppStore, tetapi pengalaman pengguna yang disajikan saat berada di desktop dan di mobile itu sangat berbeda. Selain itu, contoh lainnya adalah software Figma. Menurut saya, tata letak figma jauh lebih baik diakses di desktop dibandingkan melihat design pada mobile yang sangat kecil. 

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding tergambar melalui Box Model pada CSS. Perbedaan antara margin, border, dan padding adalah sebagai berikut: 
- Content: isi elemen yang berisi teks atau gambar 
- Margin: ruang yang berada di luar border dimana margin akan memisahkan elemen dari elemen lain (transparan)
- Border: garis tepi yang akan membungkus padding + content
- Padding: ruang di dalam border yang mengelilingi content (transparan)
Cara implementasi untuk margin, border, dan padding adalah sebagai berikut: 
<!-- div {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
} -->
width = lebar konten (tidak harus menghitung padding dan border karena default box-sizing: content-box)
border = ada garis/stroke setebal 15px berwarna hijau yang akan mengelilingi content
padding = ada jarak antar konten dan garis border sebanyak 50px 
margin = ada ruang luar 20px yang mengeliingi content 

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box merupakan layout mode yang berada di CSS3. Sistem layout satu dimensi ini dirancang untuk mengatur elemen-elemen dalam satu baris atau kolom. Kegunaan dari flex box sendiri adalah membuat deisgn lebih responsive karena keunggulannya terletak dari segi fleksibilitas. Flex box mampu mengubah ukuran elemen sesuai dengan ruang yang tersedia. Contoh penggunaan flex box adalah menu navigasi atau isi formulir. 

Sedangkan, grid layout atau CSS Grid merupakan layout dua dimensi yang memungkinkan pengguna mengatur elemen baik secara horizontal maupun vertikal dalam sebuah kontainer. Kegunaan CSS Grid adalah membuat grid kompleks jadi lebih fleksibel dan mudah diatur sesuai kebutuhan design. CSS Grid akan berguna untuk membuat design halaman yang lebih terstruktur dan terorganisir. Contoh penggunaannya adalah halaman katalog, galeri, dashboard dll. 

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Implementasi fungsi untuk menghapus dan edit product
- Membuat fungsi edit_product dan delete_product di file views.py 
- Routing url patterns di urls.py untuk fungsi edit_product dan delete_product 

Menambah middleware WhiteNoise pada settings.py
Konfigurasi variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL

Membuat folder static dimana isinya adalah folder css yang berisi file global.css dan folder image untuk menyimpan gambar seperti no product dan logo

Kustomisasi navbar 
- Import {% load static %} untuk mengakses dan menambahkan image yang berada di folder static/image
- Menambahkan image logo di sebelah kiri judul aplikasi 
``` <img src="{% static 'image/logo.png' %}" class="h-10 w-10 object-contain" /> ```
- Mengubah tampilan logout menjadi stroke button di desktop dan mobile
- Menambah logo di sebelah Home and Add Product, icon di-import melalui sumber berikut dengan format <svg> https://lucide.dev/icons/circle-plus 
```<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-circle-plus-icon lucide-circle-plus"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="M12 8v8"/></svg>```

Kustomisasi main.html
- Fokus di grid product 
```<div class="grid grid-cols-1 md:grid-cols-2 gap-6">```
- Menampilkan no-product image ketika belum ada product yang tersimpan

Kustomisasi card_product.html
Sumber pembuatan card : https://www.material-tailwind.com/docs/html/card#blog-card
- Menambah gradient pada thumbnail image
```<div class="absolute inset-0 bg-gradient-to-t from-white via-transparent to-transparent opacity-60"></div>```
- Custom category badge dibawah image 
- Menampilkan nama produk, price, dan description product
- Menambah footer card seperti author product, button read more, edit, dan delete

Kustomisasi warna pada file html create_product, edit_product, login, dan register
```<button type="submit" class="order-1 sm:order-2 flex-1 text-white px-6 py-3 rounded-md font-medium transition-colors" style="background-color: #8BC34A;">```

Kustomisasi product_detail.html
- Custom button edit dan delete 
{% raw %}
{% if user.is_authenticated and product.user == user %}
    <div class="px-6 sm:px-8 py-8">
        <div class="flex items-center gap-3">
            <a href="{% url 'main:edit_product' product.id %}" class="inline-flex items-center px-4 py-2 text-white rounded-md font-medium transition-colors" style="background-color: #8BC34A;">
                Edit Product
            </a>
            <a href="{% url 'main:delete_product' product.id %}" class="inline-flex items-center px-4 py-1.5 border-2 rounded-md font-medium transition-colors" style="border-color: #FFC107; color: #FFC107;">
                Delete Product
            </a>
        </div>
    </div>
{% endif %}
{% endraw %}

## Referensi 
1. https://stackoverflow.com/questions/25105736/what-is-the-order-of-precedence-for-css 
2. https://www.w3schools.com/css/css_specificity.asp
3. https://www.w3schools.com/css/css_boxmodel.asp
4. https://dibimbing.id/blog/detail/memahami-penggunaan-css-grid-dan-flexbox
5. https://www.dicoding.com/blog/dasar-tampilan-responsif-pada-website/ 




