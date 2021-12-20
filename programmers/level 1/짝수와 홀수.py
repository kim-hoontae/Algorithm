# 내 풀이
def solution(num):
    if num % 2 == 1:
        return 'Odd'
    else:
        return 'Even'

# 그 외 다른분들의 풀이

def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]

def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"