## Lesson 1 
> What is a distributed system?

_An distribuited system it's a state divided over multiple computers. It's not a centralized system, this system is one where  the state of your system and the program is stored on a single computer._

##### Some examples about systems using a distributed system in real world
- Domanin Name System (DNS)
- Facebook & Google use distributed systems
- Email Servers (SMTP)
- Phone Networks
> [Lesson URL](https://www.youtube.com/watch?v=7VbL89mKK3M&list=PLOE1GTZ5ouRPbpTnrZ3Wqjamfwn_Q5Y9A)
---

## Lesson 2 
> Why build a distributed system?
_On this lesson we onboard use cases on which we need to use or build a distributed system, next up are some examples of case scenarios where a distributed system would be a great approach._ 

- **Heavily intense computing applications that require a lot of processing**, for example a voice recognition system, for this type of application a distributed system would be a great choice, for example the vast majority of voice recognition system today, share the processing, first the device receiving or listening it’s only in charge of capturing the sound and sending it to a server with much more computing capacities, which is going to process the voice and return something to the other device


- **Decentralized networks** are a great example of distributed systems, this where born from the necessity of not having to rely on one server or one node, instead the network its kept alive and it’s live on each and every node of the network, a real example would be the bitcoin network it is a decentralized network with millions of nodes computing and validating each transaction.
> [Lesson URL](https://www.youtube.com/watch?v=pMQzLVK39Kk&list=PLOE1GTZ5ouRPbpTnrZ3Wqjamfwn_Q5Y9A&index=2)

---
## Leasson 3
> How to learn distributed system?

Well, in this lesson we're going to learn how to learn distributed system?, the principal idea to learn is learn by doing.
For learn distributed system, we need to learn through the experimentation and some times by taking apart, debugging, modifying an existing system.

At this time we know how to learn distributed system, the next we're gonna cover a few topics.

### Topics in Distributed Systems

- #### How systems fail

The first thing we need to have to really understand how will computers breaks. Because if we don't know how computers breaks it's hard to build a system that tolerates those breakages and keeps on working.
Well,for tolerate a failure we're gonna need a language to talk about that failure, we alredy have a common language for that situations and they are SLIs, SLOs and SLAs.

---

## Lesson 4 
> What could go wrong? 

A distributed system by its nature it is more exposed to failures and attacks, since a distributed system it is not only one device it may be a few servers on distinct locations each and single one node of the system is exposed to failure by its own, but this may be a not so bad feature of a distributed system, if a single node fails that doesn't mean he whole system goes down. Although on occasions the node that fails it’s of high importance to the system, for example a database server goes down, the entry point being attacked by a DDoS attack that overflows the whole system, but there is not only security failures there are also other problems like keeping th Up-time of the server, this implies having the economy resources to have a strong infrastructure to keep the up-time of the system

---

## Lesson 5
> The many types of fail

There are a huge number of ways in which distributed systems can fail.

#### Network failure vs node failure

#### Network failure
- Lose packets
- Corruption
- Routing issues
- Congestion Collapse
 
TCP/IP it deals with things like multipath effects and cogestion and having to retransmit on lost packets.
Another important topic is the security, and the simple way to secure an distributed system is it's using an SSH will provide an encrypted tunnel between any two nodes. 

##### Loss of connectivity

Consider a distributed system, for example we have a generalized distributed system where every node ins't necessarily connected to every node, for this example it is a connected network. What happens if one of those nodes goes down, when that node goes away we've lost connectivity between one sub nodes and another sub nodes this is called a network partition. This is bad news for many algorithms we might be running in our distributed systems all the time.

> Partition: at least 2 components of system continue to run, but can't communicate.

#### Node failures
- Fail stop
  - Crash
  - Power outage
  - Hardware failure
  - Out of memory/disk full
- Strategies
  - Checkpoint state and restart
    - High latency
  - Replicate state and fail over
    - High cost


---

## Lesson 6

> Byzantine fault tolerance

The byzantine failure is a very specific type of failure specially on distributed systems, it’s basically a fault tolerance for when a node or more in our network gets partial failure, for example a node gets hacked, or a wrong computation etc, how it’s the rest of the network going to react, or it’s even capable of knowing about the failure, by default a distributed can’t go down that would be the worst case scenario, so it’s has to have a procedure to handle this type of failures. They exist a few ways to handle this for example verifying the result of allie nodes in out network, but that bring us to a another problematic howo our we going to confirm if that node is really an allie, and that's what is called the byzantine failure.


--- 
## Lesson 7
>  Measuring realibility and performance

When we want to build a distributed system we really want to make more realible than a centraliced system. Measure the reliability and the perform of the own system we need a vocabulary to define how well we are doing.

That vocabulary it might be a SLI, SLO, SLA just for example. These measures are to compare how the system it's doing.

Well, the key about all of this it's make your system more resistant to some hardware problems. Reduce the downtime per months and guarantee the performance.

---
## Lesson 8

>Example Projects

On this lecture two types of distributed systems are presented, both do the same thing a simple chat application, the main difference its the architecture of the systems, one it's made with a  gcp service to host applications, the second one its a custom made system, on wich we can observed how a real  distributed system works, and all the complications that were presented, showing how distributed systems are more complicated by default, it really takes a lot of work to make a state of art distributed system today.

---
## Lesson 9 
> Paxos Simplified

Paxos is a consensus protocol proposed by Leslie Lamport, It's a little bit hard to understand for most computer scientists. The principal objective is trying to agree on a value. For example we have a bunch of computers connected in diferents places and these computers need to communicate over a network connection. But all the computers need to show the same value but for obviously reason this can't happen it, because all the computers are diferent. Well the paxos protocol make an consensus for all the computers to define the value for all the computers at the same time.

---

## Lesson 10
> Time in Distributed Systems

On this lecture we have a look of how time works in distributed systems, and how hard it is to handle, we take as example the game counter strike which is a FirstPersonShooter game, this game is a distributed system that has to handle multiple players at the same time, the approach that they take it’s to have  a mechanism to try to predict the players movement, this way when the real movements get to a player are compared with the server predictions, this example show the complexity behind a distributed system, but it also shows how a distributed system can solve complex, like it a online multiplayer game        

---
## Lesson 11 
> Introduction to Blockchain Consensus

The blockchains it's here, all the problems for distributed systems are solved,this not really true, some problems are well solved with blockchain and others problems are terrible match trying solve the problem.
To use it blockchain right, we need to understand how blockchains works and when we need to use it to solve some problems. 
In the next videos we're gonna learn the bitcoin blockchains data structure.

---

## Lesson 12
> What it’s a blockchain?

On this lecture we have a introduction to what blockchain is and problem solves, so in simple words blockchain is a system that divides data or information in small chunks of data called block, each block has a identifier hash that is added to the next block in the chain so in theory every block is tied to the next block making a chain, but this chain has a purpose and it is to make every block verifiable since the hash that verifies it it’s contained on the next block and so on. 

---
## Lesson 13
> Bitcoin Blockchain Consensus

The consensus of bitcoin is really simple, in theory. Well, the strawman consensus algorithm said that any machine can join or leave at any time and any computer can create a block and these block it's replicated to all the good nodes throught the network. The requirements for bitcoin consensus are new blocks eventually replicated, newer blocks point to this new block, the consensus should be able to network partition tolerant. 

---
## Lesson 14
> Should you use Bitcoin Consensus?

The question presented on this lecture was to use or not to use the bitcoin consensus on other distributed systems, one key points to consider is that bitcoin uses proof of work to control the fact that a node can join at any time, so the bitcoin consensus uses this a proof of work to verify if a block could join the network, this is a job incharge of the miners of the network to compute the calculation and validate the  new block hash, the output of this computation will let know the network if the block can join. There’s only one constraint on how the algorithm works, and is that if multiple node a=join the network the computation needed to validate a hash is upgraded so the time it takes to compute a hash is keeps the same.    

---

## Lesson 15
> Distributed System Design (Unique ID)

Every distributed system process a thousand of transactions for multiple devices at the same time. It's need a way to manage each transaction and assign it some key or ID to identify every transaction. The simple way to solve this problem is generate an ID for every transaction with different parameters, such as, the identifier number of processor, the time of the day.

---
## Lesson 16
> The CAP Theorem

On this lesson we take on what the CAP theorem is and how is present in a distributed system and in simple words, it states that it’s really hard or almost impossible to have a distributed system that’s capable of having data consistency, high availability and partition capabilities, and how in most of distributed system is a trade off of these features, and it is chosen according to the type of need or use case your system is serving.
