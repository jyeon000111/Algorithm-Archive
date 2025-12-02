# 목표: 각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값을 출력
# -> 시간을 오름차순 정렬해서 누적합을 더하면 됨. (그리디 알고리즘)
N = int(input())  # 사람의 수 N

P_list = list(map(int, input().split()))
# 오름차순 정렬한다.
P_list = sorted(P_list)

total = 0  # 결과값을 0으로 초기화

# 각 인덱스의 값이 몇 번 더해질지 헤아린 후, 곱해준다.
# 0번 인덱스는 N번, 1번 인덱스는 (N-1)번, ... , (N-1)번 인덱스는 1번 더해짐.
# -> i번 인덱스는 (N-i)번 더해진다.
for i in range(N):
    total += P_list[i] * (N - i)

print(total)
