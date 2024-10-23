def flatten_dict(d, result=None, prv_keys=[]):
    # Initialize result dictionary if it's None
    if result is None:
        result = {}
    
    for k, v in d.items():
        # Check if the value is a dictionary, then recursively flatten
        if isinstance(v, dict):
            flatten_dict(v, result, prv_keys + [k])
        else:
            # Join keys with dots and add the flattened entry to the result
            result['.'.join(prv_keys + [k])] = v
    
    return result

# Example dictionary to flatten
nested_dict = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

# Flatten the dictionary
ans = flatten_dict(nested_dict)

# Final flattened dictionary output
# {'Key1': '1', 'Key2.a': '2', 'Key2.b': '3', 'Key2.c.d': '3', 'Key2.c.e.': '1'}

print(ans)
