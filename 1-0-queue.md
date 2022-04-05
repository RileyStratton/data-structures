# Queue

## Overview

Queues are very similar to dynamic arrays. Queues are very often made using built in dynamic array structures. Queues are used when you need to process information in a FIFO (first in, first out) order.

Let's visualize this by imagining a line of people waiting to check out at a grocery store. The people next to the cashier are the front of the line, and the people furthest are the back. When someone joins the line, it is called "enqueue" operation. When someone gets checked out and leaves the line, it is called a "dequeue" operation. 

## Common Operations

### Enqueue

* This operation will add a value to the back of the list.
* Using "Big O Notation," this is an O(1) operation.
* In Python, this is done by using the ```list.append(value)``` method.

### Dequeue

* This operation will remove the first value from the front of the list.
* Depending on what type of underlying data structure you use will determine the "Big O" of this function.
* Using a dynamic array will provide O(n), because all items in the list must be moved forward one index.
* In Python, this is done by using the ```list.pop(0)``` method.
* Using a linked list (not in this tutorial) will lead to performance of O(1)

### Size 

* This is an O(1) function. The list class will keep track of it's size and return the value
* This is done in Python by using the ```len(list)``` function

### Empty

* This is an O(1) function as well. 
* In Python, this is done by checking if the length of the list is 0. ```len(list) == 0```

## Example

If you want to run this code you may visit the [Queue Example](1-1-example.py). Otherwise, it will be demonstrated here.

```py
class CustomerService:

    class Ticket:

        def __init__(self, name, problem):

            self.name = name
            self.problem = problem

        def __str__(self):

            return self.name + ": " + self.problem

    def __init__(self):

        self.queue = list()

    def create_ticket(self, name, problem):

        ticket = CustomerService.Ticket(name, problem)
        self.queue.append(ticket)

    def process_ticet(self):

        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print ("There are no tickets to process")

    def __str__(self):

        result = "["
        for ticket in self.queue:
            result += "{"+str(ticket)+"}"
            result += ", "
        result += "]"
        return result



# Test code

customer_service = CustomerService()
customer_service.create_ticket("John", "iPhone not working")
customer_service.create_ticket("Mary", "Broken monitor")
customer_service.create_ticket("Peter", "No internet")
print(customer_service)
customer_service.process_ticet()
customer_service.process_ticet()
customer_service.process_ticet()
customer_service.process_ticet()
print(customer_service)
```

Output

```
[{John: iPhone not working}, {Mary: Broken monitor}, {Peter: No internet}, ]
John: iPhone not working
Mary: Broken monitor
Peter: No internet
There are no tickets to process
[]
```

## Practice

Using the starting code, implement the request_call and process_call functions so that the calls are processed in first in first out order, except 911 should go first (can be accomplished by being processed first or adding it to the front of the queue, however you decide to implement it).

[Queue Practice](1-2-practice.py)

[Queue Solution](1-3-solution.py)