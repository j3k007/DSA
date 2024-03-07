"""Time Complexity: O(Log(n))"""

def insert(self, x):
    arr = self.arr
    arr.append(x)
    i = len(arr) - 1
    while i > 0 and arr[self.parent(i)] > arr[i]:
        p = self.parent(i)
        arr[i], arr[p] = arr[p], arr[i]
        i = p