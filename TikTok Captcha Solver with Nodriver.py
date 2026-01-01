import asyncio
from nodriver import start
from ocacaptcha import oca_solve_captcha_async

    
##### Solving captcha
user_api_key = "YOUR_API_KEY_HERE"
number_captcha_attempts = 10
wait_captcha_seconds = 60
solve_captcha_speed = 'Normal'  # Speed modes: Slow, Normal, Medium, Fast, Very Fast, Super Fast, Random
action_type = 'tiktokWhirl'
await oca_solve_captcha_async(tab, user_api_key, action_type, number_captcha_attempts, wait_captcha_seconds, solve_captcha_speed)
##### Solving captcha
