def insertion_sort(alist):
    for i, item_i in enumerate(alist):  # 索引i 和 第i个元素
        print(alist)
        index = i
        while index > 0 and alist[index - 1] > item_i:  # 对已经排序的数组从后往前扫描比较
            alist[index] = alist[index - 1]  # 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
            index -= 1

        alist[index] = item_i  # 找到已经排序的元素中小于或等于新元素的位置，将新元素插入到该位置

    return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertion_sort(unsorted_list))

"""
核心思想：对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
复杂度和稳定性：平均情况与最坏情况均为 O(n^2)，空间复杂度：未使用额外空间，稳定排序
"""
