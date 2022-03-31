list1 = ["Mathew", "John", "Mark", "Luke", "Paul", "Peter", "Mary", "Susan", "Margaret", "Elizabeth"]
list2 = ["Suzy", "Pascal", "Pythagoreon", "Mathew", "John", "Mark", "Muhammed", "Joshua", "Jacob"]

# Using the unique elements of a set, please create a set that contains all the elements of both lists. Without any duplicates.

my_set = set()

# This works because by default sets do not allow duplicates.

for item in list1:
    set.add(item)

for item in list2:
    set.add(item)

print(my_set)