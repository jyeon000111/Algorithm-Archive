def recur(total):
    global result
    # 기저조건1. target과 같으면 끝
    if total == target:
        result += 1
        return

    # 기저조건2. 이미 타겟을 넘어간 경우우
   if total > target:
        return

    # 각 경우의 수만큼 함수가 호출된다.
    recur(total + 1)  # 1을 더하는 경우
    recur(total + 2)  # 2를 더하는 경우
    recur(total + 3)  # 3을 더하는 경우