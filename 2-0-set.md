# Set

## Overview

A set is like you smashed together a dictionary and a dynamic arrary. It takes the ability to store a list of items from a dynamic array and storing keys based on their hashes from a dictionary. Whenever you add a value to a set the value will be hashed (a mathematical function to irreversibly change strings into numbers). That value is stored at the index equal to the hash. If the value is already an integer, it is stored at the value of the integer. Sets also do not allow duplicate values to be added to the set.

Sets are used when you need check if an item is in a list. Checking if an item is in a dynamic array is an O(n) operation because it has to loop through each item to check it. Checking if something is in a set is O(1) because all you have to do is hash the value and see if that item exists at the hash location. 

This problem is rarely run into, but sometimes hashes can be the same but have different initial data, so this is often solved by storing a dynamic array at that index. While this can deteriorate performance, this problem is rarely run into.

For example, let's say that we wanted to keep a list of everyone who lives in a country. Using some sort of identifier we would add each person to the list. Now that we have this list, we want to check to see if someone lives in this country. If we had used a default dynamic array, we would have to loop through the whole list to find this person, an O(n) operation. If we had instead implemented a set, all we would have to do is hash the identifier and then check to see if that identifier exists at that index. This would be an O(1) operation. This may not be an issue if only several thousand people lived in the country, but if the country contained a billion people than an O(n) operation would be much too inefficient.

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

## Example

If you want to run this code you may visit the [Set Example](2-1-example.py). Otherwise, it will be demonstrated here.

```py
import time

my_list = list()
my_set = set()

# Adds a million items to a set and list
for n in range(1000000):
    my_list.append(n)
    my_set.add(n)

list_start_time = time.time()
if 999999 in my_list: pass
list_elapsed_time = time.time() - list_start_time

set_start_time = time.time()
if 999999 in my_set: pass
set_elapsed_time = time.time() - set_start_time

print("List elapsed time: " + str(list_elapsed_time))
print("Set elapsed time: " + str(set_elapsed_time))
```

Output

```
List elapsed time: 0.005789279937744141
Set elapsed time:  0.000000715255737304
```

The set finds the item in the list 10,000 times faster.

## Practice

[Set Practice](2-2-practice.py)

[Set Solution](2-3-solution.py)