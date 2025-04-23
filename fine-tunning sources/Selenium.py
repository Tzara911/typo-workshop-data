from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time, os

# website for crawling
urls = [
    "https://www.airbnb.com",
    "https://www.booking.com",
    "https://www.expedia.com",
    "https://www.uber.com/us/en/",
    "https://www.lyft.com/rider",
    "https://www.eventbrite.com",
    "https://www.signupgenius.com",
    "https://www.osfhealthcare.org/schedule/",
    "https://www.osfhealthcare.org/services/",
]

# set the path for the screenshot
os.makedirs("real_screenshots", exist_ok=True)

# headless browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,800")

# 设定驱动路径

driver_path = r"C:\Zelandar\chromedriver.exe"  
service = Service(driver_path)
driver = webdriver.Chrome(service =service, options=options)

# 截图主循环
for idx, url in enumerate(urls):
    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载
        
       # 自动命名文件（从 URL 提取域名）
        site_name = url.split("//")[1].split("/")[0].replace("www.", "")
        screenshot_path = f"real_screenshots/{site_name}.png"
        driver.save_screenshot(screenshot_path)

        print(f"✅ 截图完成：{screenshot_path}")
    except Exception as e:
        print(f"❌ 截图失败：{url}，错误：{e}")

driver.quit()
