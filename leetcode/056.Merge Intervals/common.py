"""
Accepted
"""


class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


def func(intervals):
    intervals.sort(key=lambda x: x.start)  # 先按start排序
    result = []
    for interval in intervals:
        if not result or result[-1].end < interval.start:
            result.append(interval)
        else:
            result[-1].end = max(result[-1].end, interval.end)  # 这个-1很关键
    return result


if __name__ == "__main__":
    intervals = []
    i = Interval(1, 3)
    intervals.append(i)
    i = Interval(2, 6)
    intervals.append(i)
    i = Interval(8, 10)
    intervals.append(i)
    i = Interval(15, 18)
    intervals.append(i)
    for i in func(intervals):
        print(i.start, i.end)
