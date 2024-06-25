from typing import List

def findArrayQuadruplet(arr: List[int], s: int) -> List[int]:
    n = len(arr)
    if n < 4:
        return []

    arr.sort()
    
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if current_sum == s:
                    return [arr[i], arr[j], arr[left], arr[right]]
                elif current_sum < s:
                    left += 1
                else:
                    right -= 1

    return []
