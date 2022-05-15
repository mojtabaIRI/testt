sudo apt update 
sudo apt install firefox -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz
tar -C /opt -xzf /tmp/geckodriver.tar.gz
chmod 755 /opt/geckodriver
ln -fs /opt/geckodriver /usr/bin/geckodriver
ln -fs /opt/geckodriver /usr/local/bin/geckodriver
sudo apt install screen -y
pip install selenium
wget -O file.py https://raw.githubusercontent.com/mojtabaIRI/testt/main/firefx.py
screen -dmS MySession
screen -S MySession -p 0 -X stuff "python file.py\n"
