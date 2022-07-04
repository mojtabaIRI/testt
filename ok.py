import websocket,json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

m = '{"token":null,"v":3,"action":"login","ns":"7","message":{"login":"mojtabasafaee211@gmail.com","password":"12786Moj"},"subscribe":false}'
ws = websocket.WebSocket()


def req_browser():
    while True:
        try:
            ws.connect("wss://ws.eo.finance/ws/")
            ws.send_binary(m.encode())
            k = ws.recv()
            if len(k) == 0:
                continue
            data = json.loads(k.decode())
            token = data['message']['token']
            user_id = data['message']['user_id']
            break
        except:
            continue
    print(f"\n[!] token = {token}\n")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get("https://miner.eo.finance")
    driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'userId', 'path': '/', 'secure': False, 'value': str(user_id)})
    driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'token', 'path': '/', 'secure': False, 'value': token})
    driver.refresh()
    return driver


driver = req_browser()
driver2 = req_browser()
while True:
    sleep(5)
    print(int(driver.find_element(By.ID,'hashes-per-second').text)+int(driver2.find_element(By.ID,'hashes-per-second').text))
    print(f"\nbalance1 = {driver.find_element(By.ID,'balanceTotal').text}\nbalance2 = {driver2.find_element(By.ID,'balanceTotal').text}")
    
