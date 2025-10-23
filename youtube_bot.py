
import time
import random
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

class YouTubeViewBot:
    def __init__(self):
        self.ua = UserAgent()
        
    def get_random_user_agent(self):
        """Rastgele user agent oluştur"""
        try:
            return self.ua.random
        except:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    
    def create_stealth_driver(self, proxy=None):
        """Gizli Chrome driver oluştur"""
        try:
            options = Options()
            
            # Temel gizlilik ayarları
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # SSL ve sertifika hatalarını önle
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            
            # User agent
            options.add_argument(f"--user-agent={self.get_random_user_agent()}")
            
            # Görünmez mod
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            
            # Performans optimizasyonları
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            
            # Proxy ayarı (test yapmadan direkt kullan)
            if proxy:
                options.add_argument(f'--proxy-server={proxy}')
                print(f"🔌 Proxy kullanılıyor: {proxy}")
            
            # Driver'ı başlat
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
            # WebDriver özelliğini gizle
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]})")
            driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
            
            return driver
            
        except Exception as e:
            print(f"❌ Driver oluşturma hatası: {e}")
            return None
    
    def simulate_human_behavior(self, driver):
        """İnsan benzeri davranışlar simüle et"""
        try:
            # Rastgele bekleme
            time.sleep(random.uniform(2, 5))
            
            # Sayfayı kaydırma
            scroll_script = """
                window.scrollTo({
                    top: %d,
                    behavior: 'smooth'
                });
            """ % random.randint(100, 400)
            driver.execute_script(scroll_script)
            time.sleep(random.uniform(1, 3))
            
            # Video kontrolü
            try:
                video = driver.find_element(By.TAG_NAME, "video")
                if video:
                    # Video süresini al
                    duration = driver.execute_script("return arguments[0].duration", video)
                    if duration and duration > 10:
                        # Rastgele bir noktaya atla
                        random_time = random.uniform(10, min(60, duration))
                        driver.execute_script("arguments[0].currentTime = arguments[1]", video, random_time)
                        print(f"⏩ Video {random_time:.1f}. saniyeye atlandı")
            except:
                pass  # Video bulunamazsa sorun değil
                
        except Exception as e:
            print(f"⚠ Davranış simülasyonu hatası: {e}")
    
    def watch_video(self, driver, url, watch_duration=30):
        """Video izleme işlemi"""
        try:
            print(f"🎥 Video açılıyor...")
            driver.get(url)
            
            # Sayfanın yüklenmesini bekle
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Başlangıç beklemesi
            initial_wait = random.uniform(3, 8)
            print(f"⏳ {initial_wait:.1f} saniye bekleniyor...")
            time.sleep(initial_wait)
            
            # İnsan benzeri davranış
            self.simulate_human_behavior(driver)
            
            # Video izleme süresi
            print(f"📺 {watch_duration} saniye izleniyor...")
            start_time = time.time()
            interactions = 0
            
            while time.time() - start_time < watch_duration:
                remaining = watch_duration - (time.time() - start_time)
                
                # Rastgele ara etkileşimler (maksimum 2 kez)
                if remaining > 10 and random.random() > 0.7 and interactions < 2:
                    print("🔄 Ek etkileşim simüle ediliyor...")
                    self.simulate_human_behavior(driver)
                    interactions += 1
                
                # Kısa bekleme
                time.sleep(random.uniform(5, 12))
            
            print("✅ Video izleme tamamlandı")
            return True
            
        except TimeoutException:
            print("❌ Sayfa yükleme zaman aşımı")
            return False
        except Exception as e:
            print(f"❌ Video izleme hatası: {e}")
            return False
    
    def load_proxies_from_file(self, filename="proxies.txt"):
        """Proxy listesini dosyadan yükle (test yapmadan)"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            print(f"📥 {len(proxies)} proxy yüklendi")
            return proxies
            
        except FileNotFoundError:
            print(f"❌ Proxy dosyası bulunamadı: {filename}")
            return []
        except Exception as e:
            print(f"❌ Proxy yükleme hatası: {e}")
            return []
    
    def run_bot(self, youtube_url, total_views=10, min_wait=30, max_wait=60, use_proxies=True):
        """Bot'u çalıştır"""
        print("🚀 YouTube View Bot Başlatılıyor...")
        print(f"🎯 Hedef: {total_views} görüntüleme")
        print(f"🔗 URL: {youtube_url}")
        print("-" * 50)
        
        # Proxy'leri yükle
        proxies = []
        if use_proxies:
            proxies = self.load_proxies_from_file()
            if not proxies:
                print("⚠ Proxy kullanılmadan devam ediliyor")
                use_proxies = False
        
        successful_views = 0
        failed_views = 0
        
        for view_count in range(1, total_views + 1):
            print(f"\n📊 Görüntüleme {view_count}/{total_views}")
            
            try:
                # Proxy seç (eğer varsa)
                current_proxy = random.choice(proxies) if proxies else None
                
                # Driver oluştur
                driver = self.create_stealth_driver(current_proxy)
                if not driver:
                    failed_views += 1
                    print("❌ Driver oluşturulamadı")
                    continue
                
                # Video izleme süresi (30-120 saniye arası)
                watch_time = random.randint(30, 120)
                
                # Video izle
                success = self.watch_video(driver, youtube_url, watch_time)
                
                # Driver'ı kapat
                try:
                    driver.quit()
                except:
                    pass
                
                if success:
                    successful_views += 1
                    print(f"✅ Başarılı: {successful_views}/{total_views}")
                else:
                    failed_views += 1
                    print(f"❌ Başarısız: {failed_views}/{total_views}")
                
                # Son görüntüleme değilse bekle
                if view_count < total_views:
                    wait_time = random.randint(min_wait, max_wait)
                    print(f"⏳ {wait_time} saniye bekleniyor...")
                    time.sleep(wait_time)
                    
            except KeyboardInterrupt:
                print("\n⏹️ Kullanıcı tarafından durduruldu")
                break
            except Exception as e:
                print(f"❌ Beklenmeyen hata: {e}")
                failed_views += 1
                # Hata durumunda kısa bekle
                time.sleep(10)
                continue
        
        # Sonuçları göster
        print("\n" + "="*50)
        print("🎉 BOT ÇALIŞMASI TAMAMLANDI")
        print(f"✅ Başarılı görüntülemeler: {successful_views}")
        print(f"❌ Başarısız görüntülemeler: {failed_views}")
        if total_views > 0:
            print(f"📈 Başarı oranı: {(successful_views/total_views)*100:.1f}%")
        print("="*50)

def main():
    """Ana çalıştırıcı fonksiyon"""
    print("🎬 YOUTUBE VIEW BOT - PROXY TEST OLMADAN")
    print("=" * 40)
    
    # Kullanıcı girdileri
    youtube_url = input("📹 YouTube Video URL: ").strip()
    
    # URL kontrolü
    if not youtube_url.startswith(('https://www.youtube.com/', 'https://youtube.com/', 'https://youtu.be/')):
        print("❌ Geçersiz YouTube URL!")
        return
    
    try:
        total_views = int(input("🎯 Kaç görüntüleme: ").strip())
        min_wait = int(input("⏱️ Min bekleme (saniye): ").strip())
        max_wait = int(input("⏱️ Max bekleme (saniye): ").strip())
        use_proxies_input = input("🔒 Proxy kullanılsın mı? (e/h): ").strip().lower()
        use_proxies = use_proxies_input == 'e'
    except ValueError:
        print("❌ Geçersiz sayı girdisi!")
        return
    
    # Bot'u başlat
    bot = YouTubeViewBot()
    bot.run_bot(
        youtube_url=youtube_url,
        total_views=total_views,
        min_wait=min_wait,
        max_wait=max_wait,
        use_proxies=use_proxies
    )

if __name__ == "__main__":
    # Gerekli kütüphaneleri kontrol et
    try:
        import requests
        from fake_useragent import UserAgent
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        main()
    except ImportError as e:
        print(f"❌ Gerekli kütüphane eksik: {e}")
        print("📦 Kurulum için: pip install requests fake-useragent selenium webdriver-manager")
