#!/bin/bash
sudo apt-get install apache2 -y
sudo apt-get install php5 libapache2-mod-php5 -y
sudo apt-get install imagemagick -y

sudo mkdir /var/www/html/camera
sudo git clone https://github.com/ben-woolnough/pi-camera-web-interface /var/www/html/camera
sudo chmod +x /var/www/html/camera/camera.py
sudo mkdir /var/www/html/camera/pictures
