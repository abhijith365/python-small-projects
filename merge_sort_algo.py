def merge(list1, list2):
    new_list = list()
    a = 0
    b = 0

    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            new_list.append(list1[a])
            a += 1

        else:
            new_list.append(list2[b])
            b += 1

    while a < len(list1):
        new_list.append(list1[a])
        a += 1

    while b < len(list2):
        new_list.append(list2[b])
        b += 1
    return new_list


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        new_list = merge(left, right)
        return new_list


a = [10, 5, 6, 30, 32, 22, 55, 60, 100, 99, 88, 76, 98]

print(merge_sort(a))
