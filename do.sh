wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update 
sudo apt install google-chrome-stable -y
pip install webdriver-manager
pip install selenium
wget -O file.py https://raw.githubusercontent.com/mojtabaIRI/testt/main/ok.py?token=GHSAT0AAAAAABTG5FJZ43MCKB5NOQ26HZXUYT477YA
screen -dmS MySession
screen -S MySession -p 0 -X stuff "python file.py\n"
