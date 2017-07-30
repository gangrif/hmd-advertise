#!/usr/bin/python
import requests, urllib
from time import sleep
urlbase = 'http://192.168.10.2:5002'
sleepTime = 300

# # GET
# url = urlbase + "/cls_chompit"
# r = requests.get(url)
# url = urlbase + "/message/0/foo0"
# r = requests.get(url)
# url = urlbase + "/message/1/foo1"
# r = requests.get(url)


def main():
    while 1:
        clearDisplay()
        message = "Master Derby V1"
        writeMessage(0,message)
        message = "hackmyderby.com"
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





# # GET with params in URL
# r = requests.get(url, params=payload)
#
# # POST with form-encoded data
# r = requests.post(url, data=payload)
#
# # POST with JSON
# import json
# r = requests.post(url, data=json.dumps(payload))
#
# # Response, status etc
# r.text
# r.status_code
