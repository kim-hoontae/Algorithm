# 내풀이
def solution(s):
    answer = ''.join(sorted(s, reverse=True))   
    return answer

# 실패한 2가지 풀이 (대문자 소문자를 신경쓰지않음)
def solution(s):
    answer = s[::-1]
    return answer

def solution(s):
    answer = ''.join(reversed(s))   
    return answer

# join을 처음 활용해봤는데 편리함을 깨닳았다.