class Solution(object):
    def chalkReplacer(self, chalk, k):
        i = 0
        k = k%sum(chalk)
        while(k >= chalk[i]):
            k = k-chalk[i]
            if(i == len(chalk)-1):
                i = 0
            else:
                i += 1
                
        if(chalk[i]>k):
            return i
        return

a = Solution()
b = [3,4,1,2]
result = a.chalkReplacer(b,25)
print(result)
