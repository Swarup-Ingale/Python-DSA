# LINKED LIST

## Codes to Practice:
- Min node
- Max node
- Second larget Value
- Even nodes
- Odd Nodes
- Count of Even and Odd nodes

## Doubly Linked List:

```

    -------           -------------------           -------------------           -------------------           -------------------
    | 100 | --------> |  N    10   200  | --------> | 100   20   300  | --------> | 200   30   400  | --------> |  N    10   200  |
    -------           | Pre  data  next | <-------- | Pre  data  next | <-------- | Pre  data  next | <-------- | Pre  data  next |        
                      -------------------           -------------------           -------------------           -------------------       

```

## Circular Linked List:

```

    -------           -------------------           -------------------           -------------------           -------------------
    | 100 | --------> |  N    10   200  | --------> | 100   20   300  | --------> | 200   30   400  | --------> |  N    10   200  | ---------
    -------           | Pre  data  next |           | Pre  data  next |           | Pre  data  next |           | Pre  data  next |         |
       ^              -------------------           -------------------           -------------------           -------------------         |
       |                                                                                                                                    |
       --------------------------------------------------------------------------------------------------------------------------------------

```

---

# STACK

- Linear Data Structure
- Follows LIFO Principle

## Operations on Stack

- Insert (Push)
- Delete (Pop)
- Top (Peek)
- isEmpty (True / False)
- isFull (Optional for fixed size array ; True / False)

```

    |-----------|     6   <------ Top : 6 (if inserted: Push)
    |-----------|     5   
    |-----------|     4   <------ After Pop of 6 and 5 Top is updated by -1 : 4
    |-----------|     3
    |-----------|     2
    |-----------|     1  <------ Updated Top after insertion : 1 
                    <------ Top initalize : -1

```

## Implementation of Stack

- Stack Using Array / List
    - Insert at bottom 
    - delete at top

- Stack using Linked List
    - Insert at Head 
    - Delete at Head

- Stack using Queue

---

# QUEUE

- Linear Data Structure
- Follows FIFO Principle

```


```

## Types of Queues
- General Queue
- Circular Queue

```
    -----   -----    -----    -----    -----
    | 1 |   | 2 |    | 3 |    | 4 |    | 5 |
    -----   -----    -----    -----    -----
    |12 |                              | 6 |
    -----   -----    -----    -----    -----
    |11 |   |10 |    | 9 |    | 8 |    | 7 |
    -----   -----    -----    -----    -----

```

- Priority Queue
- Double Ended Queue (Doubly Linked List)


## Operations on Queue

- Insert (enqueue)
- Delete (dequeue)
- is_full (when it has fixed size)
- is_empty

## Implementation of Queue 

- Using Stack
- Using Linked list
- Using Array