from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from collections import defaultdict

def create_driver():
    edge_options = Options()
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-gpu')
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    edge_options.add_argument('--disable-extensions')
    edge_options.page_load_strategy = 'eager'
    
    return webdriver.Edge(
        options=edge_options,
        service=Service(EdgeChromiumDriverManager().install())
    )

def wait_for_page_and_play_video(driver, url, video_time=3):
    try:
        print(f"正在載入頁面: {url}")
        driver.get(url)
        
        print("等待頁面載入...")
        driver.implicitly_wait(2)
        
        print(f"播放影片 {video_time} 秒...")
        time.sleep(video_time + 1)
        return True
    except Exception as e:
        print(f"頁面載入或播放過程中發生錯誤: {e}")
        return False

def auto_visit(urls, target_clicks=200, video_time=3, interval_seconds=1):
    print("正在設定 Edge 瀏覽器...")
    
    click_counts = defaultdict(int)
    total_clicks_needed = len(urls) * target_clicks
    total_clicks_done = 0
    
    try:
        driver = create_driver()
        print("Edge 瀏覽器設定成功！")
        
        while True:
            if all(click_counts[url] >= target_clicks for url in urls):
                print("所有網址都已達到目標點擊數！程式結束。")
                break
                
            for url in urls:
                if click_counts[url] >= target_clicks:
                    continue
                
                try:
                    if wait_for_page_and_play_video(driver, url, video_time):
                        click_counts[url] += 1
                        total_clicks_done += 1
                        
                        print(f"\n當前進度:")
                        print(f"- 此網址: {click_counts[url]}/{target_clicks}")
                        print(f"- 總進度: {total_clicks_done}/{total_clicks_needed} ({(total_clicks_done/total_clicks_needed*100):.1f}%)")
                        
                        if interval_seconds > 0:
                            print(f"短暫等待 {interval_seconds} 秒...")
                            time.sleep(interval_seconds)
                    else:
                        print("重新啟動瀏覽器...")
                        driver.quit()
                        driver = create_driver()
                    
                except Exception as e:
                    print(f"發生錯誤: {e}")
                    try:
                        driver.quit()
                    except:
                        pass
                    print("重新啟動瀏覽器...")
                    driver = create_driver()
                    time.sleep(1)
            
            if total_clicks_done % 10 == 0:
                print("\n--- 當前進度明細 ---")
                for url in urls:
                    print(f"{url}: {click_counts[url]}/{target_clicks}")
                print("---------------\n")
            
    except KeyboardInterrupt:
        print("程式已手動停止")
    finally:
        try:
            driver.quit()
        except:
            pass
        print("\n=== 最終統計 ===")
        for url in urls:
            print(f"{url}: {click_counts[url]} 次點擊")
        print(f"總完成進度: {total_clicks_done}/{total_clicks_needed} ({(total_clicks_done/total_clicks_needed*100):.1f}%)")
        print("===============")

def get_user_urls():
    urls = []
    print("請輸入要訪問的短網址（每行一個，輸入空白行完成）：")
    while True:
        url = input().strip()
        if not url:
            break
        urls.append(url)
    return urls

def main():
    print("=== 自動點擊程式 ===")
    # 取得使用者輸入的網址
    urls_to_visit = get_user_urls()
    
    if not urls_to_visit:
        print("未輸入任何網址，程式結束")
        return
    
    # 取得點擊次數
    while True:
        try:
            target_clicks = int(input("請輸入每個網址要點擊的次數（預設200）：") or "200")
            if target_clicks > 0:
                break
            print("請輸入大於0的數字")
        except ValueError:
            print("請輸入有效的數字")
    
    # 取得影片播放時間
    while True:
        try:
            video_time = int(input("請輸入影片播放時間（秒，預設3）：") or "3")
            if video_time > 0:
                break
            print("請輸入大於0的數字")
        except ValueError:
            print("請輸入有效的數字")
    
    print("\n程式開始執行...")
    print(f"目標：每個網址點擊 {target_clicks} 次")
    print(f"影片播放時間：{video_time} 秒")
    print(f"總共需要點擊次數：{len(urls_to_visit) * target_clicks} 次")
    
    auto_visit(urls_to_visit, target_clicks=target_clicks, video_time=video_time, interval_seconds=1)

if __name__ == "__main__":
    main()
