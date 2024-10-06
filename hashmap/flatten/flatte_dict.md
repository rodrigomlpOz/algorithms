## Flatten a Nested Dictionary

### Problem Statement

You are given a dictionary that may contain nested dictionaries. Your task is to flatten this dictionary such that all the keys from the nested dictionaries are appended to the keys at the current level, separated by dots.

### Example

Input:
```python
nested_dict = {
    "a": {
        "b": {
            "c": 1,
            "d": 2
        },
    "e": 3
}
```

Output:
```python
flattened_dict = {
    "a.b.c": 1,
    "a.b.d": 2,
    "e": 3
}
```

### Explanation

The function should recursively traverse the nested dictionary, appending the keys from the nested dictionaries to the current level, separated by dots. The base case for the recursion is when a value is not a dictionary, at which point the key-value pair is added to the flattened dictionary.

### Solution

```python                                   
def flatten_dict(nested_dict, parent_key='', sep='.'):
    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
            
    return dict(items)
```

### Explanation

- **Base Case:** If the value is not a dictionary, the key-value pair is added to the `items` list.
- **Recursive Case:** If the value is a dictionary, the function calls itself recursively with the new key and the value.
- **Combining Results:** The results from the recursive calls are combined using `extend` to form the flattened dictionary.

### Example Usage

```python
nested_dict = {
    "a": {
        "b": {
            "c": 1,
            "d": 2
        },
        "e": 3
    }
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
```

### Time Complexity

The time complexity of this solution is O(N), where N is the total number of keys in the nested dictionary. This is because we need to traverse each key-value pair in the dictionary to flatten it.

### Space Complexity

The space complexity is also O(N) in the worst case, where the entire dictionary is flattened into a single-level dictionary. This is because we are creating a new dictionary to store the flattened result.

                                