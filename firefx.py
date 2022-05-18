import websocket,json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.FirefoxOptions()
options.add_argument('--headless')


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
    driver = webdriver.Firefox(options=options)
    driver.get("https://miner.eo.finance")
    driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'userId', 'path': '/', 'secure': False, 'value': str(user_id)})
    driver.add_cookie({'domain': '.eo.finance', 'expiry': 1967784870, 'httpOnly': False, 'name': 'token', 'path': '/', 'secure': False, 'value': token})
    driver.refresh()
    return driver

driver = req_browser()
driver2 = req_browser()
while True:
    sleep(5)
    print(int(driver.find_element(By.ID,'hashes-per-second').text)+int(driver.find_element(By.ID,'hashes-per-second').text))
    
   
