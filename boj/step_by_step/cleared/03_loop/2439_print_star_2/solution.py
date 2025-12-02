#f-string 서식

n = int(input())
for i in range(1, n + 1):
    print(f'{"*" * i:>{n}}')