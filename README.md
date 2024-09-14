# Depok Keebs

Tugas 2 PBP GSL 2024/2025  
Link PWS: [Depok Keebs](http://rayhan-syahdira-depokkeebs.pbp.cs.ui.ac.id/)

## **Pertanyaan 1**  
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial):**

1. Saya membuat direktori lokal di laptop saya bernama `depok_keebs`.
2. Saya membuat repository di GitHub dengan nama yang sama, yaitu `depok_keebs`.
3. Saya menginisiasi direktori lokal dengan `git`, kemudian menambahkan remote repository `depok_keebs` agar terhubung dengan repository lokal.
4. Saya membuat file-file syarat seperti `.gitignore` dan `README.md`, kemudian menginstal dependencies.
5. Setelah memulai virtual environment, saya membuat project Django baru dengan `django-admin startproject depok_keebs .`.
6. Saya memulai app baru bernama `main` dengan `python manage.py startapp main`.
7. Saya meng-*include* aplikasi dan URL `main` pada `settings.py` dan `urls.py` di direktori project, setelah itu juga menambahkan URL pada level aplikasi `main`, sehingga Django bisa me-*handle* pola URL yang akan diberikan.
8. Saya membuat direktori `templates` di dalam direktori `main`, lalu membuat `main.html` yang berisi template data diri dan nama aplikasi untuk menampilkan layout page pada web PWS.
9. Saya membuat model `Product` dengan beberapa atribut, yaitu `name`, `price`, `description`, `category`, `connection_type`, dan `layout`.
10. Setelah `models.py` selesai dikerjakan, saya melakukan migrasi models.
11. Pada `views.py` dalam aplikasi `main`, saya mengimplementasikan fungsi untuk menampilkan template HTML.
12. Saya membuat project baru pada PWS lalu menambahkan git remote PWS pada direktori lokal saya.
13. Setelah direktori lokal selesai saya kerjakan, saya melakukan *commit* dan *push* perubahan ke GitHub repository `depok_keebs` dan juga PWS.
14. Project PWS selesai build, kemudian saya melengkapi `README.md` pada GitHub repository.

## **Pertanyaan 2**  
**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas HTML:**

1. User mengirim HTTP request ke PWS server yang diteruskan ke WSGI server.
2. WSGI server meneruskan ke Django.
3. Oleh `urls.py`, HTTP request dihubungkan ke `views.py`.
4. Selanjutnya, `views.py` memproses request dan *fetch* data dari `models.py`.
5. `views.py` mengirimkan response HTTP berupa template `main.html` kembali pada User.

![Bagan Alur Request dan Response Django](images/TUGAS%202%20DJANGO%20BAGAN.jpg)

## **Pertanyaan 3**  
**Jelaskan fungsi git dalam pengembangan perangkat lunak:**

Git berfungsi sebagai *version control* dalam pengembangan perangkat lunak. Dengan Git, kita dapat melacak setiap perubahan kode yang dilakukan, memudahkan proses kolaborasi, dan memungkinkan *rollback* ke versi sebelumnya jika terjadi kesalahan.

## **Pertanyaan 4**  
**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak:**

Dengan arsitektur *Model-View-Template (MVT)* yang terstruktur, framework ini membantu pemula memahami konsep dasar pengembangan web sambil mengajarkan praktik terbaik dalam hal keamanan, manajemen database, dan skalabilitas. Selain itu, komunitasnya yang besar juga menyediakan dukungan dan sumber daya yang melimpah terutama bagi mahasiswa yang memulai pembelajaran ini.

## **Pertanyaan 5**  
**Mengapa model pada Django disebut sebagai ORM:**

*Object-Relational Mapping* (ORM) adalah sebuah teknik untuk me-*convert* sebuah object menjadi object pada sistem lain. Models pada Django disebut sebagai ORM karena Django berperan sebagai interface antara object pada Python dengan tabel pada SQL. Ini memungkinkan pengembang untuk berinteraksi dengan database tanpa harus menulis query SQL secara eksplisit, melalui *QuerySet API* yang disediakan oleh Django.

## **Pertanyaan 6**  
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform:**

Pengimplementasian sebuah platform memerlukan data delivery untuk mengirim data secara cepat antar komponen sistem. Data delivery memungkinkan monitoring analitik untuk membantu optimasi platform dan pengambilan keputusan berbasis data. Dalam platform dengan jumlah pengguna besar, data delivery yang efektif memungkinkan sistem untuk menangani traffic data tinggi.

## **Pertanyaan 7**  
**Menurutmu, mana yang lebih baik antara XML dan JSON serta mengapa JSON lebih populer dibandingkan XML:**

![XML vs JSON comparison](images/JSON_vs._XML.png)
Menurut saya, JSON mengungguli XML di beberapa bidang. Secara struktur dan ukuran, data JSON lebih compact dibanding XML, dan JSON lebih terintegrasi dengan berbagai bahasa pemrograman modern seperti JavaScript. Karena formatnya yang lebih sederhana, JSON lebih cepat diparsing daripada XML. Alasan-alasan tersebut cukup untuk membuat JSON lebih populer dibandingkan XML.

## **Pertanyaan 8**  
**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut:**

`form.is_valid()` digunakan untuk memeriksa apakah data yang dikirimkan melalui form memenuhi syarat validasi yang telah ditentukan. Fungsi ini akan mengembalikan nilai **True** jika semua data valid, dan **False** jika ada error atau data tidak valid. Django akan memeriksa setiap field dalam form sesuai dengan aturan validasi yang telah didefinisikan di model atau secara manual di form itu sendiri. Dalam konteks Depok Keebs, fungsi ini akan mengecek apakah form entry field seperti `name`, `price`, `description`, hingga `layout` telah memenuhi syarat validasi.

## **Pertanyaan 9**  
**Mengapa kita membutuhkan csrf_token saat membuat form di Django dan apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang:**

Kita membutuhkan `csrf_token` untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mencoba melakukan aksi yang tidak diinginkan atas nama pengguna yang sah tanpa sepengetahuan mereka. Setiap kali form HTML dikirimkan melalui metode POST, Django mengharapkan adanya `csrf_token` yang unik untuk sesi pengguna saat ini. Django kemudian memverifikasi bahwa token ini cocok dengan yang diharapkan untuk sesi pengguna tersebut. Jika token tidak cocok atau tidak ada, permintaan akan ditolak. 

Jika tidak menyertakan `csrf_token` dalam form Django, secara default Django akan memblokir semua permintaan POST dengan error **403 Forbidden**. Lalu, aplikasi akan menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan absennya `csrf_token` ini dengan membuat halaman berbahaya yang mengirimkan permintaan POST ke aplikasi web yang sah atas nama pengguna yang sedang login.

