#! venv/bin/python3
import requests
import asyncio
# from time import sleep

ids = [
    "0000012345",
    "0000012346",
    "0000012347",
    "0000012348",
    "0000012349",
    "0000012350"
]

async def get_book(iq, books, bq):
    i = await iq.get()
    book = dict()
    for b in books:
        if b.get("id", '') == i:
            book = b
            break
    await bq.put(book)

async def process_book_data(queue):
    book = await queue.get()
    bookstr = ""
    bookstr += f"ID: {str(book.get('id', ''))}\n"
    bookstr += f"TITLE: {book.get('title', '')}\n"
    bookstr += f"GENRE: {book.get('genre', '')}\n"
    await asyncio.sleep(1)
    print(bookstr)

async def main():
    books = requests.get('http://localhost:5000/api/books').json()
    books_queue = asyncio.Queue()
    ids_queue = asyncio.Queue()
    for i in ids:
        await ids_queue.put(i)
    gets = [get_book(ids_queue, books, books_queue) for i in ids ]
    procs = [process_book_data(books_queue) for i in ids]
    await asyncio.gather(*gets)
    await asyncio.gather(*procs)


if __name__ == '__main__':
    asyncio.run(main())

