# 새로 배운 것
1. sum() 함수
```python
n = int(input())
sum(range(1, n + 1))
```

2. 수학 공식 이용 (등차수열 합 공식)
  - 1부터 n까지의 합 : n * (n + 1) / 2
```python
n = int(input())
print(n * (n  + 1) // 2)
# //은 나눗셈 결과의 정수 부분만 가져오는 연산자