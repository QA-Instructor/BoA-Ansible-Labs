#! venv/bin/python3
import requests
from time import sleep

if __name__ == '__main__':
    delay = 2 # initial delay between requests of 2 seconds
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response()
    while response.status_code == None or response.status_code >= 500:
        if delay > 60: 
            print("too many failed attempts")
            break
        # add the below line to retrieve ERROR header details
        print("Error: " + response.headers.get("ERROR", "No Error header received"))
        sleep(delay) 
        try:
            response = requests.get('http://localhost:5000/api/flaky') 
        except:
            response = requests.Response()
        delay *= 2
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())

        # change line 6 to 10 and line 12 to 30 to see "too many failed attempts"