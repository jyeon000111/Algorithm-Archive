n = int(input())

def factorial(num):
    """정수를 입력받아
    팩토리얼 값을 반환하는 함수입니다.
    """
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(n))