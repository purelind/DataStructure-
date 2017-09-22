def shell_sort(alist):    # 将alist按升序排列
    alength = len(alist)
    h = 1
    while h < alength//3:  # h序列的初始值
        h = 3*h + 1
    while h >= 1:
        print(h)
        print(alist)
        for i in range(h, alength):  # 对每一列进行排序，排序之后子数组是部分有序的，一共存在（alength-h）个子数组需要排序
            j = i
            while j >= h and alist[j] < alist[j-h]:  # 将alist[i]插入到alist[i-h],alist[i-2h],alist[i-3h]...之中，子数组成为部分有序
                alist[j], alist[j-h] = alist[j-h], alist[j]  # 子数组中元素alist[i]交换到比它到的元素之前去
                j -= h
        h = h//3

    return alist

unsorted_list = [8, 5, 2, 6, 10, 3, 1, 4, 9, 7]
print(shell_sort(unsorted_list))

"""
1.核心思想：使数组中任意间隔为h的元素都是有序的，即h有序数组（h个互相独立的数组编织在一起组成的一个数组）
进行排序时，如果h很大，能够将元素移动到很远的地方去，
对于任意以１结尾的h序列，我们能够将数组排序
2.注意：对每一列进行排序之后，子数组是部分有序的，子数组部分有序的程度取决于递增序列的选择
3.复杂度和稳定性：平均情况O(nlogn~n^2)，最坏情况为 O(n^2)；空间复杂度：O(1)，因为使用了temp变量；非稳定排序
"""

