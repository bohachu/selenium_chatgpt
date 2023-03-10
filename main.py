import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

# 讀取 .env 檔案中的帳號密碼設定
load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# 設置網站 URL
url = "https://www.chatgpt.com/"

# 初始化 Chrome 瀏覽器
driver = webdriver.Chrome()

# 前往 ChatGPT 網站
driver.get(url)

# 找到帳號和密碼的輸入框，並自動輸入帳號和密碼
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
username_input.send_keys(username)
password_input.send_keys(password)

# 模擬按下登入按鈕
login_button = driver.find_element_by_xpath("//button[contains(text(), 'Login')]")
login_button.send_keys(Keys.RETURN)

# 等待網頁載入完成
time.sleep(5)

# 點選 New chat 按鈕
new_chat_button = driver.find_element_by_xpath("//button[contains(text(), 'New chat')]")
new_chat_button.click()

# 找到 chat 輸入框，並自動輸入提問
chat_input = driver.find_element_by_name("chat-input")
chat_input.send_keys("我想請問中華民國的總統是誰？")
chat_input.send_keys(Keys.RETURN)

# 等待回應出現
time.sleep(5)

# 取得回應答案
response = driver.find_element_by_class_name("chat-message-bot").text

# 印出回應答案
print(response)

# 關閉瀏覽器
driver.quit()
