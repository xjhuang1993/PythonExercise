"""
 Time Limit Exceeded
"""


def func(nums):
    length = len(nums)
    result = list()
    tmp_i = set()
    for i in range(length):
        if nums[i] in tmp_i:
            continue
        tmp_j = set()
        for j in range(i + 1, length):
            if nums[j] in tmp_j:
                continue
            for k in range(j + 1, length):
                if nums[i] + nums[j] + nums[k] == 0 and not is_same_list(result, [nums[i], nums[j], nums[k]]):
                    result.append([nums[i], nums[j], nums[k]])
            tmp_j.add(nums[j])
        tmp_i.add(nums[i])
    return result


def is_same_list(lists, l):
    for ls in lists:
        if sorted(ls) == sorted(l):
            return True
    return False


if __name__ == "__main__":
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    print(func(nums))
