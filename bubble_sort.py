def bubble_sort(list):
    for _ in list:
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                tmp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = tmp
    return list


list = [8, 4, 7, 3, 5, 1, 9, 2, 6]

print(bubble_sort(list))