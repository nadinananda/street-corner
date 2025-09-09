Nama : Nadin Ananda 
NPM : 2406351806 
Kelas : PBP E 
Tautan menuju aplikasi : https://nadin-ananda-streetcorner.pbp.cs.ui.ac.id/ 
 
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Langkah pertama saya membuat repository baru di github sesuai dengan nama toko yang saya inginkan yaitu Street Corner. Setelah membuat repository baru di github, saya menghubungkan repositori lokal dengan repository github. Kemudian, masuk ke tahapan membuat sebuah proyek django baru. Pada tahap ini, saya menyiapkan segala dependencies yang berada di requirements.txt, kemudian startproject atau membuat proyek Django yang bernama Street Corner. 
    
Sebelum melanjutkan pembuatan direktori main dalam projek, saya melakukan konfigurasi environment variables dan proyek yaitu file .env, .env.prod, dan mengubah beberapa konfigurasi pada settings.py. Selanjutnya, saya membuat aplikasi main dengan perintah startapp main yang otomatis akan membuat direktori baru dan menambahkan ‘main’ pada INSTALLED_APPS di settings.py.
    
Langkah selanjutnya, saya membuat template html sederhana. Setelah membuat template HTML, saya mengisi file models.py sesuai dengan 6 atribut wajib. Setelah pembuatan model, saya melakukan migrasi model dengan perintah makemigrations lalu migrate. Kemudian untuk check list selanjutnya, saya membuat fungsi pada views.py yang akan mengembalikan ke HTML dan menampilkan nama, kelas, dan nama aplikasi. Selanjutnya, saya mengubah template html agar dapat menampilkan data yang telah diambil dari model.
    
Sebelum melakukan deployment ke PWS, saya membuat sebuah routing pada urls.py aplikasi main.    Kemudian saya juga melengkapi rute URL dengan menambahkan urls.py pada direktori proyek street corner. Proses ini dilakukan agar proyek dapat melakukan pemetaan ke rute URL pada aplikasi main. Langkah terakhir, saya melakukan deployment ke PWS dan menyimpan segala perubahan ke GitHub. 
    
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Link bagan : https://www.canva.com/design/DAGyfm3r2Y8/9DU7if84nIK3juuKonjRnA/edit?utm_content=DAGyfm3r2Y8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Alur: request → urls.py → views.py (query model) → models.py → database → return data to models.py → views.py (process data) → index.html (render template html) → response

Kaitan antara urls.py, views.py, models.py, dan berkas html adalah sebagai berikut: 
- urls.py (URL Configuration)
urls.py akan mendefinisikan pola URL dan memetakan setiap URL ke fungsi view tertentu di views.py. 
- views.py (Controller)
views.py dengan models.py
views.py akan mengimpor dan menggunakan class-class model dari models.py untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada database.

views.py dengan index.html
views.py merender template HTML dan mengirimkan data (context) ke template tersebut.

- models.py (Model)
Data dari models akan ditampilkan di HTML melalui perantara views. 

- Index.html (Template)
Menyajikan data yang dapat dilihat user. 

3. Jelaskan peran settings.py dalam proyek Django!

Peran settings.py dalam proyek Django adalah sebagai pusat konfigurasi untuk menyimpan semua pengaturan dalam aplikasi web. File ini berisi pengaturan seperti kunci keamanan, konfigurasi database, aplikasi yang terpasang, middleware, konfigurasi URL, template, serta pengaturan untuk file statis dan media (Supriyono, 2024). Berdasarkan pengerjaan tugas 1, terdapat beberapa perubahan dalam settings.py yaitu mendaftarkan aplikasi ‘main’ pada INSTALED_APPS, modifikasi file settings.py untuk menggunakan environment variables, mengubah isi ALLOWED_HOST sesuai dengan host dari server yang akan dijalankan, menambahkan konfigurasi PRODUCTION, dan mengubah konfigurasi database. 

4. Bagaimana cara kerja migrasi database di Django?

Cara kerja migrasi database di Django dimulai dari pemeriksaan apabila terjadi perubahan model pada file models.py. Kemudian, langkah selanjutnya adalah membuat file migrasi dengan perintah python manage.py makemigrations. Perintah ini bertujuan untuk menghasilkan file migrasi yang merepresentasikan perubahan pada model. Sebelum menerapkan migrasi, tinjau ulang isi file migrasi agar perubahan sesuai yang diinginkan. Langkah selanjutnya adalah melakukan migrasi ke database dengan perintah python manage.py migrate. Perintah ini akan menjalankan semua perubahan yang tercantum dalam file migrasi (UNMAHA, 2024). Django akan menyimpan status migrasi dalam tabel django_migrations di database dan menggunakan grafik migrasi untuk menjaga konsistensi serta mencegah konflik. 

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, karena framework Django mampu membantu kita lebih cepat menyelesaikan pekerjaan melalui ketersediaan API, library, hingga modul dalam satu paket. Selain itu,  framework ini bersifat open source, gratis tanpa biaya lisensi, dan dapat beroperasi di berbagai platform seperti Windows, Linux, dan MacOS. Hal tersebut akan terasa lebih mudah untuk dikombinasikan dengan teknologi lain. 
    
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Sebelumnya, saya ingin mengucapkan terima kasih banyak untuk kakak-kakak asdos yang telah membantu ketika ada kesulitan. Pada pengerjaan tugas 2 ini, saya sempat mengalami kendala yaitu status failed saat run di pws. Namun, berkat adanya forum faq pada discord, permasalahan saya jadi mudah diselesaikan. Tutorial 1 sudah sangat informatif dan mudah dipahami. Sebagai saran untuk ke depannya, mungkin dari segi tutorial bisa dibuat berupa check list seperti yang tertera pada tugas 2. 

Referensi : 
Tim Dosen PBP 2025. (2025b). SCELE Fakultas Ilmu Komputer Universitas Indonesia: Log in to the site. Ui.ac.id. https://scele.cs.ui.ac.id/pluginfile.php/269605/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf
Supriyono, E. (2024). Bagaimana Mengelola “settings” Pada Sebuah Proyek Berbasis Django. Kemenkeu.go.id. https://klc2.kemenkeu.go.id/kms/knowledge/bagaimana-mengelola-settings-pada-sebuah-proyek-berbasis-django-1e465638/detail/
UNMAHA. (2024, July). Migrasi Database Django: Langkah-langkah untuk Pengembangan. Blog | Universitas Mahakarya Asia | UNMAHA. https://blog.unmaha.ac.id/migrasi-database-django-langkah-langkah-yang-benar-untuk-pengembangan-tanpa-masalah/ 