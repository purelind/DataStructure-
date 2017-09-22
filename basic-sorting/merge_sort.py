class Merge:
    def merge_sort(self, alist):  # 参照算法四版P171(public class Merge)
        self.sort_list(alist, 0, len(alist)-1)
        return alist

    def sort_list(self, alist, lo, hi):
        """将数组alist[lo..hi]排序"""
        if hi <= lo:
            return
        mid = lo + (hi - lo)//2
        self.sort_list(alist, lo, mid)  # 将左半边排序
        self.sort_list(alist, mid+1, hi)  # 将右半边排序
        self.merge(alist, lo, mid, hi)  # 归并结果，将alist[lo..mid] 和 alist[mid+1..hi]归并

    @staticmethod
    def merge(alist, lo, mid, hi):
        """
        将alist[lo..mid] 和 alist[mid+1..hi]归并
        """
        from copy import deepcopy
        blist = deepcopy(alist)  # 复制alist，这里使用alist.copy()进行浅拷贝也没事，因为alist不存在二级数组
        i = lo       # 左半边指针
        j = mid + 1  # 右半边指针
        for k in range(lo, hi+1):   # 归并回到alist[lo..hi]
            if i > mid:             # 左半边用尽（取右边的元素）
                alist[k] = blist[j]
                j += 1
            elif j > hi:            # 右半边用尽（取左边的元素）
                alist[k] = blist[i]
                i += 1
            elif blist[j] < blist[i]:  # 右半边当前元素小于左半边的当前元素（取右半边的元素）
                alist[k] = blist[j]
                j += 1
            else:                      # 右半边当前元素大于或等于左半边当前元素（取左半边的元素）
                alist[k] = blist[i]
                i += 1


unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
solve = Merge()
print(solve.merge_sort(unsortedArray))
"""
核心思想：将两个有序的数组归并成为一个更大的有序数组，先（递归的）将数组分成两半分别进行排序，然后归并结果
复杂度和稳定性：时间复杂度为 O(NlogN)；使用了等长的辅助数组，空间复杂度为 O(N)；稳定排序
"""