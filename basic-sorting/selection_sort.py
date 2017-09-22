def selection_sort(alist):
    for i in range(len(alist)):              # 不断的选择剩余元素中的最小值
        print(alist)
        min_index = i                        # 剩余元素中最小值的索引初始化指向　i
        for j in range(i+1, len(alist)):     # 遍历所有剩余元素
            if alist[j] < alist[min_index]:  # 如果扫描到比当前最小值还小的元素，改变min_index索引
                min_index = j                # 剩余元素中最小值的索引指向新的最小值
        alist[min_index], alist[i] = alist[i], alist[min_index]  # 每一次遍历（不是完整遍历）,排定一个'最小值'

    return alist

unsorted_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(selection_sort(unsorted_list))

"""
核心思想：从剩余元素中找出最小值放置在已经排序的元素数组末尾
复杂度和稳定性：平均情况与最坏情况均为 O(n^2)；空间复杂度：O(1)，因为使用了temp变量；非稳定排序
"""