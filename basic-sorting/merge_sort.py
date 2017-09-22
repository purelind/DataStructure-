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
print("Merge by Up to Bottom: ", end='')
print(solve.merge_sort(unsortedArray))
"""
核心思想：将两个有序的数组归并成为一个更大的有序数组，先（递归的）将数组分成两半分别进行排序，然后归并结果
复杂度和稳定性：时间复杂度为 O(NlogN)；使用了等长的辅助数组，空间复杂度为 O(N)；稳定排序
"""


class MergeBU:
    def merge_sort(self, alist):  # 进行lgN次两两归并
        alength = len(alist)
        sz = 1  # sz子数组大小
        while sz < alength:
            lo = 0
            while lo < alength-sz:  # 子数组索引
                self.merge(alist, lo, lo+sz-1, min(lo+sz+sz-1, alength-1))
                lo += sz+sz
            sz += sz

        return alist

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

solveBU = MergeBU()
print('Merge by Bottom to Up: ', end='')
print(solveBU.merge_sort(unsortedArray))

"""
1.核心思想：先归并那些微型数组，然后再成对归并得到的子数组，直到我们将整个数组归并在一起。
2.注意：
　* 在每一轮归并中，最后一次归并的第二个子数组可能比第一个子数组要小，但这对于merge()方法不是问题。
　* 如果不是的话，所有归并中两个数组大小都应该一样，　而在下一轮中子数组的大小会翻倍。
3.当数组长度为２的幂时，自顶向下UB和自底向上BU的归并排序所用的比较次数和数组访问次数正好相同，只是顺序不同。
4.自底向上的归并排序比较适合用链表组织的数据。 
"""
