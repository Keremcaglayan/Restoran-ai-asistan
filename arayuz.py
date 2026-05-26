import streamlit as st
import joblib

# 1. Sayfa Ayarları ve Tarayıcı Sekmesi
st.set_page_config(page_title="Laperlao AI Asistan", page_icon="🍷", layout="centered")

# 2. Laperlao Fine-Dining Özel CSS Tasarımı
st.markdown("""
<style>
    .stApp { background-color: #121212; color: #E0E0E0; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-family: 'Georgia', serif; }
    .stButton>button { background-color: #D4AF37; color: #000000; font-weight: bold; border-radius: 8px; border: 1px solid #D4AF37; width: 100%; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #000000; color: #D4AF37; border: 1px solid #D4AF37; }
    .stTextArea textarea { border-color: #D4AF37; }
</style>
""", unsafe_allow_html=True)

st.title("Restoran Akıllı Asistanı 🍝")
st.markdown("### Çoklu Departman (ABSA) Analiz Sistemi")
st.write("Lütfen analiz etmek istediğiniz müşteri yorumunu aşağıya girin:")

# 3. Modeli Yükleme
@st.cache_resource
def load_model():
    model = joblib.load('C:\\Users\\Asus\\Desktop\\Restoran asistanı proje\\Restoran_Asistan_Modeli.pkl')
    vectorizer = joblib.load('C:\\Users\\Asus\\Desktop\\Restoran asistanı proje\\Restoran_Vectorizer.pkl')
    return model, vectorizer

# 4. Parçalayıcı (ABSA) Fonksiyonumuz
def detayli_absa_analizi(yorum, model, vectorizer):
    boluculer = [" ama ", " fakat ", " ancak ", " lakin ", " rağmen ", ",", ".", " ve ", " yalnız "]
    temiz_yorum = yorum.lower()
    for b in boluculer:
        temiz_yorum = temiz_yorum.replace(b, "|")
    parcalar = temiz_yorum.split("|")
    
    # Restoran Sözlükleri
    lezzet_sozlugu = ['lezzet', 'tat', 'yemek', 'risotto', 'pizza', 'et', 'şarap', 'sos', 'harika', 'müthiş', 'soğuk', 'sıcak']
    servis_sozlugu = ['garson', 'servis', 'hizmet', 'karşılama', 'bekledik', 'hız', 'tavır', 'kaba', 'yavaş']
    ambiyans_sozlugu = ['mekan', 'ortam', 'müzik', 'ambiyans', 'manzara', 'temizlik', 'şık']
    
    analiz_sonuclari = {}
    genel_parcalar = []
    
    for parca in parcalar:
        parca = parca.strip()
        if len(parca) < 3: continue
        
        # Hangi departmandan bahsediliyor?
        kategori = None
        if any(k in parca for k in lezzet_sozlugu): kategori = "Mutfak & Lezzet 🍽️"
        elif any(k in parca for k in servis_sozlugu): kategori = "Servis & Operasyon 🤵"
        elif any(k in parca for k in ambiyans_sozlugu): kategori = "Ambiyans & Temizlik ✨"
        
        # Sadece o minik parçayı yapay zekaya soruyoruz
        vektor = vectorizer.transform([parca])
        duygu = model.predict(vektor)[0]
        
        if kategori:
            analiz_sonuclari[kategori] = duygu
        else:
            genel_parcalar.append(duygu)
            
    # Eğer yorumda departman kelimesi geçmiyorsa ilk hissi genel olarak al
    if not analiz_sonuclari and genel_parcalar:
        analiz_sonuclari["Genel Değerlendirme 📝"] = genel_parcalar[0]
        
    return analiz_sonuclari

try:
    model, vectorizer = load_model()
    
    # 5. Arayüz Etkileşimi
    yorum = st.text_area("Müşteri Yorumu:", height=150, placeholder="Örn: Trüflü risotto harika müthişti ama garsonların bize karşı tavrı gerçekten berbattı.")
    
    if st.button("Detaylı Analiz Et"):
        if yorum.strip() == "":
            st.warning("Lütfen analiz edilecek bir yorum girin!")
        else:
            # ABSA fonksiyonunu çağır
            sonuclar = detayli_absa_analizi(yorum, model, vectorizer)
            
            st.markdown("---")
            st.markdown("### 📊 Departman Bazlı Analiz Sonuçları")
            
            # Sonuçları ekrana renkli şık kutular halinde basıyoruz
            for departman, duygu in sonuclar.items():
                if duygu == 'Olumlu':
                    renk = "#2e7d32" # Yeşil
                    ikon = "✅"
                elif duygu == 'Olumsuz':
                    renk = "#c62828" # Kırmızı
                    ikon = "❌"
                else:
                    renk = "#1565c0" # Mavi
                    ikon = "ℹ️"
                    
                # Kutucuk (Card) Tasarımı HTML Entegrasyonu
                st.markdown(f"""
                <div style="padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid {renk}; background-color: #1a1a1a;">
                    <h4 style="margin:0; color:{renk}; font-family: sans-serif;">{ikon} {departman}</h4>
                    <p style="margin:5px 0 0 0; font-size:18px;">Yapay Zeka Kararı: <b>{duygu}</b></p>
                </div>
                """, unsafe_allow_html=True)



# örn: Yemek berbat  ama garsonlar ve mekan  inanlımazdı 



                
except FileNotFoundError:
    st.error("Model dosyaları (pkl) bulunamadı! Lütfen Jupyter Notebook'taki son hücreyi çalıştırıp modeli dışa aktardığınızdan emin olun.")