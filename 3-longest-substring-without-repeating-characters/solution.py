// 309 ms | 16.8 MB
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        visited={}
        left=right=0
        max_length=0
        for i in range(len(s)):
            if s[i] not in visited:
                visited[s[i]]=i
                right+=1
            else:
                left=max(left,visited[s[i]]+1)
                visited[s[i]]=i
                right+=1
            if(right-left>max_length):
                    max_length=right-left
        return max_length