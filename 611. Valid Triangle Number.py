nums = [2,2,3,4]
a = nums.sort() # make ascending order 
count = 0
n = len(nums)

for i in range(n - 1, 1, -1):
    left, right = 0, i - 1
    if nums[left] + nums[right] > nums[i]:
        count += right - left
        right -= 1
    else:
        left += 1
print(count)