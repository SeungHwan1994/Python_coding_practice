#!/usr/bin/env python
# coding: utf-8

# In[38]:


def solution(numbers, hand):
    answer = ''
    L_list = [1, 4, 7]
    R_list = [3, 6, 9]
    
    distance_0 = {2 : [2], 5 : [5], 8 : [8], 0 : [0]}
    distance_1 = {2 : [1,3,5], 5 : [4,6,2,8], 8 : [7,9,5,0], 0 : ['*','#',8] }
    distance_2 = {2 : [4,6,8], 5 : [1,3,7,9,0], 8 : [4,6,'*','#',2], 0 : [7,5,9] }
    distance_3 = {2 : [7,9,0], 5 : ['*','#'], 8 : [1,3], 0 : [2,4,6] }
    distance_4 = {2 : ['*','#'],5 : [], 8 : [], 0 : [1,3] }
    distance_list = [distance_0,distance_1,distance_2,distance_3,distance_4]
    
    L_hand = "*"
    R_hand = "#"
    
    for i in numbers:
        if i in L_list:
            answer += "L"
            L_hand = i
            
        elif i in R_list:
            answer += "R"
            R_hand = i
            
        else:
            dis = 0
            L_dis = 0
            for distance in distance_list:
                dis += 1
                L_dis = dis
                if L_hand in distance[i]:
                    break
            
            dis = 0
            R_dis = 0
            for distance in distance_list:
                dis += 1
                R_dis = dis
                if R_hand in distance[i]:
                    break
            
            if L_dis < R_dis:
                answer += "L"
                L_hand = i
                
            elif L_dis > R_dis:
                answer += "R"
                R_hand = i
                
            elif L_dis == R_dis:
                if hand == 'left':
                    L_hand = i
                    answer += "L"
                elif hand == 'right':
                    R_hand = i
                    answer += "R"
    return answer


# In[39]:


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')

#"LRLLLRLLRRL"

