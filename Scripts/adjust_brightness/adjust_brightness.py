#!/bin/usr/env python3

import os

brightness_level = int(input("Set brightness:"))

while brightness_level < 0 or brightness_level > 100:
    	print("Invalid number, not within 0 to 100. Enter another number.")
    	brightness_level = int(input("Set brightness:"))
	

os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{})".format(brightness_level))
