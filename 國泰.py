from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service # option指令套件
from selenium.webdriver.chrome.options import Options # 手機模式
from selenium.webdriver import ActionChains #WEB DRIVER 點擊用，目前只能透過element點擊要再查查
from selenium.webdriver.support import expected_conditions as EC
import os #開啟建立資料夾用
import datetime #依日期分類
import time #陽春版暫停，XD

from selenium.webdriver.support.wait import WebDriverWait

#日期+建資料夾
target_directory="C:\\Users\\yihli\\OneDrive\\桌面\\自動化測試"
dt = datetime.date.today()
current_time = datetime.datetime.now().strftime("%H-%M-%S")
format_date = dt.strftime('%Y%m%d')
file_name = f"{format_date}.txt"
file_path = os.path.join(target_directory, file_name)
with open(file_path, "a") as f:
    f.write(f"{format_date} {current_time} 建立成功\n")

#指定開發者模式與模擬手機解析度
mobile={"devicename": "iphone 12 pro"}
option = webdriver.ChromeOptions()

option.add_experimental_option("mobileEmulation", mobile)
s = Service('C:/Python/Python312/chromedriver.exe')
option.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(service=s,options=option)#
driver.get("https://cathaybk.com.tw/cathaybk/")

#使用chrome app到國泰世華銀行官網並截圖
#判斷10秒內找到元素則截圖,否則跳e
try:
    home_element= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/section/div[3]/div[1]"))
    )
    print("確認可進入首頁")
    with open(file_path, "a") as f:
        f.write(f"{format_date} {current_time} 確認可進入首頁 \n")
    screenshot_name = f"{dt}.{current_time}.首頁.png"
    screenshot_path = os.path.join("C:/Users/yihli/OneDrive/桌面/自動化測試", screenshot_name)
    driver.save_screenshot(screenshot_path)
except Exception as e:
    print(e)
    with open(file_path, "a") as f:
        f.write(f"{format_date} {current_time} 等待元素出現時發生錯誤"+e+" \n")

#暫停、找尋並點擊到信用卡列表
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div").click()

#計算有幾個項目並截圖
time.sleep(1)
count_elements=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]").find_elements(By.ID,"lnk_Link")
count = len(count_elements)
print("共有"+str(count)+"個信用卡子分類")
with open(file_path, "a") as f:
    f.write(f"{format_date} {current_time} 共有"+str(count)+"個信用卡分類 \n")
screenshot_name = f"{dt}.{current_time}.共有"+str(count)+"個信用卡子分類.png"
screenshot_path = os.path.join("C:/Users/yihli/OneDrive/桌面/自動化測試", screenshot_name)
driver.save_screenshot(screenshot_path)

#暫停、並點到停發信用卡
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]").click()
time.sleep(1)
element=driver.find_element(By.XPATH,"/html/body/div[1]/main/article/div/div/div/div[1]/div/div/a[6]/p") #找到元素(透過try試過)，無法點擊，判斷元素不再畫面內
driver.execute_script("arguments[0].scrollIntoView(true);", element) #使用Javascript滾動到元素可見區域 讚嘆chatgpt
element.click()
time.sleep(1)

#確認父元素+子元素
parent_element=driver.find_element(By.XPATH,"/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]")
child_elements=parent_element.find_elements(By.CSS_SELECTOR,"span[aria-label^='Go to slide']")

#透過迴圈知道相似子元素數量，逐一截圖並print與寫入文檔
total_stop_cards=0
for index,child_element in enumerate(child_elements,start=1):
    child_element.click()
    time.sleep(1)
    screenshot_name = f"{dt}.{current_time}.停發卡{index}.png"
    screenshot_path = os.path.join("C:/Users/yihli/OneDrive/桌面/自動化測試", screenshot_name)
    driver.save_screenshot(screenshot_path)
    time.sleep(1)

    total_stop_cards = index
with open(file_path, "a") as f:
    f.write(f"{format_date} {current_time} 停發卡共"+str(total_stop_cards)+"張 \n")
print("停發卡共"+str(total_stop_cards)+"張")


input("請輸入任意建") #避免自動關閉
