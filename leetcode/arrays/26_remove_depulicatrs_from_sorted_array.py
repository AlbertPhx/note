#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


def removeDuplicattes(nums):
    l = 1
    for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l]=nums[r]
            l+=1
    print(nums)
    return l
nums =[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicattes(nums ))
