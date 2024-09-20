from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from time import sleep

def test_scores_service(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    chrome_options.binary_location = '/usr/bin/google-chrome'
    driver = webdriver.Chrome(service=Service('/venv/bin/chromedriver-linux64/chromedriver'), options=chrome_options)
    try:
        driver.get(url)
        score_element = int(driver.find_element(by="id", value="score").text)
        sleep(10)
        if 1 <= score_element <= 1000:
            return True
        else:
            return False
            
    except NoSuchElementException as e:
        print("Element not found:", e)
    except TimeoutException as e:
        print("TimeoutException error:", e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


def main_function(url):
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(-1)
