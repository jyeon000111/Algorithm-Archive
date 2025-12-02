n = int(input())

# n을 이진수로 바꿔서 출력한다.
def get_binary(num):
    '''십진수 자연수 값을 인자로 받아서
    이진수로 바꿔서 반환하는 함수입니다.
    '''
    if num < 2:
        return str(num)
    return get_binary(num//2) + str(num % 2)

print(get_binary(n))