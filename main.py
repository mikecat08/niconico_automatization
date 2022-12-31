from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass

driver = webdriver.Chrome('./driver/chromedriver')
driver.set_window_size(1200,800)

# ニコニコのログイン画面を開く
driver.get('https://account.nicovideo.jp/login')
time.sleep(1)


# ====================================
# ログイン画面
# ====================================

# メールアドレスの入力
print('ユーザー名（メールアドレス）を入力して下さい。')
user = input('username: ')

# パスワードの入力
print('パスワードを入力して下さい。')
password = getpass.getpass('password: ')

# メールアドレスをインプットエリアに入力
input__mailtel = driver.find_element(By.ID, "input__mailtel")
input__mailtel.send_keys(user)

# パスワードをインプットエリアに入力
input__password = driver.find_element(By.ID, "input__password")
input__password.send_keys(password)

# ログインボタンをクリック
login_btn = driver.find_element(By.ID, "login__submit")
login_btn.click()
time.sleep(1)


# ====================================
# 認証コード入力画面
# ====================================

# ワンタイムパスワードの入力
print('ワンタイムパスワードを入力して下さい。')
one_time_pw = input('onetimepass: ')

# ワンタイムパスワードをインプットエリアに入力
oneTimePw = driver.find_element(By.ID, "oneTimePw")
oneTimePw.send_keys(one_time_pw)

# ログインボタンをクリック
onetime_login_btn = driver.find_element(By.NAME, "loginBtn")
onetime_login_btn.click()
time.sleep(1)


# ====================================
# ホーム画面
# ====================================

# ユーザーボタンをクリック
user_btn = driver.find_element(By.CLASS_NAME, "common-header-1kbay7q")
user_btn.click()
time.sleep(1)


# ====================================
# マイページ
# ====================================

# 動画投稿・シリーズボタンをクリック
my_movie_btn = driver.find_element(By.LINK_TEXT, "投稿動画・シリーズ")
my_movie_btn.click()
time.sleep(1)


# ====================================
# 動画一覧
# ====================================

# for mov in driver.find_elements(By.CLASS_NAME, "css-1gf8rdn"):
#   option_btn = mov.find_element(By.CLASS_NAME, "MuiButtonBase-root")
#   option_btn.click()

#   # 収入を得るボタンをクリック
#   cpp_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/ul/li[7]/a")
#   cpp_btn.click()

#   # 作品にもどるボタンがある場合はクリック
#   if driver.find_element(By.LINK_TEXT, "作品にもどる"):
#     driver.find_element(By.LINK_TEXT, "作品にもどる").click()

# ブラウザを閉じる
# driver.close()



