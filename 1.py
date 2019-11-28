def reverse(list_to_reverse, x, y):
    slice = list_to_reverse[x-1:y]
    slice.reverse()
    return list_to_reverse[:x-1] + slice + list_to_reverse[y:]


n, x1, y1, x2, y2 = map(int, input().split())
my_list = []
for i in range(1, n+1):
    my_list.append(i)

result = reverse(reverse(my_list, 1, 3), 3, 4)
for num in result:
    print(num, end=' ')