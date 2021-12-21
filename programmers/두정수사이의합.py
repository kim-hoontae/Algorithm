# 내 풀이
def solution(a, b):
    if a == b:
        return a 
    if a > b:
        a,b = b,a
    answer = sum(range(a,b+1))
    return answer

# 다른 풀이
def solution(a,b):
    return sum(range(min(a,b),max(a,b)+1))