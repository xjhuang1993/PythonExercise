"""
Accepted
这道题我灭看懂题目。。。
"""


def func(s, words):
    if not s or words == []:
        return []
    len_s = len(s)
    len_word = len(words[0])
    len_sub_str = len(words) * len_word
    times = {}
    for word in words:
        if word in times:
            times[word] += 1
        else:
            times[word] = 1
    result = []
    for i in range(min(len_word, len_s - len_sub_str + 1)):
        find_answer(i, len_s, len_word, len_sub_str, s, times, result)
    return result


def find_answer(s_start, len_s, len_word, len_sub_str, s, times, ans):
    word_start = s_start
    curr = {}
    while s_start + len_sub_str <= len_s:
        word = s[word_start:word_start + len_word]
        word_start += len_word
        if word not in times:
            s_start = word_start
            curr.clear()
        else:
            if word in curr:
                curr[word] += 1
            else:
                curr[word] = 1
            while curr[word] > times[word]:
                curr[s[s_start:s_start + len_word]] -= 1
                s_start += len_word
            if word_start - s_start == len_sub_str:
                ans.append(s_start)


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(func(s, words))
