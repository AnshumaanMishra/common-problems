nums = [1,5,11,5, 6, 6]

target = sum(nums) // 2

possible = [-1 for _ in range(target + 1)]
possible[0] = 1

def sumPossible(index, target):
    if(target < 0):
        return False
    if(index == 0): 
        return target == 0
    if(possible[target] == 1):
        return True
    if(possible[target] == 0):
        return False
    possible[target] = sumPossible(index - 1, target - nums[index]) or sumPossible(index - 1, target)
    return possible[target]

print(sumPossible(len(nums) - 1, target))

