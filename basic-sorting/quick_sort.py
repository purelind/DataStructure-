class Quick:
    def quicksort(self, alist):
        self.quicksort_rec(alist, 0, len(alist)-1)

    def quicksort_rec(self, alist, lo, hi):
        if hi <= lo:
            return
        j = self.partition(alist, lo, hi)
        self.quicksort_rec(alist, lo, j-1)
        self.quicksort_rec(alist, j+1, hi)

    def partition(self, alist, lo, hi):
        """将数组切分为a[lo..i-1], a[i], a[i+1..hi] """
        i = lo  # 左扫描指针
        j = hi + 1  # 右扫描指针
        v = alist[lo]  # 切分元素
        while True:  # 扫描左右，检查扫描是否结束并交互元素
            while True:
                i += 1
                if alist[i] >= v:
                    break
                if i == hi:
                    break
            while True:
                j -= 1
                if v >=alist[j]:
                    break
                if j == lo:
                    break
            if i >= j:
                break
            alist[i], alist[j] = alist[j], alist[i]
        alist[lo], alist[j] = alist[j], alist[lo]  # 将 v = a[j] 放入正确的位置
        return j  # a[lo..j-1] <= a[j] <= a[j+1..hi] 达成

unsorted_list = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
quicksort=Quick()
quicksort.quicksort(unsorted_list)
print(unsorted_list)