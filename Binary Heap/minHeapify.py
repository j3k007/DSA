"""Time Complexity: O(Log(N))"""

def minHeapify(self, i):
    arr = self.arr
    lt = self.lChild(i)
    rt = self.rChild(i)
    smallest = i
    n = len(arr)
    if lt < n and arr[lt] < arr[smallest]:
        smallest = lt
    if rt < n and arr[rt] < arr[smallest]:
        smallest = rt
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        self.minHeapify(smallest)