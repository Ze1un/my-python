def min_change(n,m,nums):
    if sum(nums) > m:
        return 0
    diff = m - sum(nums)
    changes = 0
    increments = sorted([9-num for num in nums],reverse = True) #可增加的数量，并反转
    for inc in increments:
        diff -= inc
        changes += 1
        if diff <= 0:
            return changes
    return changes
n,m = map(int,input().split())
nums = list(map(int,input().split()))
print(min_change(n,m,nums))
