def count_even(arr):
    count = 0
    for n in arr:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 4, 7, 8, 10]))
