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



# Test code

print("List elapsed time: " + str(list_elapsed_time))
print("Set elapsed time: " + str(set_elapsed_time))