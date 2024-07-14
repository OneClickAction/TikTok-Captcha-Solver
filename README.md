# TikTok-Captcha-Solver
This project automates the login process on TikTok using Selenium WebDriver. It also includes functionality to handle captchas using the `ocacaptcha` library.

## Features

- Automated login to TikTok
- Handling of cookies banner
- Automatic filling of login credentials
- Solving captchas using `oca_solve_captcha` function from `ocacaptcha` library

## Prerequisites

- Python 3.x
- ChromeDriver
- A valid API key for `ocacaptcha`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tiktok-automation.git
   cd tiktok-automation
   
2. Install the required Python packages:
   ```bash
   pip install selenium ocacaptcha requests
   
3. Download and install [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) compatible with your version of Chrome, and place it in your desired directory.

## Usage
1. Update the script with your own login credentials and API key:
   ```
   my_email = "your_email@example.com"
   my_password = "your_password"
   user_api_key = "your_ocacaptcha_api_key"

2. Update the ChromeDriver path:
   ```
   service = Service(executable_path='/path/to/your/chromedriver')
   
3. Update the ChromeDriver path:
   ```
   python tiktok_automation.py

## Dependencies
- Selenium
- ocacaptcha
- Requests


## Contact
For any questions or issues, please contact:

- Your Name
- Email: your_email@example.com
- GitHub: [yourusername](https://github.com/OneClickAction)
