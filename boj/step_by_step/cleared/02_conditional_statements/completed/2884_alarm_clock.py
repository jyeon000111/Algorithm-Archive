h, m = map(int, input().split())
# 시간 단위를 분 단위로 바꾸기
minutes = h * 60 + m
# 45분 빼주기 > minutes_new에 넣기
minutes_new = minutes - 45

# 예외 minutes_new가 음수일 때!
if minutes_new < 0:
    h_new = 23
    m_new = 60 + minutes_new
else:
    h_new = minutes_new // 60
    m_new = minutes_new % 60

print(h_new, m_new)