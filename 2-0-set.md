# Set

## Overview

A set is like you smashed together a dictionary and a dynamic arrary. It takes the ability to store a list of items from a dynamic array and storing keys based on their hashes from a dictionary. Whenever you add a value to a set the value will be hashed (a mathematical function to irreversibly change strings into numbers). That value is stored at the index equal to the hash. If the value is already an integer, it is stored at the value of the integer. Sets also do not allow duplicate values to be added to the set.

Sets are used when you need check if an item is in a list. Checking if an item is in a dynamic array is an O(n) operation because it has to loop through each item to check it. Checking if something is in a set is O(1) because all you have to do is hash the value and see if that item exists at the hash location. 

This problem is rarely run into, but sometimes hashes can be the same but have different initial data, so this is often solved by storing a dynamic array at that index.

## Common Operations

### Add

* This operation will add an item to the set, and is an O(1) operation.
* In Python this is done with ```set.add(value)```

### Remove

* This operation is also O(1)
* In Python you use ```set.remove(value)```

### Check Membership

* This was touched on earlier as well, this is an O(1) operation
* Using Python, you can check membership with ```if value in set:```

### Size

* Sets keep track of their size and store it in a variable, making this an O(1) operation.
* Just like other Python data structures, you check this using ```len(set)```.

## Try it out!

[Set Example](2-1-example.py)

[Set Practice](2-2-practice.py)