class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)

    def _sift_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest)


class PriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()

    def enqueue(self, val):
        self.min_heap.push(val)

    def dequeue(self):
        return self.min_heap.pop()


def heap_sort(arr):
    pq = PriorityQueue()
    for num in arr:
        pq.enqueue(num)
    sorted_arr = []
    for _ in range(len(arr)):
        sorted_arr.append(pq.dequeue())
    return sorted_arr


def maximize_adjacent_difference(arr):
    arr.sort()
    res = []
    left, right = 0, len(arr) - 1
    while left <= right:
        res.append(arr[left])
        left += 1
        if left <= right:
            res.append(arr[right])
            right -= 1
    
    total_diff = 0
    for i in range(len(res) - 1):
        total_diff += abs(res[i] - res[i+1])
        
    return res, total_diff


def smallest_subarray_greater_than_target(arr, target):
    min_len = float('inf')
    current_sum = 0
    left = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
            
    return min_len if min_len != float('inf') else -1


if __name__ == "__main__":
    print("=== Problem 1: Priority Queue & Heap Sort ===")
    pq = PriorityQueue()
    for item in [5, 3, 8, 1, 4]:
        pq.enqueue(item)
    print("Priority Queue Dequeue:", [pq.dequeue() for _ in range(5)])
    
    unsorted_arr = [12, 11, 13, 5, 6, 7]
    print("Heap Sort Output:", heap_sort(unsorted_arr))
    print()

    print("=== Problem 2: Maximize Adjacent Difference ===")
    p2_input = [4, 2, 7, 1]
    rearranged, sum_diff = maximize_adjacent_difference(p2_input)
    print("Rearranged Array:", rearranged)
    print("Total Sum of Differences:", sum_diff)
    print()

    print("=== Problem 3: Smallest Subarray Sum > Target ===")
    p3_arr = [2, 1, 5, 2, 3, 2]
    p3_target = 7
    print("Smallest Subarray Length:", smallest_subarray_greater_than_target(p3_arr, p3_target))