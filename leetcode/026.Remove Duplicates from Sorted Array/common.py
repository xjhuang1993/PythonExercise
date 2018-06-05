"""
Accepted
遍历列表元素，判断前后两个是否相等，如相等则将前一个从列表中移除，
如果不相等则将索引后移，进行下一轮比较
因为输入的nums就是有序的，所以不用考虑很后面的元素与很前面的元素相等，且处理后的也是有序的
"""


def func(nums):
    index = 0
    for num in nums[1:]:
        if num == nums[index]:
            nums.remove(num)
        else:
            index += 1
    return nums


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(func(nums))
