def get_max_papers(n,Ci):
    seen = set() #集合/哈希数组
    left = 0
    max_length = 0
    for right in range(n):
        while Ci[right] in seen:
            seen.remove(Ci[left])
            left += 1

        seen.add(Ci[right])
        max_length = max(max_length,right-left+1)
    return max_length
n = int(input())
Ci = list(map(int,input().split()))
print(get_max_papers(n,Ci))
"""
滑动窗口（Sliding Window）
滑动窗口是一种双指针技巧，通常用于处理连续子数组或子字符串问题，它可以在 O(N) 的时间复杂度内解决很多问题，比如：

最长无重复子串

最大/最小连续子数组

和满足某个条件的连续子数组

滑动窗口的基本思路
我们用 两个指针（left 和 right） 维护一个窗口，窗口内的数据始终满足题目的要求：

右指针 right 向右扩展窗口，增加新元素。

如果窗口不满足条件（例如出现重复元素），则移动 左指针 left，缩小窗口，直到窗口恢复合法状态。

更新答案（比如记录最大长度、最小长度等）。

继续移动 right，直到遍历完整个数组。
"""