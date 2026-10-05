// 23 ms | 12.6 MB
class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        rows=[[] for _ in range(numRows)]
        row=0
        direction=1
        for i in range(len(s)):
            rows[row].append(s[i])
            if row==numRows-1:
                direction=-1
            elif row==0:
                direction=1
            row+=direction
        result=""
        for r in rows:
            result+="".join(r)
        return result
            