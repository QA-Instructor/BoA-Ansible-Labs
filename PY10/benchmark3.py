#! venv/bin/python3
import timeit

def test_sync():
    results = timeit.repeat('sync.main()', setup='import sync_client as sync', repeat=5, number=5)
    avg_sync_time = sum(results) / 25
    return avg_sync_time


def test_async():
    results = timeit.repeat('asyncio.run(asyn.main())', setup='import async_client as asyn\nimport asyncio', repeat=5, number=5)
    avg_async_time = sum(results) / 25
    return avg_async_time


if __name__ == '__main__':
    avg_time_sync = test_sync()
    avg_time_async = test_async()
    print(f"Execution time (synchronous): {avg_time_sync}")
    print(f"Execution time (asynchronous): {avg_time_async}")