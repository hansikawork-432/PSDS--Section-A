'''from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return res


if __name__ == "__main__":
    sample_input = [-1, 0, 1, 2, -1, -4]
    print("Input:", sample_input)
    print("Output:", threeSum(sample_input))


from typing import List

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def get_fibonacci_sequence(count: int) -> List[int]:
    if count <= 0:
        return []
    
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print(f"First {n} Fibonacci numbers: {get_fibonacci_sequence(n)}")'''

from typing import List, Tuple

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str, moves: List[Tuple[str, str]]) -> None:
    if n == 1:
        moves.append((source, destination))
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
    moves.append((source, destination))
    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)


def solve_hanoi(n: int) -> List[Tuple[str, str]]:
    moves = []
    tower_of_hanoi(n, 'A', 'C', 'B', moves)
    return moves


if __name__ == "__main__":
    disks = 3
    all_moves = solve_hanoi(disks)
    
    print(f"Total moves required for {disks} disks: {len(all_moves)}")
    for step, (from_rod, to_rod) in enumerate(all_moves, start=1):
        print(f"Step {step}: Move disk from Rod {from_rod} to Rod {to_rod}")