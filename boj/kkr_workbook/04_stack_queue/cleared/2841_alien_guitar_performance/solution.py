import sys
input = sys.stdin.readline
# 목표: 멜로디 연주에 필요한 최소 손가락 움직임 출력
result_cnt = 0
# 프렛을 한 번 누르거나 떼는 것을 움직임 1번으로 카운트
# 어떤 줄의 프렛 여러 개 누르고 있다면, 가장 높은 프렛의 음이 발생

N, P = map(int, input().split())  # N은 멜로디를 구성하는 음의 수, P는 한 줄에 있는 프렛 수
fret_stack = [[] for _ in range(N+1)]  # 줄 번호를 인덱스로, 현재 누르고 있는 fret 위치를 스택으로 저장

for _ in range(N):
    string, fret = map(int, input().split())  # 줄 번호, 눌러야 하는 프렛 번호
    # 1. fret보다 크면, 같거나 작아질 때까지 손가락 떼기
    while fret_stack[string]:  # 스택에 프렛이 있으면 반복
        if fret_stack[string][-1] <= fret:
            break
        fret_stack[string].pop()
        result_cnt += 1

    # 2. 해당 줄에 누르고 있는 프렛이 있으면
    if fret_stack[string]:
        # 2) 마지막 값이 fret과 같으면 => 움직일 필요 없음
        if fret_stack[string][-1] == fret:
            continue
        # 3) fret보다 작으면 stack에 추가하고, 움직임 1번 카운트
        elif fret_stack[string][-1] < fret:
            fret_stack[string].append(fret)
            result_cnt += 1

    # 3. 누르고 있는 프렛이 없으면 추가하고, 움직임 1번 카운트
    else:
        fret_stack[string].append(fret)
        result_cnt += 1

print(result_cnt)



