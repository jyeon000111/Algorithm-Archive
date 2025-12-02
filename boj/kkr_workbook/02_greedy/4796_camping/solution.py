test_case = 0
while True:
    L, P, V = map(int, input().split())
    # 종료 조건: 0 0 0 입력이 들어오면 무한루프 종료!
    if (L, P, V) == (0, 0, 0):
        break
    test_case += 1
    # 목표 : 캠핑장을 최대 며칠동안 사용할 수 있는가?
    # L일 동안 캠핑장 사용 -> P-L일 동안 사용 불가 -> L일 동안 사용 -> ...
    # 전체 휴가 일수: V

    # 전체 휴가 일수를 P일 단위로 나눈다. (V가 P보다 클 때)
    # (나눈 몫 * L)일 동안 캠핑장 사용 가능.
    if V >= P:
        camping_days = (V // P) * L
        remain_holiday = V % P  # 잔여 휴가 일수는 나눈 나머지
    # 휴가 일수가 P보다 작으면, 잔여 휴가 일수에 V를 할당한다.
    else:
        remain_holiday = V
    # 잔여 휴가 일수가 L 보다 클 때는 L일 동안 추가 이용 가능
    # 작을 때는 잔여 휴가 일수만큼 추가 이용
    # -> 둘 중 더 작은 값만큼 추가 이용!
    camping_days += min(remain_holiday, L)

    print(f'Case {test_case}: {camping_days}')
