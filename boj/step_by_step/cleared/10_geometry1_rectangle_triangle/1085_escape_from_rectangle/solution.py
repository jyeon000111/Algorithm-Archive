# 목표: 직사각형의 경계선까지 가는 거리의 최솟값 출력
x, y, w, h = map(int, input().split())

# 경계선까지의 거리를 담을 리스트
distance = [x-0, w-x, y-0, h-y]
print(min(map(abs, distance)))
