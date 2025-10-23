🎬 YOUTUBE VIEW BOT

Akademik projeler ve tez çalışmaları için geliştirilmiş Python tabanlı YouTube görüntüleme botu

![](https://img.shields.io/badge/Python-3.8%252B-blue)
![](https://img.shields.io/badge/Selenium-Automation-green)
![](https://img.shields.io/badge/License-MIT-yellow)

# ✨ **Özellikler**

🤖 **Akıllı Otomasyon** — _İnsan benzeri davranışlar sergileyerek doğal kullanım simülasyonu sağlar_  
🔒 **Proxy Desteği** — _Çoklu IP kullanarak güvenli bağlantı sağlar_  
🛡️ **Gizlilik Odaklı** — _Stealth mod sayesinde tespit riski en aza indirilmiştir_  
📊 **Detaylı İstatistikler** — _Gerçek zamanlı performans takibi sunar_  
⚡ **Otomatik Yönetim** — _ChromeDriver otomatik güncellenir_  
🔄 **Hata Toleranslı** — _Bağlantı sorunlarında otomatik kurtarma sağlar_

---

## 🚀 **Hızlı Başlangıç**

### ⚙️ Gereksinimler
```bash
pip install selenium fake-useragent webdriver-manager requests
```
```bash
▶️ Temel Kullanım
python youtube_bot.py
```
```bash
📖 Kullanım Kılavuzu
🔧 1. Proxy Ayarları

proxies.txt adlı dosyayı oluşturun:

http://proxy1:8080
http://kullanici:sifre@proxy2:3128
https://guvenli-proxy:443
45.76.102.33:3128

▶️ 2. Bot'u Çalıştırma
from youtube_bot import YouTubeViewBot

bot = YouTubeViewBot()
bot.run_bot(
    youtube_url="https://youtube.com/watch?v=...",
    total_views=50,
    min_wait=30,
    max_wait=60,
    use_proxies=True
)
```

💬 3. Etkileşimli Kullanım
========================================
📹 YouTube URL: https://youtube.com/watch?v=...
🎯 Görüntüleme Sayısı: 50
⏱️ Minimum Bekleme (sn): 30
⏱️ Maksimum Bekleme (sn): 60
🔒 Proxy kullanılsın mı? (e/h): e

📊 Örnek Çıktı
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
youtube-view-bot/
├── 📄 youtube_bot.py          # Ana bot dosyası
├── 🔧 proxy_tester.py         # Proxy test aracı
├── 🌐 proxies.txt            # Proxy listesi
├── ✅ working_proxies.txt    # Çalışan proxy'ler
└── 📋 requirements.txt       # Gereksinimler
```bash

⚙️ Gelişmiş Ayarlar
# Video izleme süresi (saniye)
WATCH_TIME_MIN = 25
WATCH_TIME_MAX = 70

# Oturum arası bekleme süresi (saniye)
WAIT_TIME_MIN = 30
WAIT_TIME_MAX = 90

# İnsan benzeri davranışlar
SCROLL_AMOUNTS = [100, 200, 300, 150]
INTERACTION_CHANCE = 0.3  # %30 etkileşim şansı
```
🌐 Proxy Test Aracı

Proxy'lerinizi test etmek için:

python proxy_tester.py

❓ Sıkça Sorulan Sorular

🤔 YouTube botu tespit eder mi?
Bot, insan benzeri davranışlar sergileyip proxy kullandığı için tespit riski düşüktür; ancak %100 garanti verilemez.

🎯 Kaç görüntüleme güvenli?
Eğitim veya test amaçlı günde 50–100 görüntüleme önerilir.

🔧 Proxy zorunlu mu?
Hayır, ama proxy kullanımı gizlilik ve güvenliği artırır.
<div align="center">

⚠️ Önemli Uyarı

📢 UYARI:
Bu proje yalnızca eğitim ve akademik araştırma amaçlıdır.
Kullanımı, YouTube Hizmet Şartlarını ihlal edebilir.

Geliştirici sorumluluk kabul etmez.
Lütfen sadece kendi videolarınızda test edin ve ölçülü şekilde kullanın.

🐛 Sorun Giderme
Sorun	Çözüm
ChromeDriver hatası	webdriver-manager otomatik olarak çözer
Proxy bağlantı hatası	Proxy’leri test edin veya devre dışı bırakın
SSL hataları	Bot tarafından otomatik yönetilir
Zaman aşımı	İnternet bağlantınızı kontrol edin

</div> 

