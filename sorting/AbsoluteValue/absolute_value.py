def absolute_valute(arr):
    return sorted(arr, key=lambda x: (abs(x), x) )



arr = [2, -7, -2, -2, 0]
ans = absolute_valute(arr)
print(ans)