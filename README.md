# Depok Keebs
 
Link PWS: [Depok Keebs](http://rayhan-syahdira-depokkeebs.pbp.cs.ui.ac.id/)

<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

    
## **Pertanyaan 1**  
**Step-by-step implementasi checklist Tugas 2:**

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
</details>

<details>
 
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>

 
## **Pertanyaan 1**  
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform:**

Pengimplementasian sebuah platform memerlukan data delivery untuk mengirim data secara cepat antar komponen sistem. Data delivery memungkinkan monitoring analitik untuk membantu optimasi platform dan pengambilan keputusan berbasis data. Dalam platform dengan jumlah pengguna besar, data delivery yang efektif memungkinkan sistem untuk menangani traffic data tinggi.


## **Pertanyaan 2**  
**Menurutmu, mana yang lebih baik antara XML dan JSON serta mengapa JSON lebih populer dibandingkan XML:**

![XML vs JSON comparison](images/JSON_vs._XML.png)
Menurut saya, JSON mengungguli XML di beberapa bidang. Secara struktur dan ukuran, data JSON lebih compact dibanding XML, dan JSON lebih terintegrasi dengan berbagai bahasa pemrograman modern seperti JavaScript. Karena formatnya yang lebih sederhana, JSON lebih cepat diparsing daripada XML. Alasan-alasan tersebut cukup untuk membuat JSON lebih populer dibandingkan XML.


## **Pertanyaan 3**  
**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut:**

`form.is_valid()` digunakan untuk memeriksa apakah data yang dikirimkan melalui form memenuhi syarat validasi yang telah ditentukan. Fungsi ini akan mengembalikan nilai **True** jika semua data valid, dan **False** jika ada error atau data tidak valid. Django akan memeriksa setiap field dalam form sesuai dengan aturan validasi yang telah didefinisikan di model atau secara manual di form itu sendiri. Dalam konteks Depok Keebs, fungsi ini akan mengecek apakah form entry field seperti `name`, `price`, `description`, hingga `layout` telah memenuhi syarat validasi.


## **Pertanyaan 4**  
**Mengapa kita membutuhkan csrf_token saat membuat form di Django dan apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang:**

Kita membutuhkan `csrf_token` untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mencoba melakukan aksi yang tidak diinginkan atas nama pengguna yang sah tanpa sepengetahuan mereka. Setiap kali form HTML dikirimkan melalui metode POST, Django mengharapkan adanya `csrf_token` yang unik untuk sesi pengguna saat ini. Django kemudian memverifikasi bahwa token ini cocok dengan yang diharapkan untuk sesi pengguna tersebut. Jika token tidak cocok atau tidak ada, permintaan akan ditolak. 
Jika tidak menyertakan `csrf_token` dalam form Django, secara default Django akan memblokir semua permintaan POST dengan error **403 Forbidden**. Lalu, aplikasi akan menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan absennya `csrf_token` ini dengan membuat halaman berbahaya yang mengirimkan permintaan POST ke aplikasi web yang sah atas nama pengguna yang sedang login.


## **Mengakses URL dengan Postman**
![Postman xml](images/postman_xml.png)
![Postman xml id](images/postman_xml_id.png)
![Postman json](images/postman_json.png)
![Postman json id](images/postman_json_id.png)
</details>

<details>
 
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>

    
**Implementasi checklist Tugas 4:**

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial):**

1. Untuk membuat fungsi register, pertama tambahkan import `UserCreationForm` di `views.py` dan implementasi fungsi `register`
2. Tambahkan `register.html` di `main/templates` yang akan menjadi template untuk form register
3. Routing URL ke `urls.py` yang mengarah ke fungsi `register`
4. Untuk membuat fungsi login, tambahkan import `authenticate`, `login`, dan `AuthenticationForm` dan implementasi fungsi `login_user` di `views.py`
5. Tambahkan `login.html` di `main/templates` yang akan menjadi template form login
6. Sama dengan sebelumnya, routing URL ke `urls.py` yang mengarah ke fungsi `login_user`
7. Untuk membuat fungsi logout, tambahkan import `logout` dan implementasi fungsi `logout_user`
8. Buat tombol logout dengan menambahkan blok kode berikut di bawah hyperlink Add Product
   ```html
   <a href="{% url 'main:logout' %}">
   <button>Logout</button>
   </a>
   ```
9. Routing URL ke `urls.py` yang mengarah ke fungsi `logout_user`
10. Untuk membuat aplikasi memerlukan login sebelum menuju halaman main, import `login_required` dan tambahkan `@login_required(login_url='/login')` di baris atas fungsi `show_main` pada `views.py`
11. Sekarang, coba jalankan server dan melakukan register untuk membuat user baru. Kemudian, login dengan username dan password yang dibuat
12. Buat Product baru dengan Add New Product sebanyak 3 buah.
13. Untuk menghubungkan Product dengan User, import `User` ke `models.py` dan tambahkan variabel `user` dengan ForeignKey dengan `on_delete=models.CASCADE` (agar ketika user dihapus, Product bersangkutan akan terhapus juga) dalam `context`
14. Modifikasi fungsi `create_product_entry` di `views.py` untuk mencegah Django menyimpan objek Product yang telah dibuat ke dataabase, melainkan ke user
15. Dalam fungsi `show_main`, ubah variabel `product_entries` dari yang semula menampilkan semua objek dalam database menjadi difilter menurut user yang sedang aktif
16. Simpan perubahan dengan `makemigrations` dan `migrate`
17. Untuk menampilkan user yang sedang login dan menambahkan cookies seperti last login, tmbahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` di `views.py`
18. Ganti blok kode `login_user/if form.is_valid()` dengan:
    ```python
    if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
    ```
19. Dalam `context` di fungsi `show_main`, tambahkan variabel `last_login` dengan value `request.COOKIES['last_login']`
20. Tambahkan `response.delete_cookie('last_login')` di fungsi `logout_user` yang berfungsi untuk menghapus cookie last_login saat pengguna melakukan logout
21. Tunjukkan informasi last login dengan menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` setelah tombol logout pada `main.html`

    
## **Pertanyaan 1**
**Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**

`HttpResponseRedirect()` adalah kelas Django yang digunakan untuk membuat respons HTTP dengan kode status 302 (redirect). Saat menggunakan ini, kita harus memberikan URL tujuan secara eksplisit, baik dalam bentuk string URL lengkap atau menggunakan `reverse()` untuk mendapatkan URL dari nama rute. Fungsinya murni hanya untuk mengalihkan pengguna ke URL lain tanpa fitur tambahan.
`redirect()` adalah fungsi utilitas Django yang lebih sederhana dan fleksibel. Ini dapat menerima berbagai jenis argumen seperti URL, nama rute, atau objek model. Django akan secara otomatis menangani konversi argumen ini menjadi URL yang benar. `redirect()` adalah cara yang lebih umum digunakan karena lebih mudah dan memiliki kemampuan tambahan dibandingkan `HttpResponseRedirect()`.


## **Pertanyaan 2**
**Jelaskan cara kerja penghubungan model `Product` dengan `User`!**

Cara kerja penghubungan model Product dengan User di Django bekerja melalui konsep ForeignKey, yang memungkinkan satu entitas (dalam hal ini, Product) berelasi dengan satu entitas lainnya (User). Berikut cara kerjanya secara bertahap:
1. Pada model Product, kita menambahkan field user yang merupakan ForeignKey ke model User. Ini berarti setiap entri mood dihubungkan secara langsung ke satu pengguna.
2. Di dalam views, ketika pengguna mengirim form untuk membuat entri baru, kita tidak langsung menyimpan data ke database. Alih-alih, kita menahan proses simpan dengan `commit=False`, yang memungkinkan kita menambahkan informasi tambahan sebelum data disimpan ke database.
3. Ketika menampilkan data di halaman utama, kita hanya menampilkan Product yang dibuat oleh pengguna yang sedang login. Ini dilakukan dengan menggunakan metode `filter()`, di mana kita menyaring data Product yang user-nya sesuai dengan `request.user`.
Dengan menambahkan ForeignKey di model, mengisi field user saat menyimpan, dan menyaring data berdasarkan pengguna yang sedang login, Django secara otomatis mengelola hubungan antara MoodEntry dan User, sehingga setiap entri mood selalu terkait dengan pengguna yang membuatnya.


## **Pertanyaan 3**
**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication adalah proses verifikasi identitas pengguna, memastikan bahwa pengguna yang mencoba mengakses sistem adalah siapa yang mereka klaim. Di Django, autentikasi dilakukan saat pengguna login, di mana kredensial seperti username dan password diverifikasi dengan data yang tersimpan di database.
Authorization, di sisi lain, adalah proses yang mengatur apa yang dapat dilakukan pengguna setelah terautentikasi. Django menggunakan sistem permissions untuk mengontrol akses pengguna ke berbagai sumber daya atau fungsi dalam aplikasi. Misalnya, hanya pengguna tertentu yang dapat menambah atau mengedit data berdasarkan izin yang diberikan. Dekorator seperti `@login_required` dan `@permission_required` digunakan untuk membatasi akses berdasarkan status login atau izin spesifik yang dimiliki pengguna.


## **Pertanyaan 4**
**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django menyimpan status login pengguna dengan menggunakan session di server dan mengirimkan cookie sessionid ke browser pengguna untuk melacak session tersebut. Setiap kali pengguna mengunjungi halaman lain, cookie ini digunakan untuk mengidentifikasi session pengguna di server, sehingga Django dapat mengenali siapa yang sedang login. Selain untuk login, cookies juga berfungsi menyimpan preferensi pengguna dan untuk tujuan analitik, tetapi penggunaannya tidak selalu aman. Cookies rentan terhadap serangan seperti XSS atau pembajakan session, sehingga penting untuk mengaktifkan flag HttpOnly dan Secure guna memastikan cookies lebih aman.
</details>






