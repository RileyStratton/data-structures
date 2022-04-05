list1 = ["Mathew", "John", "Mark", "Luke", "Paul", "Peter", "Mary", "Susan", "Margaret", "Elizabeth"]
list2 = ["Suzy", "Pascal", "Pythagoreon", "Mathew", "John", "Mark", "Muhammed", "Joshua", "Jacob"]

my_set = set()

# This works because by default sets do not allow duplicates.

for item in list1:
    my_set.add(item)

for item in list2:
    my_set.add(item)

print(my_set)