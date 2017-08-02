class Merge:
    def mergeSort(self, alist):  # 参照算法四版P171(public class Merge)
        self.mergeSort_rec(alist, 0, len(alist)-1)

    def mergeSort_rec(self, alist, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo)//2
        self.mergeSort_rec(alist, lo, mid)  # 将左半边排序
        self.mergeSort_rec(alist, mid+1, hi)  # 将右半边排序
        self.mergeSortedArray(alist, lo, mid, hi)  # 归并结果

    def mergeSortedArray(self, alist, lo, mid, hi):
        """将alist[lo..mid] 和 alist[mid+1..hi]归并"""
        blist = alist.copy()  # 复制alist
        i = lo  # 左半边指针
        j = mid + 1  # 右半边指针
        for k in range(lo, hi+1):
            if i > mid:  # 左半边用尽（取右边的元素）
                alist[k] = blist[j]
                j += 1
            elif j > hi:  # 右半边用尽（取左边的元素）
                alist[k] = blist[i]
                i += 1
            elif blist[j] < blist[i]:  # 右半边当前元素小于左半边的当前元素（取右半边的元素）
                alist[k] = blist[j]
                j += 1
            else:  # 右半边当前元素大于或等于左半边当前元素（取左半边的元素）
                alist[k] = blist[i]
                i += 1

# 时间复杂度为 O(NlogN), 使用了等长的辅助数组，空间复杂度为 O(N)
unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort = Merge()
merge_sort.mergeSort(unsortedArray)
print(unsortedArray)
