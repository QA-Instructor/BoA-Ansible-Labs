#! venv/bin/python3
import requests

# if __name__ == '__main__':
#     response = requests.get('http://localhost:5000/api/flaky') # intentionally flaky endpoint
#     print(response.status_code)


if __name__ == '__main__':
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response() # if the request fails with an exception, just create an empty response object as placeholder
    while response.status_code == None or response.status_code >= 500:
        try:
            response = requests.get('http://localhost:5000/api/flaky')
        except:
            response = requests.Response()
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())