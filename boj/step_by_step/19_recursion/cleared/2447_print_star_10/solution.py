N = int(input())
# 목표: N*N 2차원 배열에 재귀 패턴의 별을 출력
# - N = 3: 가운데 제외한 모든 칸에 별이 하나씩 있음
# - N > 3 (9, 27, 81, ...): 가운데 공백. 주변을 (N/3)*(N/3) 정사각형을 둘러싼 형태

# 1. 공백으로 가득 채워진 2차원 배열을 만들어둔다.
pattern = [[' '] * N for _ in range(N)]

def draw_pattern(N, row_idx, col_idx):
    '''정사각형의 크기 N와 그 구간에 패턴을 시작점 행, 열 인덱스를 인자로 받아
    주어진 재귀적 패턴이 되도록
    별을 찍는 함수입니다.
    '''
    # 0. 종료 조건:
    if N == 1:
        pattern[row_idx][col_idx] = '*'
        return
        
    # 1. 가운데는 공백으로 두기
    # 좌상단 모서리 기준점: (N/3, N/3)
    
    # 2. 주변 8개 정사각형 그리기
    # 좌상단 모서리 기준점 반복문으로 뽑아내기
    # (0, 0), (0, N/3), (0, N/3*2)
    # (N/3, 0), (N/3, N/3*2)
    # (N/3*2, 0) (N/3*2, N/3), (N/3*2, N/3*2)
    small_size = N//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: # 가운데 사각형 제외
                continue  
            # 각 모서리에 대해서, 재귀호출해서 패턴 그리기
            new_i = row_idx + i * small_size
            new_j = col_idx + j * small_size
            draw_pattern(small_size, new_i, new_j)
        

draw_pattern(N, 0, 0)
for row in pattern:
    print(''.join(row))





