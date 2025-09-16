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
Tag csrf_token pada form Django berfungsi untuk melindungi aplikasi dari serangan CSRF. CRSF atau Cross-Site Request Forgery dapat menyerang pengguna melalui tautan berupa SMS, email, atau obrolan (GeeksforGeeks, 2023). Tag tersebut bekerja dengan cara memverifikasi bahwa request POST berasal dari user yang sah. Apabila kita tidak menambahkan csrf_token, maka penyerang dapat memanfaatkan sesi pengguna untuk melakukan tindakan yang tidak sah. Penyerang dapat membuat formulir berbahaya di situs mereka sendiri, menipu pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi Django kita. Hal tersebut disebabkan karena permintaan POST akan tampak valid berkat cookie sesi yang terkirim bersamaan (GeeksforGeeks, 2023).

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
- Menambahkan beberapa fungsi baru di views.py seperti, create_product (redirect ke halaman form melalui tommbol Add) dan show_product (menampilkan halaman detail object)
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






