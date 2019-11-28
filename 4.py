# import sys
# sys.stdin = open("input.txt", "r")

x_max = 0
y_max = 0
elements = []

n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    elements.append([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)])
    if x_max < max(x1, x2):
        x_max = max(x1, x2)
    if y_max < max(y1, y2):
        y_max = max(y1, y2)

board = [[0 for y in range(y_max)] for x in range(x_max)]

for element in elements:
    x1, y1, x2, y2 = element
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1

colored = 0
for x in range(x_max):
    for y in range(y_max):
        if board[x][y] == 1:
            colored += 1

print(colored)
