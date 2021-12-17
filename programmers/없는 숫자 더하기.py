# 내 풀이
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# 감명받음
def solution(numbers):
    return 45 - sum(numbers)