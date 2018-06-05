

def insert_sort(nums):
    """
    插入排序
    """
    for i in range(len(nums)):
        insert_num = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > insert_num:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = insert_num


def shell_sort(nums):
    """
    希尔排序
    """
    d = len(nums)
    while d != 0:
        d = d // 2
        for x in range(d):
            for i in range(x + d, len(nums), d):
                j = i - d
                insert_num = nums[i]
                while j >= 0 and nums[j] > insert_num:
                    nums[j + d] = nums[j]
                    j -= d
                nums[j + d] = insert_num


def select_sort(nums):
    """
    选择排序
    """
    length = len(nums)
    for i in range(length):
        key = nums[i]
        index = i
        for j in range(i + 1, length):
            if nums[j] < key:
                key = nums[j]
                index = j
        nums[index] = nums[i]
        nums[i] = key


def bubble_sort(nums):
    """
    冒泡排序
    """
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def quick_sort(nums, left, right):
    """
    快速排序
    """
    i, j = left, right
    if i >= j:
        return
    key = nums[i]
    while i < j:
        while i < j and nums[j] >= key:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= key:
            i += 1
        nums[j] = nums[i]
    nums[i] = key
    quick_sort(nums, left, i - 1)
    quick_sort(nums, j + 1, right)


if __name__ == "__main__":
    nums = [6, 5, 3, 1, 8, 7, 4, 2, 9]
    # insert_sort(nums)
    # shell_sort(nums)
    # select_sort(nums)
    # bubble_sort(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
