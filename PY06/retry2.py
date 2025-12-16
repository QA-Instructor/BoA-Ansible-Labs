#! venv/bin/python3
import requests
from time import sleep

if __name__ == '__main__':
    delay = 2 # initial delay between requests of 2 seconds
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response() # if the request fails with an exception, just create an empty response object as placeholder
    while response.status_code == None or response.status_code >= 500:
        if delay > 60: # if enough iterations have passed for delay to exceed 60s, give up
            print("too many failed attempts")
            break
        sleep(delay) # wait for the delay period
        try:
            response = requests.get('http://localhost:5000/api/flaky') # retry request
        except:
            response = requests.Response()
        delay *= 2 # double the delay if no successful response
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())

        # change line 6 to 10 and line 12 to 30 to see "too many failed attempts"