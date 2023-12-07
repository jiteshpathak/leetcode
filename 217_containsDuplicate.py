class Solution(object):
    def containsDuplicate(self, nums):
        s1 = sorted(nums)
        for i in range(0,len(s1)-1):
            if s1[i]==s1[i+1]:
                return True
        return False
obj1=Solution()
result = obj1.containsDuplicate([1,2,3,1])
print(result)