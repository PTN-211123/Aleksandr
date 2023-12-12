nums = [15, 3, 72, 34, 1, 7]
for i in range(len(nums)):
    if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        print(nums)
# for i in range(len(nums)):
#     print(i)
#     if nums[i] > nums[i + 1]:
#         nums[i] = nums[i +1]

# print(nums)