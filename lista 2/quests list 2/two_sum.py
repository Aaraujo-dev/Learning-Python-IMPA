def two_sum(nums, target):
    for i in range(len(nums)):
        x = 0
        while x < len(nums):
            if target - nums[x] == nums[i]:
                return [x, i]
            x += 1


result = two_sum([1, 2, 3, 4, 5,13], 18)
print(result)     #printa os indices não os numeros em si