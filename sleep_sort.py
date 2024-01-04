import threading
from time import sleep


def sleep_sort(i):
    sleep(i)
    global sorted_list
    sorted_list.append(i)
    return i


items = [2, 4, 5, 2, 1, 7]
sorted_list = []
for i in items:
    threading.Thread(target=sleep_sort, args=(i,)).start()

while len(sorted_list) < len(items):
    pass

print(sorted_list)
