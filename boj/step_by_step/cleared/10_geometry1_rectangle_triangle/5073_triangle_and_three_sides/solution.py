# 목표: 세 변의 길이가 주어질 때, 삼각형의 종류를 구분하여 출력

while True:
    sides = list(map(int, input().split()))
    if not sides[0]:  # 종료 조건: 0 입력
        break
    # 삼각형의 성립 조건: 가장 긴 변의 길이 < 나머지 두 변의 길이의 합
    sides.sort()  # 오름차순 정렬
    if sides[2] >= sides[0] + sides[1]: # 삼각형이 아니면
        print('Invalid')
    else: # 삼각형이면
        set_len = len(set(sides)) 
        if set_len == 1:
            print('Equilateral')
        elif set_len == 2:
            print('Isosceles')
        else:
            print('Scalene')