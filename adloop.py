#!/usr/bin/python
import requests, urllib, random
from time import sleep
urlbase = 'http://oled:5002'
sleepTime = 30
twitter = '@hackthederby'


def main():
    while 1:
        ads = [
            twitter,
            'hackmyderby.com',
            'Mess w the best',
            'Growlers are yum',
            '*Free Hugs*'
        ]
        clearDisplay()
        message = "Master Derby V1"
        writeMessage(0,message)
        message = random.choice(ads)
        writeMessage(1,message)

        #Now we take a nap for sleepTime
        sleep(sleepTime)

def clearDisplay():
    url = urlbase + "/cls_chompit"
    r = requests.get(url)

def writeMessage(row,message):
    message = urllib.quote(message)
    url = urlbase + "/message/%s/%s" % (row,message)
    r = requests.get(url)

if __name__ == '__main__':
    main()
