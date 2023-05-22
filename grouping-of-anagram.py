#https://leetcode.com/problems/group-anagrams/
def groupAnagrams(strs):
    temp ={}
    sort = ""
    for i in strs:
        sort = "".join(sorted(i))
        #
        if sort in temp:
            temp[sort].append(i)    
        else:
           temp[sort] = [i] 
    return list(temp.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))