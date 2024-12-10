import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class PG2:
    def assignment(self):
        driver = webdriver.Edge()
        url = "https://www.pos.com.my/send/ratecalculator"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver,10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        fromCode = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="postcodeFrom"]')))
        fromCode.send_keys("35600")

        toCode= wait.until(EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="postcodeTo"]')))
        toCode.send_keys("70594")

        Weight= wait.until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="eg. 0.1kg"]')))
        Weight.send_keys("15")

        driver.find_element(By.XPATH, "//a[normalize-space()='Calculate']").click();

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        bookingAmount= wait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='RM 41.32']")))

        assert bookingAmount.text == "RM 41.32"

        time.sleep(3)

        driver.close()


dd = PG2 ()
dd.assignment()

