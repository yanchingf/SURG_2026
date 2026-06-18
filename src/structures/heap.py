
class Heap: # maxheap
    
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)
        self.sift_up(len(self.arr) - 1)

    def pop(self):
        if not self.arr:
            return None
        self.swap(0, len(self.arr) - 1)
        val = self.arr.pop()
        self.sift_down(0)
        return val

    def get_max(self):
        if self.arr:
            return self.arr[0]
        return None

    def sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.arr[i] > self.arr[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def sift_down(self, i):
        n = len(self.arr)
        while True:
            largest = i
            left, right = 2*i + 1, 2*i + 2
            if left < n and self.arr[left] > self.arr[largest]:
                largest = left
            if right < n and self.arr[right] > self.arr[largest]:
                largest = right
            if largest == i:
                break
            self._swap(i, largest)
            i = largest

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def __len__(self):
        return len(self.arr)