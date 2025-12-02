n = int(input())
def factorial(num):
    '''정수 num을 인자로 받아
    팩토리얼 값을 반환하는 함수입니다.
    '''
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(n))