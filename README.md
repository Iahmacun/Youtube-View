<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube View Bot - Akademik Proje</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 40px 0;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .badge {
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            backdrop-filter: blur(10px);
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card h2 {
            color: #4a5568;
            margin-bottom: 20px;
            font-size: 1.8rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .feature-item {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            color: white;
            backdrop-filter: blur(10px);
        }

        .feature-item h3 {
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
        }

        .warning {
            background: #fed7d7;
            border-left: 4px solid #e53e3e;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .setup-steps {
            display: grid;
            gap: 15px;
        }

        .step {
            display: flex;
            align-items: flex-start;
            gap: 15px;
        }

        .step-number {
            background: #667eea;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-weight: bold;
        }

        .usage-example {
            background: #f7fafc;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            padding: 25px;
            margin: 20px 0;
        }

        .btn {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .btn:hover {
            background: #5a67d8;
        }

        .footer {
            text-align: center;
            color: white;
            margin-top: 50px;
            padding: 30px 0;
            opacity: 0.8;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .features {
                grid-template-columns: 1fr;
            }
            
            .card {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🎬 YouTube View Bot</h1>
            <p>Akademik Projeler ve Tez Çalışmaları İçin</p>
            <div class="badges">
                <span class="badge">Python 3.8+</span>
                <span class="badge">Selenium</span>
                <span class="badge">Proxy Desteği</span>
                <span class="badge">Akademik</span>
            </div>
        </header>

        <div class="features">
            <div class="feature-item">
                <h3>🤖 Akıllı Otomasyon</h3>
                <p>İnsan benzeri davranışlar, rastgele kaydırma, gerçekçi bekleme süreleri</p>
            </div>
            <div class="feature-item">
                <h3>🔒 Gizlilik Odaklı</h3>
                <p>Stealth mod ile tespit edilme riski minimize edilmiştir</p>
            </div>
            <div class="feature-item">
                <h3>🌐 Proxy Desteği</h3>
                <p>Çoklu IP adresleri ile güvenli ve anonim bağlantı</p>
            </div>
        </div>

        <div class="card">
            <h2>🚀 Hızlı Başlangıç</h2>
            <div class="setup-steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <div>
                        <strong>Gereksinimleri yükleyin:</strong>
                        <div class="code-block">
pip install selenium fake-useragent webdriver-manager requests
                        </div>
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <div>
                        <strong>Proxy dosyası oluşturun (proxies.txt):</strong>
                        <div class="code-block">
http://proxy1:8080
https://proxy2:3128
192.168.1.100:8080
                        </div>
                    </div>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <div>
                        <strong>Bot'u çalıştırın:</strong>
                        <div class="code-block">
python youtube_bot.py
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="card">
            <h2>📖 Kullanım</h2>
            <div class="usage-example">
                <h4>Örnek Çalıştırma:</h4>
                <div class="code-block">
🎬 YOUTUBE VIEW BOT - STABİL SÜRÜM
========================================
📹 YouTube URL: https://www.youtube.com/watch?v=...
🎯 Görüntüleme sayısı: 50
⏱️ Min bekleme: 30
⏱️ Max bekleme: 60
🔒 Proxy kullanılsın mı? (e/h): e
                </div>
            </div>
        </div>

        <div class="card">
            <h2>⚙️ Kod Örneği</h2>
            <div class="code-block">
from youtube_bot import YouTubeViewBot

bot = YouTubeViewBot()
bot.run_bot(
    youtube_url="https://youtube.com/watch?v=...",
    total_views=50,
    min_wait=30,
    max_wait=60,
    use_proxies=True
)
            </div>
        </div>

        <div class="card">
            <h2>📊 Çıktı Örneği</h2>
            <div class="code-block">
🚀 YouTube View Bot Başlatılıyor...
🎯 Hedef: 50 görüntüleme

📊 Görüntüleme 1/50
🔌 Proxy kullanılıyor: http://192.168.1.1:8080
🎥 Video açılıyor...
⏳ 8.3 saniye bekleniyor...
📺 45 saniye izleniyor...
✅ Başarılı: 1/50
            </div>
        </div>

        <div class="warning">
            <h3>⚠️ ÖNEMLİ UYARI</h3>
            <p>Bu proje sadece <strong>eğitim ve akademik araştırma</strong> amaçlıdır. 
            YouTube'un Hizmet Şartları'nı ihlal edebilir. Sorumluluk kullanıcıya aittir. 
            Limitli kullanım önerilir.</p>
        </div>

        <div class="card">
            <h2>🛠️ Özellikler</h2>
            <ul style="list-style-position: inside; line-height: 2;">
                <li>🤖 İnsan benzeri davranış simülasyonu</li>
                <li>🔒 Proxy desteği (çoklu IP)</li>
                <li>🛡️ Gizlilik odaklı (stealth mode)</li>
                <li>📊 Detaylı istatistik ve loglama</li>
                <li>⚡ Otomatik ChromeDriver yönetimi</li>
                <li>🔄 Hata toleranslı bağlantı</li>
                <li>🎯 Esnek yapılandırma seçenekleri</li>
            </ul>
        </div>

        <footer class="footer">
            <p>YouTube View Bot - Akademik Proje | MIT License</p>
            <p style="margin-top: 10px; font-size: 0.9rem;">
                Sadece eğitim ve bilimsel araştırma amaçlıdır
            </p>
        </footer>
    </div>
</body>
</html>
