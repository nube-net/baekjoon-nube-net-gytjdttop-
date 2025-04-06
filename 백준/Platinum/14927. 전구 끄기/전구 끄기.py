import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
min_flips = sys.maxsize
bit_table = [0] * n

for i in range(n):
    for j in range(n):
        if table[i][j]:
            bit_table[i] |= (1 << (n - j - 1))

for first_row_pattern in range(1 << n):
    current_table = bit_table[:]
    flip_count = 0
    
    # 1
    for col in range(n):
        if first_row_pattern & (1 << col):
            bit = n - col - 1
            current_table[0] ^= (1 << bit)
            if 1 < n:
                current_table[1] ^= (1 << bit)
            if bit > 0:
                current_table[0] ^= (1 << (bit - 1))
            if bit < n - 1:
                current_table[0] ^= (1 << (bit + 1))
            flip_count += 1
    # 2
    for row in range(1, n):
        for col in range(n):
            bit = n - col - 1
            if current_table[row - 1] & (1 << bit):
                current_table[row] ^= (1 << bit)
                if row + 1 < n:
                    current_table[row + 1] ^= (1 << bit)
                if bit > 0:
                    current_table[row] ^= (1 << (bit - 1))
                if bit < n - 1:
                    current_table[row] ^= (1 << (bit + 1))
                flip_count += 1

    if current_table[-1] == 0:
        min_flips = min(min_flips, flip_count)

print(min_flips if min_flips != sys.maxsize else -1)




