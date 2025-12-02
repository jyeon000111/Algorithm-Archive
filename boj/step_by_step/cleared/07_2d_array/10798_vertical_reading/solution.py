# 5*15의 2차원 행렬을 빈문자열로 초기화한다.
blackboard_matrix = [[''] * 15 for _ in range(5)]

# 다섯줄의 글자를 입력받아, 각 행을 슬라이싱해 수정한다.
for row_idx in range(5):
    # 한 줄을 입력받아, 글자 하나하나를 요소로 하는 리스트를 만든다.
    new_chars_list = list(input())
    # 변경할 리스트의 길이만큼 슬라이싱하여, 재할당한다.
    blackboard_matrix[row_idx][:len(new_chars_list)] = new_chars_list

# 1행1열, 2행1열, 3행1열, ... 순으로 출력해야 한다.    
# 열 인덱스를 먼저 순회 -> 행 인덱스를 다음에 순회하며 한글자씩 공백없이 출력
for col_idx in range(15):
    for row_idx in range(5):
        print(blackboard_matrix[row_idx][col_idx], end='') 

