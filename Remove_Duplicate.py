def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n in nums:
            if n not in seen:
                seen.add(n)
                result.append(n)
    return result
print(remove_duplicates([1, 2, 2, 3,1,4,4,8,7,5,6,8,9,]))
result = remove_duplicates([1, 2, 2, 3,1,4,4,8,7,5,6,8,9,])
result.sort()# result has been sorted in selection order 
print(result)
