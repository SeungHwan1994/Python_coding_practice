# 동일한 길이의 숫자로된 리스트 absolutes 와 불리언으로 구성된 리스트 signs 가 있을때,
# 불리언의 True 일경우 더하기 연산을 하고 False 일경우 빼기 연산을 하여 합계를 결과로 출력하라.
# 예를들면, absolutes = [1, 2, 3, 5] / sings = [True, True, False, False] 일경우, 결과는 -5 가 된다.

def solution(absolutes, signs):
    cnt = 0
    answer = 0

    for i in absolutes:
        if signs[cnt] == True:
            answer += i
        else:
            answer -= i
        cnt += 1


    return answer
