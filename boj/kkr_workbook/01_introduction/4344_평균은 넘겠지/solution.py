c = int(input())

for test_case in range(c):
    data = list(map(int, input().split()))
    N = data[0] # 학생의 수
    scores = data[1:] # N명의 점수 리스트
    # 평균을 구한다.
    avg_score = sum(scores) / N
    

    # 평균을 넘는 학생들의 수를 구한다.
    student_over_avg_cnt = 0
    for score in scores:
        if score > avg_score:
            student_over_avg_cnt += 1
    
    # 평균을 넘는 학생의 비율을 출력한다.
    print(f'{(student_over_avg_cnt / N * 100):.3f}%')