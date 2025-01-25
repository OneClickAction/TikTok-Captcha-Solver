# TikTok Captcha Solver
This project automates the login process on TikTok using Selenium WebDriver. It also includes functionality to handle captchas using the `ocacaptcha` library.

## Features

- Automated login to TikTok
- Handling of cookies banner
- Automatic filling of login credentials
- Solving captchas using `oca_solve_captcha` function from `ocacaptcha` library

## Prerequisites

- Python >= 3.11
- ChromeDriver
- A valid API key for `ocacaptcha`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/OneClickAction/TikTok-Captcha-Solver.git
   cd TikTok-Captcha-Solver
   
2. Install the required Python packages:
   ```bash
   pip install selenium ocacaptcha
   
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
   

## Dependencies
- Selenium
- ocacaptcha


## Contact
For any questions or issues, please contact:

- OCA admin
- Email: oneclickactionsoft@gmail.com
- GitHub: [One Click Action](https://github.com/OneClickAction)
- Telegram [One Click Action](https://t.me/+70DIlIc543U4NGQy)
- Discord [One Click Action](https://discord.com/invite/YyDx3SJNCh)
- YouTube [One Click Action](https://www.youtube.com/@ocasoft)
