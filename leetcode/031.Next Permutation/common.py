"""
Accepted
题目的意思是将列表组成一个数字，改变顺序找到下一个比原列表数字大的列表
从右到左（即从小到大）找第一个比它右边小的数（索引index）
然后在它右边找比它大的数里最小那个
交换这两个数的位置。然后将index右边的数倒序
题目要求void Do not return anything, modify nums in-place instead.
所以。。。
builtins.py里的list.reverse()居然不能对切片用。。
所以运用切片改变步长得到reverse
"""


def func(nums):
    length = len(nums)
    i = length - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:
        # my_reverse(nums, 0, length - 1)
        nums.reverse()
        return nums  # i等于0说明原nums是降序，所以直接倒序输出
    else:
        j = i
        i = i - 1
        while j < length and nums[j] > nums[i]:
            j += 1
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[length - 1:i:-1]
        # my_reverse(nums, i + 1, length - 1)
        # nums[i + 1:].reverse()
        return nums


# def my_reverse(nums, left, right):
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1


if __name__ == "__main__":
    nums = [3, 2, 1]
    print(func(nums))
