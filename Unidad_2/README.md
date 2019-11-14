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