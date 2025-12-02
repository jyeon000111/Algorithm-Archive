# 목표: 재귀 횟수 N에 따른 챗봇의 응답을 출력
N = int(input())
head = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'

line1 = '"재귀함수가 뭔가요?"'
line2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
line3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
line4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

tail1 = line1
tail2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
tail3 = '라고 답변하였지.'

underbar = '____'

def print_recursion(n, current=0):
    if current == 0:
        print(head)

    if n < current:  # 현재 값이 n을 넘어가면 종료
        return
    
    if n > current:
        print(underbar*current + line1)
        print(underbar*current + line2)
        print(underbar*current + line3)
        print(underbar*current + line4)

    if n == current:
        print(underbar*n + line1)
        print(underbar*n + tail2)
    
    print_recursion(n, current+1)

    print(underbar*current + tail3)
    

print_recursion(N)




