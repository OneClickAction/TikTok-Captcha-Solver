from playwright.sync_api import sync_playwright
from ocacaptcha import oca_solve_captcha
import time
import random
import asyncio
from playwright.async_api import async_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=[
            "--no-sandbox",
            "--disable-infobars",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled",
            "--ignore-certificate-errors",
            "--start-maximized",
            "--accept-lang=en-US,en;q=0.5",
            "--disable-popup-blocking",
        ]
    )
    context = browser.new_context(
        locale="en-US"
    )

    page = context.new_page()

    # Upload website
    page.goto("https://www.tiktok.com/login/phone-or-email/email")
    time.sleep(random.uniform(8, 12))

    # Check cookies banner
    shadow_root_handle = page.evaluate_handle(
        "document.querySelector('body > tiktok-cookie-banner')?.shadowRoot"
    )
    if shadow_root_handle:
        buttons = shadow_root_handle.query_selector_all(
            "div > div.button-wrapper > button:nth-child(1)"
        )
        if buttons:
            if buttons[0].is_visible():
                buttons[0].click()
                time.sleep(random.uniform(2, 5))

    # Write login data
    email_input = page.locator('//input[@name="username"]')
    my_email = "YOUR_USERNAME_OR_EMAIL_HERE"
    email_input.click()
    for char in my_email:
        page.keyboard.type(char, delay=random.uniform(0.01, 0.05))
    time.sleep(random.uniform(2, 5))

    password_input = page.locator('//input[@type="password"]')
    my_password = "YOUR_PASSWORD_HERE"
    password_input.click()
    for char in my_password:
        page.keyboard.type(char, delay=random.uniform(0.001, 0.005))
    time.sleep(random.uniform(2, 3))
    page.locator('//button[contains(@data-e2e,"login-button")]').click()
    
    
    ##### Solving captcha
    user_api_key = "YOUR_API_KEY_HERE"
    number_captcha_attempts = 10
    wait_captcha_seconds = 60
    solve_captcha_speed = 'Normal'  # Speed modes: Slow, Normal, Medium, Fast, Very Fast, Super Fast, Random
    action_type = 'tiktokWhirl'
    oca_solve_captcha(page, user_api_key, action_type, number_captcha_attempts, wait_captcha_seconds, solve_captcha_speed)
    ##### Solving captcha

    #Check too many attempts message
    if page.locator('//div[contains(@type,"error")]').count() > 0:
        print('Error! Too many attempts')

    time.sleep(random.uniform(15, 30))

    # Close the service
    browser.close()
