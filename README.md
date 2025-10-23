🎬 YouTube View Bot
Akademik projeler ve tez çalışmaları için geliştirilmiş Python tabanlı YouTube görüntüleme botu

!(https://img.shields.io/badge/Python-3.8%252B-blue)
(https://img.shields.io/badge/Selenium-Automation-green)
(https://img.shields.io/badge/License-MIT-yellow)

✨ Özellikler
🤖 Akıllı Otomasyon - İnsan benzeri davranış simülasyonu

🔒 Proxy Desteği - Çoklu IP ile güvenli bağlantı

🛡️ Gizlilik Odaklı - Stealth mod ile tespit riski azaltılmıştır

📊 Detaylı İstatistik - Gerçek zamanlı performans takibi

⚡ Otomatik Yönetim - ChromeDriver otomatik güncelleme

🔄 Hata Toleranslı - Bağlantı sorunlarında otomatik kurtarma

🚀 Hızlı Başlangıç
Gereksinimler
bash
pip install selenium fake-useragent webdriver-manager requests
Temel Kullanım
bash
python youtube_bot.py
📖 Kullanım Kılavuzu
1. Proxy Ayarları
proxies.txt dosyası oluşturun:

text
http://proxy1:8080
http://kullanici:sifre@proxy2:3128
https://guvenli-proxy:443
45.76.102.33:3128
2. Bot'u Çalıştırma
python
from youtube_bot import YouTubeViewBot

bot = YouTubeViewBot()
bot.run_bot(
    youtube_url="https://youtube.com/watch?v=...",
    total_views=50,
    min_wait=30,
    max_wait=60,
    use_proxies=True
)
3. Interaktif Kullanım
text
🎬 YOUTUBE VIEW BOT
========================================
📹 YouTube URL: https://youtube.com/watch?v=...
🎯 Görüntüleme sayısı: 50
⏱️ Min bekleme (saniye): 30
⏱️ Max bekleme (saniye): 60
🔒 Proxy kullanılsın mı? (e/h): e
📊 Örnek Çıktı
text
🚀 YouTube View Bot Başlatılıyor...
🎯 Hedef: 50 görüntüleme

📊 Görüntüleme 1/50
🔌 Proxy kullanılıyor: http://192.168.1.1:8080
🎥 Video açılıyor...
⏳ 8.3s bekleniyor...
📺 45s izleniyor...
✅ Başarılı: 1/50

🎉 BOT ÇALIŞMASI TAMAMLANDI
✅ Başarılı görüntülemeler: 45
❌ Başarısız görüntülemeler: 5
📈 Başarı Oranı: 90.0%
🗂️ Dosya Yapısı
text
youtube-view-bot/
├── 📄 youtube_bot.py          # Ana bot dosyası
├── 🔧 proxy_tester.py         # Proxy test aracı
├── 🌐 proxies.txt            # Proxy listesi
├── ✅ working_proxies.txt    # Çalışan proxy'ler
└── 📋 requirements.txt       # Gereksinimler
⚙️ Gelişmiş Özellikler
Özelleştirilebilir Ayarlar
python
# Video izleme süreleri (saniye)
WATCH_TIME_MIN = 25
WATCH_TIME_MAX = 70

# Session arası bekleme (saniye)
WAIT_TIME_MIN = 30
WAIT_TIME_MAX = 90

# İnsan benzeri davranış ayarları
SCROLL_AMOUNTS = [100, 200, 300, 150]
INTERACTION_CHANCE = 0.3  # %30 etkileşim şansı
Proxy Test Aracı
Proxy'lerinizi test etmek için:

bash
python proxy_tester.py
❓ Sıkça Sorulan Sorular
🤔 Bot YouTube tarafından tespit edilir mi?
Bot, insan benzeri davranışlar sergileyerek ve proxy kullanarak tespit edilme riskini minimize eder, ancak %100 garanti verilemez.

🎯 Kaç görüntüleme güvenli?
Akademik çalışmalar için günde 50-100 görüntüleme makul kabul edilir. Büyük ölçekli kullanımlardan kaçının.

🔧 Proxy kullanmak zorunlu mu?
Hayır, proxy kullanmadan da çalışabilir ancak proxy kullanımı güvenliği artırır.

⚠️ Önemli Uyarılar
📢 DİKKAT: Bu proje sadece eğitim ve akademik araştırma amaçlıdır.

YouTube'un Hizmet Şartları'nı ihlal edebilir

Sorumluluk kullanıcıya aittir

Limitli kullanım önerilir

Aşırı kullanım hesap ban'ına sebep olabilir

Sadece kendi videolarınız üzerinde test yapın

🐛 Sorun Giderme
Sorun	Çözüm
ChromeDriver hatası	webdriver-manager otomatik çözer
Proxy bağlantı hatası	Proxy'leri test edin veya proxy'siz çalıştırın
SSL hataları	Kod otomatik olarak yönetir
Zaman aşımı	İnternet bağlantınızı kontrol edin
📄 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

🤝 Katkıda Bulunma
Fork edin

Feature branch oluşturun (git checkout -b feature/amazing-feature)

Commit edin (git commit -m 'Add amazing feature')

Push edin (git push origin feature/amazing-feature)

Pull Request oluşturun

<div align="center">
⚠️ UYARI: Bu bot sadece eğitim ve akademik araştırma amaçlıdır. Etik kullanım kullanıcının sorumluluğundadır.

</div>
