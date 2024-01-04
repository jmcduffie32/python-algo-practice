import math


def merging(left, right):
    new_list = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            new_list.append(right.pop(0))
        elif right[0] >= left[0]:
            new_list.append(left.pop(0))

    if len(left) > 0:
        for el in left:
            new_list.append(el)

    if len(right) > 0:
        for el in right:
            new_list.append(el)

    return new_list

def merge_sort(l):
    new_l = []
    if len(l) == 1:
        new_l = l

    else:
        left = merge_sort(l[:len(l) // 2])
        right = merge_sort(l[len(l) // 2:])
        new_l = merging(left, right)
        
    return new_l


print(merge_sort([2,1,5, -9, 10]))
