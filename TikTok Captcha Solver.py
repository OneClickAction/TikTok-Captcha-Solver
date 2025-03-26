from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from ocacaptcha import oca_solve_captcha
import json
import time
import requests
import urllib.request
import base64
import os
import random
import string
import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('start-maximized')
options.add_argument('--accept-lang=en-US,en;q=0.5')
options.add_argument('--dom-automation=disabled')
options.add_argument('--ignore-certificate-errors')


service = Service(executable_path='C:\\Python\\webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
actions = ActionChains(driver, duration=550)

# Upload website
driver.get("https://www.tiktok.com/login/phone-or-email/email")
time.sleep(random.uniform(8, 12))

# Check cookies banner
shadow_root = driver.execute_script("return document.querySelector('body > tiktok-cookie-banner')?.shadowRoot")
if shadow_root:
    buttons = shadow_root.find_elements(By.CSS_SELECTOR, "div > div.button-wrapper > button:nth-child(1)")
    if buttons:
        is_exists_cookies_button = buttons[0]
        if is_exists_cookies_button.is_displayed():
            is_exists_cookies_button.click()
            time.sleep(random.uniform(2, 5))

# Write login data
email_input = driver.find_element(By.XPATH, '//input[@name="username"]')
my_email = "YOUR_USERNAME_OR_EMAIL_HERE"
for char in my_email:
    actions.move_to_element(email_input).click().send_keys(char).perform()
    time.sleep(random.uniform(0.00001,0.00005))
time.sleep(random.uniform(2, 5))

password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
my_password = "YOUR_PASSWORD_HERE"
for char in my_password:
    actions.move_to_element(password_input).click().send_keys(char).perform()
    time.sleep(random.uniform(0.000001,0.000005))
time.sleep(random.uniform(2, 3))
login_btn = driver.find_element(By.XPATH, '//button[contains(@data-e2e,"login-button")]').click()

##### Solving captcha
user_api_key = "YOUR_API_KEY_HERE"
number_captcha_attempts = 10
wait_captcha_seconds = 60
solve_captcha_speed = 'Normal' #Speed modes: Slow, Normal, Medium, Fast, Very Fast, Super Fast
action_type = 'tiktokWhirl'
oca_solve_captcha(driver, user_api_key, action_type, number_captcha_attempts, wait_captcha_seconds, solve_captcha_speed)
##### Solving captcha

#Check too many attempts message
is_exist_many_attemps = driver.find_elements("xpath", '//div[contains(@type,"error")]')
if len(is_exist_many_attemps) > 0:
   print('Error! Too many attemps')
time.sleep(random.uniform(15, 30))

# Close the service
driver.quit()
