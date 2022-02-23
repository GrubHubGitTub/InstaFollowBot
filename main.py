import random
import os
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("selenium")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
install("python-dotenv")
from dotenv import load_dotenv

# _______ CHANGE PATH TO YOUR ENV FILE IF NECESSARY________
load_dotenv(".env")
email = os.getenv("email")
pw = os.getenv("pw")

#   -----------CHOOSE WEBDRIVER (REMOVE HEADLESS OPTION TO SEE SELENIUM RUNNING)------------
install("webdriver-manager")

# # CHROME DRIVER USE THIS:
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# EDGE DRIVER USES THIS:
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
options = Options()
options.add_argument("headless")
driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()), options=options)


def login():
    login_choice = input("Sign in through ig or fb?")

    # login through insta
    if login_choice == "ig":
        driver.get("https://www.instagram.com")
        sleep(3)
        print("Logging in to instagram...")
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(email)
        pw_input = driver.find_element(By.NAME, "password")
        pw_input.send_keys(pw)
        login_button = driver.find_element(By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF")
        login_button.click()
        sleep(5)

    # login through fb
    if login_choice == "fb":
        driver.get("https://www.instagram.com")
        sleep(3)
        print("Logging in to instagram via Facebook...")
        current_url = driver.current_url
        login_with_fb = driver.find_element(By.CSS_SELECTOR,".KPnG0")
        login_with_fb.click()
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))
        fb_email_input = driver.find_element(By.NAME,"email")
        fb_pw_input = driver.find_element(By.NAME,"pass")
        fb_email_input.send_keys(email)
        fb_pw_input.send_keys(pw)
        login_fb_button = driver.find_element(By.NAME,"login")
        login_fb_button.send_keys(Keys.ENTER)
        sleep(10)
        # no_notif = driver.find_element(By.CSS_SELECTOR,".aOOlW.HoLwm")
        # no_notif.click()
        # sleep(3)

def get_account(account):
    print(f"Looking for {account}")
    user_search = driver.find_element(By.CSS_SELECTOR, ".XTCLo")
    user_search.send_keys(account)
    sleep(2)
    user = driver.find_element(By.CSS_SELECTOR, ".-qQT3")
    user.click()
    sleep(7)

def get_followers():
    show_followers = driver.find_element(By.CSS_SELECTOR, "ul.k9GMp li:nth-child(2) a")
    show_followers.click()
    sleep(3)
    follow_buttons = driver.find_elements(By.CSS_SELECTOR,".sqdOP.L3NKy.y3zKF")
    follower_amount = len(follow_buttons)
    while follower_amount < 50:
        popup = driver.find_element(By.XPATH, "/html/body/div[6]/div//a")
        popup.send_keys(Keys.END)
        follow_buttons = driver.find_elements(By.CSS_SELECTOR,".sqdOP.L3NKy.y3zKF")
        follower_amount = (len(follow_buttons))
        print(f" Collecting followers: {follower_amount}")
        sleep(1)
    follow(follow_buttons)

def follow(follow_buttons):
    count = 1
    for button in follow_buttons:
        rand_sleep = random.randint(1, 5)
        button.click()
        print(f"Clicking {count}")
        sleep(rand_sleep)
        count += 1

account = input("From what account would you like to get followers?")
login()
get_account(account)
get_followers()

