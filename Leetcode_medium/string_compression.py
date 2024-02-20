# String Compression (https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        
        cc = 0
        s = ""
        i = 0
        while i<len(chars):
            cc = 0
            char = chars[i]
            cc +=1

            for j in range(i+1, len(chars)):
                if chars[j]==char:
                    cc+=1
                else:
                    break

            s = s+char
            if cc>1:
                s = s+ str(cc)
            i = i+cc

        for i in range(0,len(chars)):
            if i < len(s):
                chars[i] = s[i]
            else:
                break

        return len(s)        
