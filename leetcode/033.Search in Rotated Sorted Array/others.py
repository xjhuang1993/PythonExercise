"""
Accepted
利用二分法
注意列表是螺旋升序的
"""


def func(nums, target):
    if not nums:
        return -1
    length = len(nums)
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # 说明mid左边升序不变，螺旋发生在右边
            if nums[left] <= target <= nums[mid]:  # target在mid左边，直接舍弃右边
                right = mid - 1
            else:  # 同上，舍弃左边
                left = mid + 1
        else:  # 螺旋发生在左边
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = right - 1
    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    print(func(nums, target))
