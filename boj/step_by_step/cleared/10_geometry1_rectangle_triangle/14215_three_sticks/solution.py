sticks = list(map(int, input().split())) # 막대 3개의 길이

# 목표: 각 막대의 길이를 줄일 수 있을 때, 만들 수 있는 삼각형의 최대 둘레

# 삼각형의 성립 조건: 가장 긴 변의 길이 < 나머지 두 변의 길이의 합
sticks.sort()  # 오름차순 정렬

if sticks[2] >= sticks[0] + sticks[1]:
    # 가장 긴 변의 길이를 줄여야 한다.
    max_side = sticks[0] + sticks[1] - 1
    print(max_side + sticks[0] + sticks[1])

else: # 길이를 줄이지 않고 그대로 합을 출력한다.
    print(sum(sticks))