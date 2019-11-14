# Asynchronous Programming 

## An Introduction to Asynchronous Programming in Python
Asynchronous  programming it’s a hard concept in computer science and it’s more complicated to make use of it in a real scenario, on this lecture we onboard basic concepts of parallelism and concurrency all the way up to the async model. As we know async programming is a concurrent model of parallel computing in which the main process yields time or waits for new sub-tasks running concurrently to finish their processes, next up are a few examples of parallel programming making use of processes, threads and async model.  

### 1. Multiple Processes
Multi processes is the easiest way of applying parallelism, it consist of running the same program in separate processes, keeping in mind that these two programs running simultaneously  won’t be able to share common resources between them, so for certain tasks they are useless since they don't work together really well in and maybe be in some cases a resource overkill, since they a complete separate processes running in the cpu

### 2. Threading
In contrast of multiple processes multi treads can run in parallel inside the same process meaning thay can share resources, by definition a thread is a line of execution, pretty much like a process, but you can have multiple threads in the context of one process and they all share access to common resources.

In python we can access threading really easy by importing threading module
`import threading`

A mayor disadvantage for using threads is that is really hard to cordinate them, meaning there is no other mechanisim to control them, so can be very challenging to make concurrent code only using threads 

### Coroutines
Coroutines and concurrency go hand by hand. Coroutines are a general control structure in wich flow control is cooperatively passed between two different routines without returning.

The 'yield' statement in Python is a good example. It creates a coroutine. When the 'yield ' is encountered the current state of the function is saved and control is returned to the calling function. The calling function can then transfer execution back to the yielding function and its state will be restored to the point where the 'yield' was encountered and execution will continue.

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

#### Synchronous version

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