
def removeDuplicattes(nums):
    newArray=[]
    for i in range(0,len(nums)):
        if nums[i] not in newArray:
            newArray.append(nums[i])
    return newArray
nums =[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicattes(nums ))
