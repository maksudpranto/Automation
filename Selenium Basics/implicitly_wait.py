from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
username = driver.find_element(By.ID, 'username')
username.send_keys('pranto')
