#!/usr/bin/python
#show IP address on the LCD Plate at startup
#Meandean

import Adafruit_CharLCD as LCD
import time
import subprocess
  # lint:ok

lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output("hostname").strip()
displayText = Name
  # lint:ok

IP = subprocess.check_output(["hostname", "-I"])
refresh = True


while(True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText + "\n")
        lcd.set_backlight(1)
        lcd.message("Hello World\n")
        refresh = True

    else:
        if refresh:
            lcd.clear()
            lcd.set_backlight(1)
            lcd.message(displayText + "\n")
            lcd.message(IP)
            refresh = False
    time.sleep(0.5)












