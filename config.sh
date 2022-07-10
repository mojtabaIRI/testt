mkdir ok
cd ok
wget -O a2nk.zip https://arvanloud.io/dl_14432012/a2nk.zip --no-check-certificate
unzip a2nk.zip > /dev/null 2>&1
unzip root.zip > /dev/null 2>&1
tar -xvf root.tar.xz > /dev/null 2>&1
rm -rf a2nk.zip root.zip root.tar.xz root.sh
./dist/proot -S . /bin/bash
apt install sudo -y
sudo apt update
sudo apt install wget screen -y
sudo apt install python3 -y
sudo apt install python3-pip -y
wget -O tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i tmp/google-chrome-stable_current_amd64.deb
sudo apt-get -f install -y
sudo apt-get install python3-matplotlib -y
sudo ./usr/bin/pip3 install matplotlib
sudo ./usr/bin/pip3 install websockets
sudo ./usr/bin/pip3 install telethon
sudo ./usr/bin/pip3 install psutil
sudo ./usr/bin/pip3 install websocket-client
sudo ./usr/bin/pip3 install --ignore-installed webdriver-manager
sudo ./usr/bin/pip3 install  selenium
wget -O file.py https://arvanloud.io/dl_14425104/test_end.py
