🎬 YouTube View Bot
Akademik projeler ve tez çalışmaları için geliştirilmiş Python tabanlı YouTube görüntüleme botu.

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Selenium-Automation-green
https://img.shields.io/badge/License-MIT-yellow

✨ Özellikler
🤖 İnsan benzeri davranış simülasyonu

🔒 Proxy desteği (çoklu IP)

🛡️ Gizlilik odaklı (stealth mode)

📊 Detaylı istatistik ve loglama

⚡ Otomatik ChromeDriver yönetimi

🔄 Hata toleranslı bağlantı

🚀 Hızlı Kurulum
bash
# Gerekli kütüphaneleri yükleyin
pip install selenium fake-useragent webdriver-manager requests

# Bot'u çalıştırın
python youtube_bot.py
📖 Kullanım
Proxy dosyası oluşturun (proxies.txt):

text
http://proxy1:8080
http://user:pass@proxy2:3128
45.76.102.33:3128
Bot'u çalıştırın ve bilgileri girin:

text
🎬 YOUTUBE VIEW BOT
📹 YouTube URL: https://youtube.com/watch?v=...
🎯 Görüntüleme sayısı: 50
⏱️ Min bekleme: 30
⏱️ Max bekleme: 60
🔒 Proxy kullanılsın mı? (e/h): e
İzleme sürecini takip edin:

text
🚀 YouTube View Bot Başlatılıyor...
📊 Görüntüleme 1/50
🔌 Proxy kullanılıyor: http://192.168.1.1:8080
🎥 Video açılıyor...
⏳ 8.3s bekleniyor...
📺 45s izleniyor...
✅ Başarılı: 1/50
⚙️ Kod Örneği
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
🎯 Örnek Çıktı
text
🎉 BOT ÇALIŞMASI TAMAMLANDI
✅ Başarılı görüntülemeler: 45
❌ Başarısız görüntülemeler: 5
📈 Başarı Oranı: 90.0%
⚠️ Önemli Uyarılar
Sadece eğitim ve akademik araştırma amaçlıdır

YouTube ToS ihlal edilebilir

Sorumluluk kullanıcıya aittir

Limitli kullanım önerilir

Aşırı kullanım ban sebebi olabilir

🛠️ Dosya Yapısı
text
youtube-view-bot/
├── youtube_bot.py          # Ana bot dosyası
├── proxy_tester.py         # Proxy test aracı
├── proxies.txt            # Proxy listesi
└── working_proxies.txt    # Çalışan proxy'ler
📞 Destek
Sorularınız için Issue açabilirsiniz.

Not: Bu bot sadece eğitim ve bilimsel araştırma amaçlıdır. Etik kullanım kullanıcının sorumluluğundadır.

License: MIT License
