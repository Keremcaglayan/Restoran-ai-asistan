# YAPAY ZEKA TEMELLERİ - PROJE GÜNLÜĞÜ



**18.05.2026**

* **Ne yaptım?** Proje konusu olarak "Fine-dining restoranları için müşteri geri bildirimlerini analiz eden bir Sınıflandırma ve NLP asistanı" yapmaya karar verdim. Kaggle'dan "10000 Restaurant Reviews" adlı İngilizce veri setini bularak ilk incelemelerimi yaptım.



* **Hangi AI aracını / kaynağı kullandım?** Gemini asistanı ile beyin fırtınası yaparak NLP ve Sınıflandırma mimarisinin planlamasını yaptım.



* **Karşılaştığım sorun ve nasıl çözdüm?** Yönergedeki "çözümü siz yöneteceksiniz" kriterine uymak için veri setini yerelleştirme (Türkçeye çevirme) ihtiyacı hissettim.



* **Bir sonraki adım:** Python üzerinden bir makine çevirisi modeli kurarak verileri Türkçeleştirmek.





**18.05.2026**

* **Ne yaptım?** İngilizce veri setini Hugging Face `transformers` modelleriyle Türkçeye çevirmeyi denedim. Ancak çeviri süresinin yerel cihazımda (CPU) saatler süreceğini fark edince strateji değiştirerek doğrudan 60.000 satırlık, Türkçe puanlı müşteri yorumları içeren `yorumsepeti.csv` veri setini projeye dahil ettim.



* **Hangi AI aracını / kaynağı kullandım?** Hata ayıklama (debugging), kütüphane çakışmalarını çözme ve yeni csv dosyasının Pandas ile ilk analizi (shape, info, head) için Gemini desteği aldım.



* **Karşılaştığım sorun ve nasıl çözdüm?** Çeviri aşamasında Hugging Face'ten kaynaklı `404 Not Found` (yanlış repo ismi) ve `Unknown task translation` (kütüphane sürümü uyuşmazlığı) hataları aldım. Hazır `pipeline` yapısını bırakıp `AutoTokenizer` ile manuel kuruluma geçerek teknik sorunu aştım. Fakat 60 bin satırlık yerel veriyi bulmak projeyi hızlandırmak adına asıl çözüm oldu.



* **Bir sonraki adım:** Yeni veri setindeki hız, servis ve lezzet puanlarını tek bir sütunda toplayıp ortalamalarını alarak yorumları "Olumlu", "Olumsuz" veya "Nötr" olarak etiketlemek (Veri Ön İşleme).





**21.05.2026**

* **Ne yaptım?** Veri Ön İşleme (Data Preprocessing) adımını tamamladım. `yorumsepeti.csv` içindeki geçersiz (`-` gibi) karakterleri ve eksik yorumları temizledim. Hız, servis ve lezzet puanlarının ortalamasını alarak modeli eğiteceğim `Duygu` (Olumlu/Olumsuz/Nötr) hedef etiketini oluşturdum. Ardından TF-IDF yöntemi ile metinleri vektörize ettim ve model eğitimini gerçekleştirdim.



* **Hangi AI aracını / kaynağı kullandım?** Pandas ile veri temizleme, `to\\\\\\\_numeric(errors='coerce')` kullanımı ve TF-IDF parametreleri konusunda Gemini asistanından destek aldım.



* **Karşılaştığım sorun ve nasıl çözdüm?** Başlangıçta daha karmaşık ve gelişmiş bir yapı olduğunu düşünerek Random Forest modelini ana algoritma olarak seçmiştim. Ancak eğitim sonrasında elde edilen metrikleri titizlikle incelediğimde, TF-IDF ile vektörize edilmiş yüksek boyutlu ve seyrek (sparse) metin verilerinde doğrusal bir model olan Logistic Regression'ın (Accuracy: %86.03, F1-Score: %83.93) Random Forest'ı (Accuracy: %84.83, F1-Score: %81.09) geride bıraktığını fark ettim. Veri bilimi prensiplerine sadık kalarak, daha yüksek ve kararlı başarım gösteren Logistic Regression modelini Restoran asistanının şampiyon modeli (ana motoru) yapmaya karar verdim ve projeyi bu doğrultuda güncelledim.



* **Bir sonraki adım:** Sunum dosyasını ve GitHub `README.md` içeriğini Logistic Regression modelinin başarısına göre optimize ederek projeyi eksiksiz bir şekilde teslime hazır hale getirmek.







**22.05.2026**

* **Ne yaptım?** Projenin dokümantasyon sürecini ve paketlemesini tamamladım. README.md dosyasını ve `sunum.pdf` slaytlarını şampiyon modelimiz olan Logistic Regression'ın gerçek metriklerine (Accuracy: %86.03) göre baştan aşağı güncelledim. Ayrıca projeyi tam bir "asistan" formatına sokmak için modeli `joblib` kütüphanesi ile dışa aktardım.



* **Hangi AI aracını / kaynağı kullandım?** README ve markdown dokümantasyon formatlarını profesyonel bir endüstri standardına getirmek ve modeli dışa aktarma kodunu (deployment hazırlığı) yazmak için Gemini asistanından destek aldım.



* **Karşılaştığım sorun ve nasıl çözdüm?** Dokümantasyonda modelin neden değiştirildiğini savunurken sadece kod değil, veri bilimi felsefesini de (dengesiz verilerde TF-IDF \& doğrusal model uyumu) açıklamam gerekiyordu. Metriklerin şeffaf analizini detaylandırarak bu savunmayı dokümantasyona başarılı bir şekilde yansıttım.



* **Bir sonraki adım:** Dosyaları GitHub reposuna yüklemek.



**22.05.2026**

* **Ne yaptım?** Proje dosyalarını Git terminali aracılığıyla oluşturduğum açık kaynaklı GitHub reposuna yükledim. Kurulum (deployment) adımlarının farklı cihazlarda nasıl çalışacağını test ederek README dosyasının son kontrollerini yaptım.



* **Hangi AI aracını / kaynağı kullandım?** Temel Git komutları (`git init`, `git add`, `git commit`, `git push`) ve GitHub'a proje entegrasyonu ile README dosyasındaki link yönlendirmeleri konusunda Gemini desteği aldım.



* **Karşılaştığım sorun ve nasıl çözdüm?** GitHub yüklemesinden sonra README dosyasındaki "Nasıl Çalıştırılır" kısmını test ederken iki potansiyel hata fark ettim. Birincisi, `git clone` komutuna `.git` ile biten asıl repo adresi yerine web tarayıcı linkini eklemiştim. İkincisi ise `cd` komutunda klasör adını küçük harfle (`restoran-ai-asistan`) yazmıştım. Linux/macOS gibi büyük/küçük harf duyarlı (case-sensitive) işletim sistemlerinde bunun sorun çıkarabileceğini fark ederek, her iki terminal komutunu da mükemmel çalışacak şekilde güncelledim.



* **Bir sonraki adım:** Projeye ekleyebileceğim birkaç fikir düşünmek.





**27.05.2026**

* **Ne yaptım?** Projeyi sadece arka planda çalışan bir kod olmaktan çıkarıp, son kullanıcının (restoran yönetiminin) kullanabileceği interaktif bir web arayüzüne (Dashboard) dönüştürdüm. Şampiyon modelimi `Streamlit` kütüphanesi kullanarak fine-dining konseptine uygun bir web sayfasına bağladım.



* **Hangi AI aracını / kaynağı kullandım?** Streamlit kurulumu, CSS arayüz tasarımı entegrasyonu ve makine öğrenmesindeki "Polarity Clash" (Zıtlık Çakışması) problemini aşmak için hibrit bir Varlık Tabanlı Duygu Analizi (ABSA) algoritması geliştirmek konusunda Gemini asistanından destek aldım.



* **Karşılaştığım sorun ve nasıl çözdüm?** Arayüzü test ederken, "Yemek harikaydı ama servis berbattı" gibi çift zıt duygu barındıran (Polarity Clash) cümlelerde modelin bağlamı karıştırarak genel bir "Nötr" kararı verdiğini veya tek tarafa eğildiğini fark ettim. Bu sorunu çözmek için cümleyi zıtlık bağlaçlarından ("ama", "fakat" vb.) bölen ve Restoran departmanlarına göre (Lezzet, Servis, Ambiyans) kelime avı yapan yeni bir ayrıştırıcı fonksiyon yazdım. Artık asistanımız tek bir karar vermek yerine, her departman için ayrı ayrı (Örn: Lezzet: Olumlu, Servis: Olumsuz) raporlama yapabilen bir yönetim paneline dönüştü.



* **Bir sonraki adım:** Geliştirilen interaktif web arayüzü ile 1 Haziran'daki proje savunmasında jüriye canlı bir demo sunumu gerçekleştirmek.





