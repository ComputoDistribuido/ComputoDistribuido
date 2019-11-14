# Asynchronous Programming 

## An Introduction to Asynchronous Programming in Python
Asynchronous  programming it’s a hard concept in computer science and it’s more complicated to make use of it in a real scenario, on this lecture we onboard basic concepts of parallelism and concurrency all the way up to the async model. As we know async programming is a concurrent model of parallel computing in which the main process yields time or waits for new sub-tasks running concurrently to finish their processes, next up are a few examples of parallel programming making use of processes, threads and async model.  

### 1. Multiple Processes
Multi processes is the easiest way of applying parallelism, it consist of running the same program in separate processes, keeping in mind that these two programs running simultaneously  won’t be able to share common resources between them, so for certain tasks they are useless since they don't work together really well in and maybe be in some cases a resource overkill, since they a complete separate processes running in the cpu


## Async IO
This short program is the Hello World of async IO
#### Asynchronous version

```python
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```
The order of this output is the heart of async IO. Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await the function talks to the event loop and gives control back to it.

![count1](count1.png)

#### Synchronous version**

```python
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

These functions time.sleep() and asyncio.sleep() they are used as stand for any time-intensive processes that involve wait time. The function time.sleep() can represent any time consuming blocking function call, while asyncio.sleep() is used to stand in for a non-blocking call.
![count2](count2.png)

