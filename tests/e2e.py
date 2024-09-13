from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import sys

def test_scores_service():
    try:
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000")
        score_element = int(driver.find_element(by="id", value="score").text)
        sleep(10)
        if 1 <= score_element <= 1000:
            return True
        else:
            return False
    except NoSuchElementException as e:
        print("Element not found:", e)
    except AssertionError as e:
        print("Assertion error:", e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


def main_function():
    test_scores=test_scores_service()
    if test_scores:
        sys.exit(0)
    else:
        sys.exit(-1)




















