import random

import selenium as s
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

email = ""
pw = ""

login_choice = input("Sign in through ig or fb?")
account = input("From what account would you like to get followers?")

# login through insta
if login_choice == "ig":
    chrome_driver = "C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"
    driver = s.webdriver.Chrome(executable_path=chrome_driver)
    driver.get("https://www.instagram.com")
    sleep(3)
    username_input = driver.find_element_by_name("username")
    username_input.send_keys(email)
    pw_input = driver.find_element_by_name("password")
    pw_input.send_keys(pw)
    login_button = driver.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF")
    login_button.click()
    sleep(5)

# login through fb
if login_choice == "fb":
    chrome_driver = "C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"
    driver = s.webdriver.Chrome(executable_path=chrome_driver)
    driver.get("https://www.instagram.com")
    sleep(3)
    current_url = driver.current_url
    login_with_fb = driver.find_element_by_css_selector(".KPnG0")
    login_with_fb.click()
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    fb_email_input = driver.find_element_by_name("email")
    fb_pw_input = driver.find_element_by_name("pass")
    fb_email_input.send_keys(email)
    fb_pw_input.send_keys(pw)
    login_fb_button = driver.find_element_by_name("login")
    login_fb_button.send_keys(Keys.ENTER)
    sleep(10)
    no_notif = driver.find_element_by_css_selector(".aOOlW.HoLwm")
    no_notif.click()
    sleep(3)

# choose the insta account
user_search = driver.find_element_by_css_selector(".XTCLo")
user_search.send_keys(account)
sleep(2)
account = driver.find_element_by_css_selector(".-qQT3")
account.click()
sleep(5)
show_followers = driver.find_element_by_css_selector("a.-nal3")
show_followers.click()
sleep(3)

# collect 50 buttons
follow_buttons = driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")
follower_amount = len(follow_buttons)
while follower_amount < 50:
    popup = driver.find_element_by_xpath("/html/body/div[6]/div//a")
    popup.send_keys(Keys.END)
    follow_buttons = driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")
    follower_amount = (len(follow_buttons))
    print(follower_amount)
    sleep(1)

# click the buttons (insta allows max 50)
for button in follow_buttons:
    rand_sleep = random.randint(1, 5)
    button.click()
    sleep(rand_sleep)



