# 🚀 TikTok Captcha Solver

[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-supported-brightgreen.svg)](https://www.selenium.dev/)
[![Playwright](https://img.shields.io/badge/playwright-supported-orange.svg)](https://playwright.dev/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/OneClickAction?style=social)](https://github.com/OneClickAction)

> 🔓 Automate TikTok login and bypass captchas using **Selenium** or **Playwright** + [OCA Captcha](https://t.me/OneClickActionBot)

---

## ✨ Features

- ✅ Automatic TikTok login
- ✅ Support for **Selenium** and **Playwright**
- ✅ Auto-filling of login credentials
- ✅ Captcha solving via `oca_solve_captcha`
- ✅ Easy integration with [OCA Captcha API](https://t.me/OneClickActionBot)

---

## ⚡ Requirements

- Python **3.13.1+**  
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) (only for Selenium)  
- Selenium (for `TikTok Captcha Solver with Selenium.py`)  
- Playwright (for `TikTok Captcha Solver with Playwright.py`)  
- 🔑 API key for **ocacaptcha**  

---

## 📥 Installation

### 🔹 Option 1: Selenium

```bash
git clone https://github.com/OneClickAction/TikTok-Captcha-Solver-Selenium.git
cd TikTok-Captcha-Solver-Selenium
pip install selenium ocacaptcha
```

➡️ Download and install **ChromeDriver** compatible with your Chrome version

### 🔹 Option 2: Playwright

```bash
git clone https://github.com/OneClickAction/TikTok-Captcha-Solver-Playwright.git
cd TikTok-Captcha-Solver-Playwright
pip install playwright ocacaptcha
```

---

## 🚀 Usage

### 🔹 Selenium

1. Set your login credentials and API key:

```python
my_email = "YOUR_USERNAME_OR_EMAIL_HERE"
my_password = "YOUR_PASSWORD_HERE"
user_api_key = "YOUR_API_KEY_HERE"
```

2. Update the **ChromeDriver** path:

```python
service = Service(executable_path="/path/to/your/chromedriver")
```

### 🔹 Playwright

1. Set your login credentials and API key:

```python
my_email = "YOUR_USERNAME_OR_EMAIL_HERE"
my_password = "YOUR_PASSWORD_HERE"
user_api_key = "YOUR_API_KEY_HERE"
```

---

## 🔑 Getting Your OCA API Key

1. Open the [Telegram bot](https://t.me/OneClickActionBot)
2. Send the `/start` command
3. Choose **English** or **Russian** language
4. Go to **Another services** menu
5. Select **Captcha** and get your API key
6. Copy your **API key** and paste it into your script

---

## 📦 Dependencies

- **Selenium**
- **Playwright**
- **ocacaptcha**

---

## 📞 Contact

For support or business inquiries:

- **Admin**: OCA Team
- **Email**: oneclickactionsoft@gmail.com
- **GitHub**: [One Click Action](https://github.com/OneClickAction)
- **Telegram**: [One Click Action](https://t.me/+70DIlIc543U4NGQy)
- **Discord**: [One Click Action](https://discord.com/invite/YyDx3SJNCh)
- **YouTube**: [OCA Soft](https://www.youtube.com/@ocasoft)

---

💡 **Take action now:** Automate your TikTok login and let OCA Captcha handle the hard part 🔥
