from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
import time
import getpass

# CHROMEDRIVER = "./driver/chromedriver"
# chrome_service = fs.Service(executable_path=CHROMEDRIVER)
# driver = webdriver.Chrome(service=chrome_service)

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# ブラウザのサイズを指定
driver.set_window_size(1200,800)

# 要素が見つかるまで、最大30秒間待機する
driver.implicitly_wait(30)

# ニコニコのログイン画面を開く
driver.get('https://account.nicovideo.jp/login')

# ページの読み込みが完了するまで待機
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

# 一覧の表示件数を100件に切り替える
pulldown_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/section/nav[1]/div/div[2]/div")
pulldown_btn.click()
mov_num_100 = driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[4]")
mov_num_100.click()


# 現在のページのURLを取得
cur_url = driver.current_url

# ループ処理用の変数を用意
i = 0

while True:
  i = i + 1
  time.sleep(1)

  # リンク先を格納するための空のリスト型を用意
  cpp_urls = []

  # 各動画の収益化登録ページのURLを繰り返し取得する処理
  for mov in driver.find_elements(By.CLASS_NAME, "css-hgmrya"):
    option_btn = mov.find_element(By.CLASS_NAME, "MuiButtonBase-root")
    option_btn.click()

    # 収入を得るボタンのリンク先URLをリスト型に格納
    cpp_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/a[7]")
    cpp_btn_url = cpp_btn.get_attribute('href')
    cpp_urls.append(cpp_btn_url)

    # 背景エリアをクリックすることでモーダルを消す
    # これをしないと次の動画のオプションボタンをクリックすることができない
    backdrop_root = driver.find_element(By.CLASS_NAME, "MuiBackdrop-root")
    backdrop_root.click()


  # ====================================
  # 申請画面
  # ====================================

  for cpp in cpp_urls:

    # クリエイター奨励プログラムへの参加ページへ遷移
    driver.get(cpp)
    time.sleep(1)

    # id Column01を持つdiv要素の中の1番上の要素のclassを取得
    col01_ttl = driver.find_element(By.XPATH, "//*[@id='Column01']/div")
    col01_ttl_class = col01_ttl.get_attribute('class')
    print(col01_ttl_class)

    # id Column01を持つdiv要素の中の1番上の要素のclassがapply-msgだった時のみ以下の処理を実行
    if col01_ttl_class == "apply-msg":

      # チュートリアルを下までスクロール
      tutorial = driver.find_element(By.ID, "tutorial")
      driver.execute_script("arguments[0].scrollTo(0, document.body.scrollHeight);", tutorial)

      # チェックボックスをクリック
      check_box = driver.find_element(By.ID, "checkerid")
      check_box.click()

      # 申請ボタンをクリックする
      apply_btn = driver.find_element(By.LINK_TEXT, "作品収入を申請する")
      apply_btn.click()

  # 元の一覧ページに戻る
  driver.get(cur_url)
  time.sleep(1)

  # ループ回数に応じた数だけ次の一覧ページへ遷移する繰り返し処理
  for j in range(i):
    # 次の一覧ページへ遷移するボタンを取得
    next_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/section/nav[2]/div/nav/ul/li[9]/button")
    next_btn.click()
    time.sleep(1)

  # 次の一覧ページへ遷移するボタンのclassを取得
  next_btn = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/section/nav[2]/div/nav/ul/li[9]/button")
  next_btn_class = next_btn.get_attribute('class')

  # 次へボタンのクラスにMui-disabledが含まれている場合はループを終了する
  if "Mui-disabled" in next_btn_class:
    break

  # ループが20回以上ループした場合もループを終了する
  if i > 20:
    break


# ブラウザを閉じる
driver.close()



