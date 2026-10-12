
T = int(input("enter test cases: "))

for i in range(T):
    S = input("enter string: ")
    freq = {}

    for ch in S:
        freq[ch] = freq.get(ch, 0) + 1

    ans = sum(v // 2 for v in freq.values())
    print(ans)