def remove_first_name_duplicates(names):
    # Sort the names based on the first name
    sorted_names = sorted(names, key=lambda x: x[0])
    ans = []
    
    for i in range(len(sorted_names)):
        # Add the name to the result if it's the first occurrence of that first name
        if i == 0 or sorted_names[i-1][0] != sorted_names[i][0]:
            ans.append(sorted_names[i])
    
    return ans

names = [("Ian", "Botham"), ("David", "Gower"), ("Ian", "Bell"), ("Ian", "Chappell")]
ans = remove_first_name_duplicates(names)
print(ans)
