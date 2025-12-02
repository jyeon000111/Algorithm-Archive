# 목표: T초를 맞추기 위해 5분, 1분, 10초 버튼을 최소로 누르려면 각각 몇 번 눌러야 하는가.
T = int(input())  # 요리시간 (초)

# 최소 버튼 조작을 위해 시간 단위가 가장 큰 버튼부터 눌러야 한다. (Greedy 알고리즘)
# 각 시간 단위가 서로 나누어 떨어지므로, 단위가 큰 버튼부터 누르는 규칙이 성립한다.

# A, B, C 버튼의 지정된 시간을 리스트에 담는다. (초 단위로 변환)
abc_buttons = [300, 60, 10]
# 누르는 횟수도 리스트에 담아야 한다. (0으로 초기화)
button_cnt = [0] * 3

# 인덱스를 기준으로 버튼 시간을 탐색한다.
for idx in range(3):
    button_time = abc_buttons[idx]
    # 남은 시간이 버튼 시간 이상인 조건 하에서 반복해서 차감하고, button_cnt 의 해당 인덱스를 1 올린다.
    while T >= button_time:
        T -= button_time
        button_cnt[idx] += 1

    # 반복문 종료 조건: 남은 시간이 0이면 종료 or 남은 값이 button_time 보다 작으면 button_cnt 에 -1 을 재할당
    if T == 0:
        print(*button_cnt)
        break
    elif T < 10:
        print(-1)
        break

