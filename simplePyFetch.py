#AUTHOR:        Ru1722
#PROGRAM NAME:  simplePyFetch
#DESCRIPTION:   A simple python system fetch tool
#VERSION:       1.0
#DEV NOTES:     Hopefully next version I will convert uptime into days minutes hours and seconds

import platform
import psutil
from termcolor import colored
from datetime import datetime
import time

uname = platform.uname()

#You can change color and attribute to the text below
color = 'green'
attribute = 'blink'

boot_time_timestrap = psutil.boot_time()
boottime = datetime.fromtimestamp(boot_time_timestrap)

def getUpTime():
    return time.time() - psutil.boot_time()

def upTime():
    uptimeInSeconds = getUpTime()
    return uptimeInSeconds // 60

OS = colored("OS:           ",color,attrs = [attribute])
CPU = colored("CPU:          ",color,attrs = [attribute])
Name = colored("SYSTEM NAME:  ",color,attrs = [attribute])
BT = colored("BOOT TIME:    ",color,attrs = [attribute])
UT = colored("SYSTEM UPTIME:",color,attrs = [attribute])

print(OS,platform.release())
print(CPU,platform.architecture()[0])
print(Name,platform.system())
print(BT,boottime.hour,":",boottime.minute,":",boottime.second,)
print(UT,upTime(), "minutes")

