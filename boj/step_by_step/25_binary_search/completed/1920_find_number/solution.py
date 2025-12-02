# 목표: N개의 정수 중 X가 존재하면 1 출력, 존재하지 않으면 0 출력

N = int(input())
arr = list(map(int, input().split()))

M = int(input()) # 탐색할 X의 개수
target_list = list(map(int, input().split()))

# 이진 탐색을 위해 탐색할 배열 오름차순 정렬
arr.sort()

for target in target_list:
    left = 0
    right = N - 1
    found = False  # 탐색 성공 플래그
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            found = True
            print(1)
            break  # while 종료
        elif target < arr[mid]:  # 타겟이 왼쪽에 있을 때
            right = mid - 1
        else:  # 타겟이 오른쪽에 있을 때
            left = mid + 1
    if found:
        continue  # 다음 탐색으로 넘어가기
    print(0)