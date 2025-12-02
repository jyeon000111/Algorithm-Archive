# The "What" (최종 코드)

# Boolean 리스트를 활용한다. 
# 인덱스를 학생 번호로 사용할 것이므로, 0번 인덱스를 사용하지 않는 31칸짜리 리스트를 만든다.
student_checked_list = [False] * 31

# 28줄로 출석번호가 한줄씩 주어진다. 중복 없다.
for _ in range(28):
    num = int(input())
    # 제출한 학생 번호에 해당하는 인덱스의 값을 True로 바꾼다.
    student_checked_list[num] = True

# 1번부터 30번까지 탐색하면서 False인 인덱스를 출력한다.
for idx in range(1, 31):
    if not student_checked_list[idx]:
        print(idx)