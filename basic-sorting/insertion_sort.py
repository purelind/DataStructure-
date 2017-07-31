def insertionSort(alist):
    for i, item_i in enumerate(alist):  # 索引i 和　第i个元素
        print(alist)
        index = i
        while index > 0 and alist[index - 1] > item_i:  # 对已经排序的数组从后往前扫描比较
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i  # 找到已经排序的元素中小于或等于新元素的位置，

    return alist

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertionSort(unsorted_list))