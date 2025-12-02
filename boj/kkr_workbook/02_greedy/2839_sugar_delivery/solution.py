N = int(input())  # 배달할 설탕의 양(kg)
# 목표: 5kg, 3kg 단위의 봉지에 나눠담을 때, 가장 적은 봉지 수 출력

cnt_pack = 0  # 사용한 봉지 수를 0으로 초기화

while True:  # 무한 반복
    # 종료 조건 1: N이 0일 때
    if N == 0:
        break
    # 종료 조건 2:  나누어 떨어지지 않으면 -1 할당하고 루프 종료
    elif N < 3:
        cnt_pack = -1
        break
    if N % 5 != 0:  # 5의 배수가 아니면,
        N -= 3  # 3 차감
        cnt_pack += 1  # 사용한 봉지 수 1 증가

    else:  # 5의 배수면, 전부 5kg에 담고, 루프 종료.
        cnt_pack += N / 5  # (N / 5)봉지 사용
        N = 0

print(int(cnt_pack))

