# isPalindrome 함수의 반환값, recursion 함수의 호출 횟수를 출력
temp_call_count = 0

def recursion(s, l, r):
    global temp_call_count
    temp_call_count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


T = int(input())
for testcase in range(T):
    temp_call_count = 0
    string = input()
    result_Palindrome = isPalindrome(string)
    print(result_Palindrome, temp_call_count)
