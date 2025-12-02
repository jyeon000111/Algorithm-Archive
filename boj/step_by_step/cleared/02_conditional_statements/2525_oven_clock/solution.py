h, m = map(int, input().split())
time = int(input())
minutes = h * 60 + m
minutes_add = minutes + time
m_add = minutes_add % 60

if minutes_add >= 60 * 24:
    h_add = minutes_add // 60 - 24
else:
    h_add = minutes_add // 60

print(h_add, m_add)