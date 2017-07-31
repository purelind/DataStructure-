def bubble_sort(alist):
    for i in range(len(alist)):  # 冒泡需要n（列表长度）次遍历（不是严格的遍历，每一次遍历排定一个数字，下一次遍历的数字少一个）
        print(alist)
        for j in range(1, len(alist)-i):  # 对于每一个i,排定一个数字
            if alist[j - 1] > alist[j]:   # 较大的数字后移，如同较大的泡泡上浮
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
    return alist

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(unsorted_list))

"""平均情况与最坏情况均为 O(n^2),空间复杂度：O(1)"""
