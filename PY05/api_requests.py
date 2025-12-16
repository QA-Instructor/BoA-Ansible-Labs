#! venv/bin/python3
import requests


if __name__ == '__main__':
    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."} # add this line
    p = requests.post('http://localhost:5000/api/books', json=book) # and this line
    print(p.status_code, p.text)
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())