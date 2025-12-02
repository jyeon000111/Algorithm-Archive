import sys
from collections import deque
# 효율적인 수정을 위해 deque 자료구조 사용

T = int(sys.stdin.readline())
for _ in range(T):
    input_key = sys.stdin.readline().strip()
    # 목표: 입력 순서대로 키 문자열이 주어졌을 때, 비밀번호 출력
    # 백스페이스(-) : 바로 앞 글자 삭제
    # 화살표(<, >) : 커서 위치 1칸 이동
    dq1 = deque()  # 커서 앞
    dq2 = deque()  # 커서 뒤

    # 나머지 문자는 비밀번호의 일부
    for key in input_key:  # 입력 순서대로 키 꺼내기
        if key == '-':  # 백스페이스가 입력된 경우
            if dq1:  # 커서 앞에 값이 있으면
                dq1.pop()  # 제거
        elif key == '<':  # 왼쪽 화살표 입력된 경우
            if dq1:  # 커서 앞에 값이 있으면
                dq2.appendleft(dq1.pop())  # dq1 맨 뒤 값을 dq2 맨 앞으로 이동
        elif key == '>':  # 오른쪽 화살표 입력된 경우
            if dq2:  # 커서 뒤에 값이 있으면
                dq1.append(dq2.popleft())# dq2의 맨 앞 값을 dq1의 맨 뒤로 이동
        else:  # 나머지 문자는 dq1에 그대로 추가
            dq1.append(key)

    print(''.join(dq1 + dq2))