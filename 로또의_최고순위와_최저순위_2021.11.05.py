#!/usr/bin/env python
# coding: utf-8

# In[11]:


a = 1
b = [1, 3]
print(type(a))
b.islist()


# In[12]:


def solution(lottos, win_nums):
    
    if type(lottos) != list or type(win_nums) != list:
        return "배열이 아닙니다."
    
    elif len(lottos) != 6 or len(win_nums) != 6:
        return "길이가 6인 배열이 아닙니다."
    
    for win_nums_num in win_nums:
        if type(win_nums_num) != int:
            return "로또 번호가 숫자가 아닙니다"
        elif not 1 <= win_nums_num <= 45:
            return "로또 번호가 1 이상 45 이하인 정수가 아닙니다."
        elif win_nums.count(win_nums_num) >= 2:
            return "로또 배열안에 같은 숫자가 있습니다."
        
    for lottos_num in lottos:
        if type(lottos_num) != int:
            return "민우 로또 번호가 숫자가 아닙니다"
        elif not 0 <= lottos_num <= 45:
            return "민우 로또 번호가 0 이상 45 이하인 정수가 아닙니다."
        elif not lottos_num == 0 :
            if lottos.count(lottos_num) >= 2:
                return "0을 제외한 민우 로또 배열안에 같은 숫자가 있습니다."
    
    match_nums = 0
    unkown_nums = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            match_nums += 1

    min_win = match_nums
    max_win = match_nums + unkown_nums
    result_dict = { 6:1 , 5:2 , 4:3 , 3:4 , 2:5 , 1:6 , 0:6}
    
    answer = [ result_dict[max_win], result_dict[min_win] ]
    return answer

# 알 수 없는 숫자 = n
# 당첨된 숫자 개수 = m
# 당첨되지 않은 숫자 = 6 - m + n
# 최대 당첨숫자 = m + n
# 최저 당첨숫자 = m
# 당첨된 숫자 6 = 1등 / 5 = 2등 / 4 = 3등 / 3 = 4등 / 2 = 5등 / 1 or 0 = 6등


# In[13]:


print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
print(solution(23123, 23123))
print(solution([1,2], [1,3,4,]))
print(solution([1,2,3,4,5,6], [1,2,3,4,5,"a"]))
print(solution([1,2,3,4,5,6], [1,2,3,4,5,69]))
print(solution([0,0,3,4,5,6], [1,2,3,4,5,1]))
print(solution([0,0,3,'a',5,6], [1,2,3,4,5,6]))
print(solution([0,0,3,46,5,6], [1,2,3,4,5,6]))
print(solution([0,0,3,3,5,6], [1,2,3,4,5,6]))
print(solution([0,0,3,43,5,6], [1,2,3,4,5,6]))
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]


# In[12]:


a = [2, 1, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
for i in zip(a,b):
    print(i)
a.sort()
print(a)

print(not not True or (not True))

