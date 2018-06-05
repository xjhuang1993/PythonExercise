"""
Accepted
"""


def func(ss):
    tmp_dict = {}
    for s in ss:
        tmp_list = list(s)
        tmp_list.sort()  # 先排序保持唯一性
        tmp_tuple = tuple(tmp_list)  # 元组可哈希
        if tmp_tuple not in tmp_dict:
            tmp_dict[tmp_tuple] = [s]
        else:
            tmp_dict[tmp_tuple].append(s)
    return [val for val in tmp_dict.values()]


if __name__ == "__main__":
    ss = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(func(ss))

