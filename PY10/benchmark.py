#! venv/bin/python3
import timeit

def test_sync():
    result = timeit.timeit('sync.main()', setup='import sync_client as sync', number=1)
    return result

if __name__ == '__main__':
    time_sync = test_sync()
    print(f"Execution time (synchronous): {time_sync}")