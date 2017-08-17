import picamera, sys
from subprocess import call
from datetime import datetime

camera = picamera.PiCamera()

# Set the filename
filename = "/var/www/html/camera/pictures/new.jpg"

# Set the image resolution
camera.resolution = (720, 480)

# Set the brightness to the value of the first command-line argument
try:
    camera.brightness = int(sys.argv[1])
except:
    camera.brightness = 50

print("Taking picture...")

# Take the picture
camera.capture(filename)

# Time picture was taken
currentTime = datetime.now()

print("Adding timestamp...")

# Formatted timestamp
timestampMessage = str(currentTime.strftime("%Y.%m.%d-%H:%M:%S"))

timestampCommand = "/usr/bin/convert " + filename + " -pointsize 24 \
-fill red -annotate +480+30 '" + timestampMessage + "' " + filename

# Call the command to timestamp the image
call([timestampCommand], shell=True)

print("Done")
