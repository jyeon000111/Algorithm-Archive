# 목표: 자연수 N의 가장 작은 생성자 구하기 (생성자 없는 경우 0 출력)

# 분해합: N과 N을 이루는 각 자리수의 합
# 245의 분해합 : 245 + 2 + 4 + 5 = 256
# 256의 생성자 : 245
# - 생성자가 없거나 여러 개일 수도 있다.

# [ 아이디어 ]
# - 생성자 < 분해합
# - 이분탐색? 안됨. 299의 분해합이 300의 분해합보다 크기 때문.
# - 모든 자릿수가 9라고 가정할 때, 생성자와 분해합의 차이가 가장 큼
# - 그럼 모든 자릿수를 9라고 가정하고 거기서부터 1씩 증가시켜가면서 분해합 계산!


N = int(input())

# 일단 자릿수를 구해야 한다.. 문자열의 길이 구하기
num_cnt = len(str(N))


# 최소 N - (9 * num_cnt) 부터 가능하다.
for num in range(N - (9 * num_cnt), N):
    if num < 1:
        continue
    # 각 자릿수의 합 구하기
    temp_arr = list(map(int, str(num)))
    split_sum = sum(temp_arr) + num

    if split_sum == N:
        print(num)
        break
else:
    print(0)