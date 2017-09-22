class Quick:
    def quick_sort(self, alist):
        self.quick_sort_rec(alist, 0, len(alist)-1)

    def quick_sort_rec(self, alist, lo, hi):
        if hi <= lo:
            return
        j = self.partition(alist, lo, hi)
        self.quick_sort_rec(alist, lo, j-1)
        self.quick_sort_rec(alist, j+1, hi)

    @staticmethod
    def partition(alist, lo, hi):
        """将数组切分为alist[lo..i-1], alist[i], alist[i+1..hi] """
        i = lo          # 左扫描指针
        j = hi + 1      # 右扫描指针
        v = alist[lo]   # 切分元素
        while True:     # 扫描左右，检查扫描是否结束并交互元素
            while True:
                i += 1
                if alist[i] >= v:
                    break
                if i == hi:
                    break
            while True:
                j -= 1
                if v >= alist[j]:
                    break
                if j == lo:
                    break
            if i >= j:
                break
            alist[i], alist[j] = alist[j], alist[i]
        alist[lo], alist[j] = alist[j], alist[lo]   # 将 v = a[j] 放入正确的位置
        return j                                    # a[lo..j-1] <= a[j] <= a[j+1..hi] 达成

unsorted_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
quicksort = Quick()
quicksort.quick_sort(unsorted_list)
print(unsorted_list)

"""
1.核心思想：
 a.从数列中挑出一个元素作为基准数。
 b.分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
 c.再对左右区间递归执行第二步，直至各区间只有一个数。
2. 复杂度和稳定性：平均情况O(NlogN),最坏情况均为 O(N^2)；空间复杂度：O(logN~N)；非稳定排序
"""
