from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://miner.eo.finance")
driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'userId', 'path': '/', 'secure': False, 'value': '922240272'})

driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'token', 'path': '/', 'secure': False, 'value': '0cb6cd98f8f46770c5002f06e39751a87dd85ca7545f1e0b263a572932b9b413e2ffe17896f508dd8e98362619a4e9d22f0406bba48d12c5f01ed727f15ef931'})
driver.refresh()
while True:
    sleep(5)
    print(driver.find_element(By.ID,'hashes-per-second').text)
