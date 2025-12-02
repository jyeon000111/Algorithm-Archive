n = int(input())

def fibonacci(num):
    '''정수 num을 입력받아
    num번째 피보나치 수를 반환합니다.
    '''
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(n))