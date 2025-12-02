a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    print(max(a, b, c) * 100)
else:
    if a == b or a == c:
        equal_num = a
    else:
        equal_num = b
    print(1000 + equal_num * 100)