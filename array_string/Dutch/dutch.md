### Dutch National Flag Problem

#### Problem Statement
Write a program that takes an array `A` and an index `index` into `A`, and rearranges the elements such that all elements less than `A[index]` appear first, followed by elements equal to `A[index]`, followed by elements greater than `A[index]`.

#### Examples
- Input: `A = [0, 1, 2, 0, 2, 1, 1]`, `index = 1`
  - Output: `[0, 0, 1, 1, 1, 2, 2]`
- Input: `A = [3, 3, 2, 1, 3, 2, 1]`, `index = 2`
  - Output: `[1, 1, 2, 3, 3, 3, 2]`

#### Function Signature
```python
def dutch(A: List[int], index: int) -> None:
   pass
```

#### High-Level Algorithm
1. **Initialization**:
   - Identify the pivot value `val` as `A[index]`.
   - Initialize three pointers: `less` to the beginning of the array, `equal` to the beginning of the array, and `more` to the end of the array.
2. **Partitioning**:
   - While `equal` is less than `more`:
     - If `A[equal]` is less than `val`, swap `A[less]` and `A[equal]`, then increment both `less` and `equal`.
     - If `A[equal]` is greater than `val`, decrement `more` and swap `A[equal]` and `A[more]`.
     - If `A[equal]` is equal to `val`, increment `equal`.
3. **Output**:
   - The array `A` is modified in place to reflect the partitioning.

#### Example Function Calls

```python
A1 = [0, 1, 2, 0, 2, 1, 1]
index1 = 1
print(dutch(A1, index1))  # Output: [0, 0, 1, 1, 1, 2, 2]

A2 = [3, 3, 2, 1, 3, 2, 1]
index2 = 2
print(dutch(A2, index2))  # Output: [1, 1, 2, 3, 3, 3, 2]

A3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
index3 = 6
print(dutch(A3, index3))  # Output: [1, 1, 2, 3, 3, 4, 5, 9, 5, 6, 5]
```

These example function calls will test the `dutch` function and verify that it correctly partitions the array based on the pivot value at the specified index.
