# 목표: 삼각형의 세 각이 주어졌을 때, 삼각형의 종류 구분하여 출력

angles = [int(input()) for _ in range(3)]

# 1. 세 각의 합이 180이 아니면 Error 출력
if sum(angles) != 180:
    print('Error')
else:  # 세 각의 합이 같은 경우,
    set_len = len(set(angles))
    # 2. 세 각의 크기 모두 같은 경우
    if set_len == 1:
        print('Equilateral')
    # 3. 두 각이 같은 경우
    elif set_len == 2:
        print('Isosceles')
    # 4. 같은 각이 없는 경우
    else:
        print('Scalene')
