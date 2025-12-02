# 목표: 세 점이 주어졌을 때, 직사각형을 만들기 위해 필요한 네 번째 점을 출력
c1, r1 = map(int, input().split())
c2, r2 = map(int, input().split())
c3, r3 = map(int, input().split())

# 같은 좌표가 2번씩, 짝수 개만큼 존재해야 한다.
# 홀수인 c좌표, r좌표를 출력한다.
c_list = [c1, c2, c3]
r_list = [r1, r2, r3]

for c in c_list:
    if c_list.count(c) % 2 == 1:
        print(c, end=' ')
for r in r_list:
    if r_list.count(r) % 2 == 1:
        print(r)