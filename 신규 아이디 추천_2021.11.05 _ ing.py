#!/usr/bin/env python
# coding: utf-8

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# In[6]:


a = 'abcde'
b = list(a)
c = ""
for i in b:
    c += i
    
print(c)
print([i for i in range(10)])
b.remove('a')
print(b)


# In[7]:


a = list("aaaaaabcd")
while True:
    if a[0] == "a":
        a.pop(0)
    else:
        break

print(a)


# In[69]:


a = "abcd"
a[0]


# In[ ]:





# In[8]:


a = "aaabcd123---___...????!!!!!"
for char in a:
    print(char)
a.replace("a","")


# In[71]:



new_id = ".....???..1........!!!....."

def solution(new_id):
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    special_char = ['-','_','.']
    for char in new_id:
        if not char.isalnum() and char not in special_char:
            new_id = new_id.replace(char,"")

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while True:
        if ".." not in new_id:
            break
        new_id = new_id.replace("..",".")
    print(new_id)
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id_list = list(new_id)
    
    while True:
        if new_id_list == []:
            break
        elif new_id_list[0] == ".":
            del new_id_list[0]
        elif new_id_list[-1] == ".":
            del new_id_list[-1]
        else:
            break

    new_id = ""
    for i in new_id_list:
        new_id += i

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == "":
        new_id = "a"

# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16:
        dish = new_id
        count = 0
        new_id = ""
        for i in dish:
            if count == 15:
                break
            count += 1
            new_id += i

#  만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    new_id_list = list(new_id)
    
    while True:
        if new_id_list == []:
            break
        elif new_id_list[-1] == ".":
            del new_id_list[-1]
        else:
            break

    new_id = ""
    for i in new_id_list:
        new_id += i

# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        new_id_list = list(new_id)
        last_char = new_id_list[-1]
        
        while not len(new_id_list) == 3:
            new_id_list.append(last_char)
    
    new_id = ""
    for i in new_id_list:
        new_id += i
    
    answer = new_id
    return answer

solution(new_id)


# In[20]:


def solution(new_id):
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id_list = list(new_id.lower())
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    all_numbers = [i for i in range(10)]
    all_char = ["-","_","."]
    for char in new_id_list:
        if not char in all_number.extend(all_char):
            new_id.remove(char)
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    for i in range(new_id.count('.')):
        if new_id[new_id.index('.') + 1] == '.':
            new_id.pop(new_id.index('.') + 1)
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#  만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    
    
    answer = ''
    return answer


# In[ ]:




