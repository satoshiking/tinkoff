in_str = input().lower()
cleaned = ""
for i in range(len(in_str)):
    if in_str[i].isalpha():
        cleaned += in_str[i]

if cleaned == ''.join(reversed(cleaned)):
    print('YES')
else:
    print('NO')
