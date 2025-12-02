import sys
# --- 파일 입출력 설정 ---
# 입력 파일 경로
sys.stdin = open("input.txt", "r")
# --------------------

# 목표: 두 섬을 연결하는 가장 짧은 다리의 길이 구하기
# - 0은 바다, 1은 육지

# [ 아이디어 ]
# multi-source BFS 로 각 섬의 지점들에서 동시 출발
# 각기 다른 섬임을 숫자로 구분 (2부터 사용)
# - 좌상단부터 한칸씩 탐색
# - 상좌 인접한 칸이 1 아닌 숫자로 표시되어 있으면, 같은 숫자 기록

from pprint import pprint


def 

N = int(input())  # 지도의 크기

map_arr = [list(map(int, input().split())) for _ in range(N)]  


for y in range(N):
    for x in range(N):
        if map_arr[x][y] == 0:
            
        

