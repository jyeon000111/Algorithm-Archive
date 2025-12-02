# 보완할 점. 새로 공부한 것
- `print` 함수를 이렇게 f-string으로 쓰면 좀 더 깔끔해 보임.

```python
n = int(input())
for i in range(1, 10):
  # f-string을 사용한 출력
  print(f"{n} * {i} = {n*i}") 
```