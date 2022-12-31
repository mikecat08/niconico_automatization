from selenium import webdriver
import time

driver = webdriver.Chrome('./driver/chromedriver')

# ニコニコのログイン画面を開く
driver.get('https://account.nicovideo.jp/login')
time.sleep(1)

# ブラウザを閉じる
driver.close()



