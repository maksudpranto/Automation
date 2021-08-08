from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# Right/Context Click Example

action_chain = ActionChains(driver)
click_item = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
action_chain.context_click(click_item).perform()

# Click specific options
right_click_options = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
for item in right_click_options:
    print(item.text)
    if item.text == 'Copy':
        item.click()
        break

