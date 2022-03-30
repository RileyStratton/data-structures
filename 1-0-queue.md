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

## Try it out!

[Queue Example](1-1-example.py)

[Queue Practice](1-2-practice.py)