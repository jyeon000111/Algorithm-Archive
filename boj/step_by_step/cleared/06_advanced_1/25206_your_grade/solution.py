# 목표 : 전공평점(major_gpa) 구하기
# 전공평점 = sum(학점 * 과목평점) / 학점의 총합

# 등급을 키, 과목평점을 밸류로 하는 딕셔너리를 생성한다.
grade_point_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
    }
# 학점*과목평점의 총합, 학점의 총합을 각각 0으로 초기화
total_grade_point = 0
total_credit = 0


# 20줄에 걸쳐 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
for _ in range(20):
    course_name, credit, grade = input().split()
    # credit 을 float 타입으로 변환해준다.
    credit = float(credit)
    
    # 중요한 조건: 등급이 P인 항목은 계산에서 제외한다.
    if grade == 'P':
        continue

    # 현재 과목의 과목평점을 구한다.
    grade_point = grade_point_dict[grade]
    # total_grade_point, total_credit 에 필요한 값을 더해준다.
    total_grade_point += credit * grade_point
    total_credit += credit
    

major_gpa = total_grade_point / total_credit
print(major_gpa)