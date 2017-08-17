# pi-camera-web-interface
Web interface for Raspberry Pi camera

## Requirements
* Raspberry Pi
* Camera module

## Installation
1. Download pcwi-install.sh
2. Make the script executable with `sudo chmod +x pcwi-install.sh` and run with `sudo ./pcwi-install.sh`
3. Run the command `sudo visudo` to edit the sudoers file
4. Add to the end of the file: `www-data ALL=(ALL) NOPASSWD: /var/www/html/camera/camera.py`

## Usage
Make sure Apache is running and go to [your Raspberry Pi's IP address]/camera (e.g. 192.168.1.123/camera)

## Interface
![Screenshot](https://raw.githubusercontent.com/ben-woolnough/pi-camera-web-interface/master/images/interface.PNG)
