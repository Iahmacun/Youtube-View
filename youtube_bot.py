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
        """Generate a random user agent"""
        try:
            return self.ua.random
        except:
            return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    
    def create_stealth_driver(self, proxy=None):
        """Create a stealth Chrome driver"""
        try:
            options = Options()
            
            # Basic stealth settings
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Ignore SSL/certificate issues
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            
            # Random user agent
            options.add_argument(f"--user-agent={self.get_random_user_agent()}")
            
            # Headless mode
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            
            # Performance optimizations
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            
            # Proxy setup (used without prior testing)
            if proxy:
                options.add_argument(f'--proxy-server={proxy}')
                print(f"🔌 Using proxy: {proxy}")
            
            # Initialize driver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
            # Hide WebDriver properties
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3]})")
            driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
            
            return driver
            
        except Exception as e:
            print(f"❌ Driver creation error: {e}")
            return None
    
    def simulate_human_behavior(self, driver):
        """Simulate human-like behavior"""
        try:
            # Random waiting
            time.sleep(random.uniform(2, 5))
            
            # Random scrolling
            scroll_script = """
                window.scrollTo({
                    top: %d,
                    behavior: 'smooth'
                });
            """ % random.randint(100, 400)
            driver.execute_script(scroll_script)
            time.sleep(random.uniform(1, 3))
            
            # Video interaction
            try:
                video = driver.find_element(By.TAG_NAME, "video")
                if video:
                    duration = driver.execute_script("return arguments[0].duration", video)
                    if duration and duration > 10:
                        random_time = random.uniform(10, min(60, duration))
                        driver.execute_script("arguments[0].currentTime = arguments[1]", video, random_time)
                        print(f"⏩ Skipped to {random_time:.1f} seconds")
            except:
                pass
                
        except Exception as e:
            print(f"⚠ Human behavior simulation error: {e}")
    
    def watch_video(self, driver, url, watch_duration=30):
        """Watch video for a given duration"""
        try:
            print(f"🎥 Opening video...")
            driver.get(url)
            
            # Wait for the page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Initial wait
            initial_wait = random.uniform(3, 8)
            print(f"⏳ Waiting {initial_wait:.1f} seconds...")
            time.sleep(initial_wait)
            
            # Human-like actions
            self.simulate_human_behavior(driver)
            
            # Watch duration
            print(f"📺 Watching for {watch_duration} seconds...")
            start_time = time.time()
            interactions = 0
            
            while time.time() - start_time < watch_duration:
                remaining = watch_duration - (time.time() - start_time)
                
                # Random interactions (up to 2 times)
                if remaining > 10 and random.random() > 0.7 and interactions < 2:
                    print("🔄 Simulating extra interaction...")
                    self.simulate_human_behavior(driver)
                    interactions += 1
                
                time.sleep(random.uniform(5, 12))
            
            print("✅ Video watch completed")
            return True
            
        except TimeoutException:
            print("❌ Page load timeout")
            return False
        except Exception as e:
            print(f"❌ Video watch error: {e}")
            return False
    
    def load_proxies_from_file(self, filename="proxies.txt"):
        """Load proxy list from file (without testing)"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            print(f"📥 {len(proxies)} proxies loaded")
            return proxies
            
        except FileNotFoundError:
            print(f"❌ Proxy file not found: {filename}")
            return []
        except Exception as e:
            print(f"❌ Proxy load error: {e}")
            return []
    
    def run_bot(self, youtube_url, total_views=10, min_wait=30, max_wait=60, use_proxies=True):
        """Run the bot"""
        print("🚀 Starting YouTube View Bot...")
        print(f"🎯 Target views: {total_views}")
        print(f"🔗 URL: {youtube_url}")
        print("-" * 50)
        
        # Load proxies
        proxies = []
        if use_proxies:
            proxies = self.load_proxies_from_file()
            if not proxies:
                print("⚠ Continuing without proxies")
                use_proxies = False
        
        successful_views = 0
        failed_views = 0
        
        for view_count in range(1, total_views + 1):
            print(f"\n📊 View {view_count}/{total_views}")
            
            try:
                current_proxy = random.choice(proxies) if proxies else None
                
                # Create driver
                driver = self.create_stealth_driver(current_proxy)
                if not driver:
                    failed_views += 1
                    print("❌ Could not create driver")
                    continue
                
                # Random watch time (30-120 seconds)
                watch_time = random.randint(30, 120)
                
                success = self.watch_video(driver, youtube_url, watch_time)
                
                try:
                    driver.quit()
                except:
                    pass
                
                if success:
                    successful_views += 1
                    print(f"✅ Success: {successful_views}/{total_views}")
                else:
                    failed_views += 1
                    print(f"❌ Failed: {failed_views}/{total_views}")
                
                if view_count < total_views:
                    wait_time = random.randint(min_wait, max_wait)
                    print(f"⏳ Waiting {wait_time} seconds before next view...")
                    time.sleep(wait_time)
                    
            except KeyboardInterrupt:
                print("\n⏹️ Stopped by user")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                failed_views += 1
                time.sleep(10)
                continue
        
        print("\n" + "="*50)
        print("🎉 BOT RUN COMPLETED")
        print(f"✅ Successful views: {successful_views}")
        print(f"❌ Failed views: {failed_views}")
        if total_views > 0:
            print(f"📈 Success rate: {(successful_views/total_views)*100:.1f}%")
        print("="*50)

def main():
    """Main function"""
    print("🎬 YOUTUBE VIEW BOT - WITHOUT PROXY TEST")
    print("=" * 40)
    
    youtube_url = input("📹 YouTube Video URL: ").strip()
    
    if not youtube_url.startswith(('https://www.youtube.com/', 'https://youtube.com/', 'https://youtu.be/')):
        print("❌ Invalid YouTube URL!")
        return
    
    try:
        total_views = int(input("🎯 Total views: ").strip())
        min_wait = int(input("⏱️ Min wait (seconds): ").strip())
        max_wait = int(input("⏱️ Max wait (seconds): ").strip())
        use_proxies_input = input("🔒 Use proxies? (y/n): ").strip().lower()
        use_proxies = use_proxies_input == 'y'
    except ValueError:
        print("❌ Invalid number input!")
        return
    
    bot = YouTubeViewBot()
    bot.run_bot(
        youtube_url=youtube_url,
        total_views=total_views,
        min_wait=min_wait,
        max_wait=max_wait,
        use_proxies=use_proxies
    )

if __name__ == "__main__":
    try:
        import requests
        from fake_useragent import UserAgent
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        main()
    except ImportError as e:
        print(f"❌ Missing library: {e}")
        print("📦 Install with: pip install requests fake-useragent selenium webdriver-manager")
