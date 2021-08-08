from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://courses.letskodeit.com/login")
wait = WebDriverWait(driver, 10)
wait.until(ec.title_is("Login"))

print(driver.title)
wait = WebDriverWait(driver, 10)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'email')))
email_id.send_keys('maksudpranto')
password = driver.find_element(By.ID, 'password')
password.send_keys('pranto')
