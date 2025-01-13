# Nombre del problema: Counting Sort
# Rubén Colmenero Sánchez 
# 13/01/2025

def counting_sort(n, arr):
    min_val, max_val = min(arr), max(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr: count[num - min_val] += 1
    positions, sorted_arr = [], []
    for i, c in enumerate(count):
        sorted_arr.extend([i + min_val] * c)
        positions.extend([sum(count[:i])] * c)
    return sorted_arr, positions

n = int(input())
arr = list(map(int, input().split()))
sorted_arr, positions = counting_sort(n, arr)
print(" ".join(map(str, sorted_arr)))
print(" ".join(map(str, positions)))