import asyncio

def fetch(url):
    """ Make request and return result """
    pass

def worker(name, queue, results):
    """ A function to take unmade requests from a queue, perform the work, and add result to the queue """
    pass

async def distribute_work(url, requests, concurrency, results):
    """ Divide up work into batches and collect final results """
    queue = asyncio.Queue()

    # Add an item to the queue for each request we want to make
    for _ in range(requests):
        queue.put_nowait(url)

    # Create workers to match the concurrency
    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i + 1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()

    print("---")
    print(
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )

def assault(url, requests, concurrency):
    """ Entrypoint to making requests """
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)