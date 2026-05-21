### Akıllı Restoran Asistanı: Doğal Dil İşleme Destekli Müşteri Geri Bildirim Sistemi



**Tek Cümlelik Özet:** fine-dining konsepti için geliştirilen, binlerce müşteri yorumunu Doğal Dil İşleme (NLP) ile analiz edip işletmenin karar alma süreçlerini hızlandıran bir yapay zeka duygu analizi (sentiment analysis) asistanıdır.



### 📌 Problem Tanımı



Fine-dining restoran konseptinde kusursuz müşteri memnuniyeti ve yüksek hizmet standartları işletmenin sürdürülebilirliği için kritik öneme sahiptir. Ancak, dijital platformlardan gelen binlerce metinsel müşteri yorumunun manuel olarak okunması, kategorize edilmesi ve bunlardan anlamlı çıkarımlar yapılması insan gücüyle mümkün değildir.



Bu projede amaç; gelen tüm geri bildirimleri anlık olarak analiz eden, yorumların duygu tonunu (olumlu/olumsuz/nötr) ayıran ve mutfak/servis operasyonlarına dair nokta atışı geri bildirimler sunan bir **Yapay Zeka Asistanı** geliştirmektir.



## 📊 Kullanılan Veri Seti



Projede gerçek müşteri deneyimlerini yansıtması amacıyla tamamen Türkçe olan, 60.242 satırlık geniş çaplı bir restoran yorum veri seti kullanılmıştır.



* **Veri Seti:** `yorumsepeti.csv` https://www.kaggle.com/datasets/dgknrsln/yorumsepeti



* **İçerik:** Hız, servis ve lezzet puanları (1-10 arası) ile birlikte müşterilerin metinsel yorumlarını içerir.



## 🧠 Kullanılan Model ve Yöntemler



Projede metin verilerini anlamlandırmak ve sınıflandırmak için aşağıdaki makine öğrenmesi adımları izlenmiştir:



1. **Veri Ön İşleme (Data Preprocessing):** Pandas kütüphanesi ile eksik/hatalı veriler temizlenmiş, hız, servis ve lezzet puanlarının ortalaması alınarak yorumlar "Olumlu" (>=7), "Nötr" (4-6) ve "Olumsuz" (<4) olarak etiketlenmiştir.
2. **Vektörizasyon (NLP):** Metinlerin matematiksel olarak ifade edilebilmesi için `TfidfVectorizer` (TF-IDF) yöntemi kullanılarak en sık geçen 5000 özellik çıkarılmıştır.
3. **Makine Öğrenmesi Modelleri:**



* &#x20;**Logistic Regression (Ana Model):** Yüksek boyutlu ve seyrek (sparse) metin verilerinde gösterdiği yüksek başarım nedeniyle projenin ana karar mekanizması olarak seçilmiştir.



* **Random Forest Classifier (Baseline Model):** Ağaç tabanlı algoritmaların metin üzerindeki performansını ölçmek ve karşılaştırma yapmak amacıyla kullanılmıştır.





## ⚙️ Nasıl Çalıştırılır (Kurulum Adımları)



Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu bilgisayarınıza klonlayın:

```bash
   git clone https://github.com/Keremcaglayan/Restoran-ai-asistan.git
   cd Restoran-ai-asistan
```



2.Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

3.Projeyi çalıştırmak için Jupyter Notebook dosyasını açın ve hücreleri sırasıyla çalıştırın:

```bash
jupyter notebook proje.ipynb
```







## 📈 Sonuçlar ve Performans Değerlendirmesi

Modelin performansı, verinin %20'lik test seti üzerinde değerlendirilmiştir. Yapılan eğitimler sonucunda, doğrusal (linear) bir model olan \*\*Logistic Regression\*\*, karmaşık ağaç tabanlı \*\*Random Forest\*\* modelini geride bırakarak Laperlao asistanının ana karar motoru olmuştur.



\*Ana Model (Logistic Regression)



\* Accuracy (Doğruluk): %85.34
\* F1-Score: %83.93



\* Karşılaştırma Modeli (Random Forest)



\* Accuracy (Doğruluk): %84.83
\* F1-Score: %81.09





Yüksek boyutlu TF-IDF metin vektörlerinde doğrusal modellerin daha başarılı olduğu bu sonuçlarla kanıtlanmıştır. Logistic Regression modelinin F1-Skorunun yüksek olması, asistanın özellikle "Olumsuz" şikayetleri kaçırmadan sınıf dengesizliklerine karşı dirençli bir analiz yapabildiğini göstermektedir.

(Not: Tahminlerin detaylı dağılımını gösteren `Confusion\_Matrix.png` dosyası repo içerisine eklenmiştir.)



## 🚀 Sınırlılıklar ve Geliştirme Önerileri



\*Sınırlılıklar: Eğitim verisi gerçek hayattan alındığı için çok fazla imla hatası, kısaltma ve argo içermektedir. Temel bir TF-IDF modeli, kelimelerin bağlamını (örneğin "kötü değil" cümlesindeki olumsuzluk ekinin olumlu anlam yaratmasını) yakalamakta zorlanabilmektedir. Ayrıca veri setindeki "Olumlu" yorumların sayısı, "Olumsuz" yorumlardan fazla olduğu için kısmi bir veri dengesizliği bulunmaktadır.


\* Geliştirme Önerileri: Gelecek versiyonlarda modelin bağlamı daha iyi anlaması için Hugging Face üzerinden önceden eğitilmiş Türkçe dil modelleri (örneğin BERTurk) kullanılarak \*fine-tuning\* işlemi yapılabilir. Ayrıca sistem Restoranın SQL veritabanına entegre edilerek, günlük yorumların anlık olarak bir arayüz (dashboard) üzerinden şeflere raporlanması sağlanabilir.





## 

