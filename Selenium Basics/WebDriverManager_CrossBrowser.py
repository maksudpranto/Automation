from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import time

broswerName = 'firefox'
if broswerName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif broswerName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif broswerName == 'safari':
    driver = webdriver.Safari()
elif broswerName == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Please pass the correct browse name." + broswerName)

driver.implicitly_wait(5)
driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
driver.find_element(By.ID, "user_email").send_keys('pranto@gmail.com')
driver.find_element(By.ID, "user_password").send_keys('pranto@gmail.com')
time.sleep(5)
