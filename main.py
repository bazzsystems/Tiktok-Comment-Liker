import os
import time
import json
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
HOW_MANY = 10  # Adjust the number of likes per video here
options = webdriver.FirefoxOptions()
options.log.level = "trace"

bot = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
bot.set_window_position(0, 0)
bot.set_window_size(414, 936)

# Initialize the driver
bot = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
bot.get("https://tiktok.com")
time.sleep(3)  # Let the page load

# Read cookies from a JSON file and add to the driver
with open('cookies.json', 'r') as f:
    cookies = json.load(f)

for cookie in cookies:
    sanitized_cookie = {key: cookie[key] for key in ['name', 'value', 'domain', 'path', 'secure', 'httpOnly', 'expirationDate'] if key in cookie}

    # Modify or remove invalid 'SameSite' attribute
    if 'SameSite' in cookie:
        if cookie['SameSite'] not in ['None', 'Lax', 'Strict']:
            print(f"Warning: Unsupported SameSite flag in cookie {cookie['name']}. Setting to 'None'.")
            sanitized_cookie['SameSite'] = 'None'
        else:
            sanitized_cookie['SameSite'] = cookie['SameSite']
        
    print(f"Adding cookie: {sanitized_cookie}")
    bot.add_cookie(sanitized_cookie)




# Confirm login by navigating to a page that requires it
bot.get("https://tiktok.com")
time.sleep(5)  # Adjust as needed

wait = WebDriverWait(bot, 10)

# Your URLs to interact with
url_file = open('urls.txt', "r")
urls = url_file.readlines()

def doesnt_exist(bot, xpath):
    try:
        bot.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    else:
        return False

# Initialize your flag
show_verify_message = True

for url in urls:
    print('--Liking comments for this post: ' + url)
    bot.get(url)
    
    # Show the verify message only once
    if show_verify_message:
        print("Verify Now 20 seconds time frame one time")
        time.sleep(20)
        show_verify_message = False  # Set flag to False to not show it again
    
    if not doesnt_exist(bot, '/html/body/div[5]/div/div/div[3]/button[2]'):
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[3]/button[2]'))).click()
        print('Closed pop-ups')
    else:
        print('No pop-up window.')
    
    # Your existing code here
    elmendt = bot.find_element(By.CSS_SELECTOR, ".tiktok-nmbm7z-ButtonActionItem:nth-child(2)")
    elmendt.click()
    time.sleep(2)
    commentss = bot.find_element(By.CSS_SELECTOR, ".tiktok-1mf23fd-DivContentContainer svg")
    commentss.click()
    time.sleep(2)
    if not doesnt_exist(bot, '.tiktok-nmbm7z-ButtonActionItem:nth-child(2)'):
        print("verifying now 20 seconds time frame one time")
        time.sleep(20)
        continue
