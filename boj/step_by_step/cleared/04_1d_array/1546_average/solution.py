# 시험 본 과목 n개
n = int(input())

# 둘째 줄에 n개 과목의 점수가 주어진다. 이를 리스트에 담는다.
score_list = list(map(int, input().split()))

# 점수 중 최댓값을 m이라고 한다.
m = max(score_list)

# 모든 점수를 점수/m*100으로 고친 후, 새로운 평균을 출력한다.
# 수학적으로 새로운 평균은 현재 평균/m*100과 같다.
# (a/m*100 + b/m*100 + c/m*100) / 3 == (a + b + c) / m*100 / 3
print(sum(score_list) / (m*100) / n)