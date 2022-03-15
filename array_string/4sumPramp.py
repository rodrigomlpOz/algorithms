'''
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. 
Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
'''

def findArrayQuadruplet(arr, s):
    n = len(arr)

    # if there are fewer than 4 items in arr, by
    # definition no quadruplet exists whose sum is s
    if (n < 4):
        return []

    # sort arr in an ascending order
    arr.sort()

    for i in range(n-4):
        for j in range(i+1, n-3):
            # r stores the complementing sum
            r = s - (arr[i] + arr[j])

            # check for sum r in subarray arr[j+1…n-1]
            low, high = j + 1, n - 1

            while (low < high):
                if (arr[low] + arr[high] < r):
                    low+=1

                elif (arr[low] + arr[high] > r):
                    high-=1

                # quadruplet with given sum found
                else:
                    return [arr[i], arr[j], arr[low], arr[high]]

    return []


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(findArrayQuadruplet(arr, s))
