import threading
import time
from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# User input
num_urls = int(input("How many URLs do you want to collect? "))
num_threads = 1
file_option = input("Do you want to add to the file or overwrite it? (add/overwrite): ")

# Initialize driver only once
executable_path = "geckodriver.exe"

# Thread-safe queue
collected_urls = Queue()

def collect_url(thread_id, num_urls_per_thread):
    options = webdriver.FirefoxOptions()
    # Uncomment the following line to run in headless mode
    # options.headless = True
    driver = webdriver.Firefox(executable_path=executable_path, options=options)
    driver.get("https://www.tiktok.com/foryou")
    
    time.sleep(2)
    
    # Dismiss the pop-up
    try:
        popup = driver.find_element(By.CSS_SELECTOR, ".tiktok-1anes8e-StyledIcon")
        popup.click()
        time.sleep(1)
    except NoSuchElementException:
        print("No popup found.")
        
    # Click on the first video
    try:
        first_video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-e2e="feed-video"]'))
        )
        first_video.click()
        time.sleep(2)
    except (NoSuchElementException, TimeoutException):
        print("First video not found or not clickable. Exiting thread.")
        driver.quit()
        return
    print("verify now 20 seconds time frame one time")
    time.sleep(20)
    for i in range(num_urls_per_thread):
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-e2e="arrow-right"]'))
            )
            next_button.click()
            time.sleep(2)
            
            current_url = driver.current_url
            collected_urls.put(current_url)
            print(f"Thread-{thread_id} Collected URL {i+1}: {current_url}")
            
        except (NoSuchElementException, TimeoutException):
            print(f"Element not found or not clickable. Skipping...")
            break
    
    driver.quit()

# Create threads
threads = []
for i in range(num_threads):
    num_urls_per_thread = num_urls // num_threads
    t = threading.Thread(target=collect_url, args=(i, num_urls_per_thread))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Save URLs to a file
urls_list = list(collected_urls.queue)
with open("urls.txt", "a" if file_option == "add" else "w") as f:
    for url in urls_list:
        f.write(f"{url}\n")

print(f"Collected URLs: {urls_list}")
