"""
Accepted
题目里说的是空间复杂度应该为O(1)，即不能新建新的array，
所以将转换集合（去重复）之后的list放回nums的空间中。
所以直接return len(set(nums))是不行的，因为在调用set()方法的时候创建了隐藏的内存地址。
"""


def func(nums):
    nums[:] = list(set(nums))
    nums.sort()  # 加这个的原因是：虽然题目中要求返回的是去重后的列表长度，但是在检测中还对去重list是否有序进行了判断
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(func(nums))
