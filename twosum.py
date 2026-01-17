def twoosum(numbers, target):
    n=len(nums)
    for i in range (n):
        for j in range(i+1,n):
            if numbers[i]+numbers[j]==[targets]:
                return [i,j]
    return[]
nums[2,7,11,15]
targets=9
print(twoosum(nums,targets))