def insert_element(l, to_insert):
    check_location = len(l) - 1
    insert_location = 0

    while check_location >= 0:
        if to_insert > l[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1

    l.insert(insert_location, to_insert)

    return l

def insertion_sort(l):
    sorted_list = []
    while len(l) > 0:
        to_insert = l.pop(0)
        sorted_list = insert_element(sorted_list, to_insert)
    return sorted_list

cabinet = [1, 2, 3, 3, 4, 6, 8, 12]

print(insertion_sort(cabinet))
