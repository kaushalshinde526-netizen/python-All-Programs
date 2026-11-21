def pair_sum(nums,target):
    seen={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in seen:
            return (complement,nums[i])
        seen[nums[i]]=i 
    return None
print(pair_sum([2,7,11,15],9))  # (4,5)