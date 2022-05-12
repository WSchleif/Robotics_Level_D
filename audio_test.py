import os

os.system("gpio -g mode 18 ALT5")
os.system("aplay /home/pi/hello_42.wav")
os.system("gpio - mode 18 in")