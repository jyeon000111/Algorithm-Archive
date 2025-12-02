# 입력 : 각 줄에 N 입력 (0 <= N <= 12, N은 정수)

# 출력 : 칸토어 집합 모양 출력
# 1. '-' * (3 ** N) 문자열에서 시작한다.
# 2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다.
# 3. 남은 2개의 선도 3등분 하고, 가운데 문자열을 공백으로 바꾼다. (재귀!)
# 4. 모든 선의 길이가 1이 되면 멈춘다.

def cantor_set(num):
    '''숫자를 인자로 받아
    칸토어 집합 모양 문자열을 반환하는 함수입니다.
    '''
    if num == 0:
        return '-'
    mini_cantor = cantor_set(num - 1)
    return mini_cantor + ' ' * len(mini_cantor) + mini_cantor


while True:
    try:
        n = int(input())
        # n을 이용한 로직 작성
        print(cantor_set(n))

    except EOFError:
        # 더 이상 읽을 라인이 없으면(파일 끝이면) 에러가 발생하고,
        # 루프를 탈출함
        break



