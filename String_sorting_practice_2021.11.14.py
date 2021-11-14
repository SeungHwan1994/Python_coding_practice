# 문자열의 n번째 문자열을 기준으로 정렬하여 출력하는 문제.
# strings = 여러개의 문자열을 담은 리스트
# n = 문자열의 n번째 문자가 문자열을 정렬한 기준이됨.
# 예를들면, strings = ['apple','grape','banana'] / n = 1 일경우 결과는 ['banana','apple','grape'] 가 된다.


def solution(strings, n):
    answer = []
    dict_string = {}
    for string in strings:
        dict_string[string[n] + string] = string

    new_dict = {}
    sorted_key_list = sorted(dict_string)

    for key in sorted_key_list:
        new_dict[key] = dict_string[key]

    for key, value in new_dict.items():
        answer.append(value)

    return answer
