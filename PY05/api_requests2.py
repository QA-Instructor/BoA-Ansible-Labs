#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth # add this import


if __name__ == '__main__':
    auth = HTTPDigestAuth('learner', 'p@ssword') # provide username and password
    token = requests.post('http://localhost:5000/auth/tokens', auth=auth) # make a request to get a token
    print(token.text) # display token value
    t_auth_headers = {"Authorization": f"Bearer {token.text}"} 

    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "A gripping high-fantasy wuth thriller elements"} # add this line
    # book = {"id": "0000012345"} # add this line
    p = requests.post('http://localhost:5000/api/books', json=book, headers=t_auth_headers) # and this line
    # p = requests.put('http://localhost:5000/api/books', json=book, headers=t_auth_headers) # and this line
    # p = requests.delete('http://localhost:5000/api/books', json=book, headers=t_auth_headers)
    # print(p.status_code, p.text)
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())