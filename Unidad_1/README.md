# Lesson 1 
## What is a distributed system?

_An distribuited system it's a state divided over multiple computers. It's not a centralized system, this system is one where  the state of your system and the program is stored on a single computer._

##### Some examples about systems using a distributed system in real world
- Domanin Name System (DNS)
- Facebook & Google use distributed systems
- Email Servers (SMTP)
- Phone Networks
> [Lesson URL](https://www.youtube.com/watch?v=7VbL89mKK3M&list=PLOE1GTZ5ouRPbpTnrZ3Wqjamfwn_Q5Y9A)
---

# Lesson 2 
## Why build a distributed system?
_On this lesson we onboard use cases on which we need to use or build a distributed system, next up are some examples of case scenarios where a distributed system would be a great approach._ 

- **Heavily intense computing applications that require a lot of processing**, for example a voice recognition system, for this type of application a distributed system would be a great choice, for example the vast majority of voice recognition system today, share the processing, first the device receiving or listening it’s only in charge of capturing the sound and sending it to a server with much more computing capacities, which is going to process the voice and return something to the other device


- **Decentralized networks** are a great example of distributed systems, this where born from the necessity of not having to rely on one server or one node, instead the network its kept alive and it’s live on each and every node of the network, a real example would be the bitcoin network it is a decentralized network with millions of nodes computing and validating each transaction.
> [Lesson URL](https://www.youtube.com/watch?v=pMQzLVK39Kk&list=PLOE1GTZ5ouRPbpTnrZ3Wqjamfwn_Q5Y9A&index=2)

---
# Leasson 3
## How to learn distributed system?

Well, in this lesson we're going to learn how to learn distributed system?, the principal idea to learn is learn by doing.
For learn distributed system, we need to learn through the experimentation and some times by taking apart, debugging, modifying an existing system.

At this time we know how to learn distributed system, the next we're gonna cover a few topics.

### Topics in Distributed Systems

- #### How systems fail

The first thing we need to have to really understand how will computers breaks. Because if we don't know how computers breaks it's hard to build a system that tolerates those breakages and keeps on working.
Well,for tolerate a failure we're gonna need a language to talk about that failure, we alredy have a common language for that situations and they are SLIs, SLOs and SLAs.
---
# Lesson 4 
> What could go wrong? 

A distributed system by its nature it is more exposed to failures and attacks, since a distributed system it is not only one device it may be a few servers on distinct locations each and single one node of the system is exposed to failure by its own, but this may be a not so bad feature of a distributed system, if a single node fails that doesn't mean he whole system goes down. Although on occasions the node that fails it’s of high importance to the system, for example a database server goes down, the entry point being attacked by a DDoS attack that overflows the whole system, but there is not only security failures there are also other problems like keeping th Up-time of the server, this implies having the economy resources to have a strong infrastructure to keep the up-time of the system
---


