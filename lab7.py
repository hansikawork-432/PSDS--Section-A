import sys
class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] >= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def extract_max(self):
        if not self.heap:
            return None
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
        return result

    def display(self):
        print(*self.heap)


def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)


heap_vals = list(
    map(
        int,
        input("Enter elements for Max Heap (space-separated): ").strip().split(
        ),
    )
)
pq = MaxHeap()
for val in heap_vals:
    pq.insert(val)

print("Max Heap / Priority Queue:", end=" ")
pq.display()
print("Highest Priority Element:", pq.extract_max())

sort_vals = list(
    map(
        int,
        input("Enter elements for Heap Sort (spaced): ")
        .strip()
        .split(),
    )
)
heap_sort(sort_vals)
print("Heap Sort:", *sort_vals)

a = list(
    map(
        int,
        input("Enter elements for Rearranging Array (spaced): ")
        .strip()
        .split(),
    )
)
a.sort()
n = len(a)
result = []
left = 0
right = n - 1

while left <= right:
    if left == right:
        result.append(a[left])
        break
    result.append(a[left])
    left += 1
    result.append(a[right])
    right -= 1

total_sum = 0
for i in range(1, n):
    total_sum += abs(result[i] - result[i - 1])

print("Rearranged Array:", *result)
print(f"Total Sum = {total_sum}")

arr = list(
    map(
        int,
        input("Enter array for Subarray search (space-separated): ")
        .strip()
        .split(),
    )
)
target = int(input("Enter target sum: "))
n_arr = len(arr)
left_window = 0
current_sum = 0
min_length = sys.maxsize

for right_window in range(n_arr):
    current_sum += arr[right_window]
    while current_sum > target:
        min_length = min(min_length, right_window - left_window + 1)
        current_sum -= arr[left_window]
        left_window += 1

if min_length == sys.maxsize:
    print(-1)
else:
    print(f"Smallest Subarray Length = {min_length}")