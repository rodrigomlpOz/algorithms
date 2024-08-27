def remove_first_name_duplicates(names):
    sorted_names = sorted(names, key=lambda x: x[0])
    ans = []
    for i in range(len(sorted_names)):
        if i == 0 or sorted_names[i-1][0] != sorted_names[i][0]:
            ans.append(names[i])
    return ans


names =[("Ian","Botham"),("David","Gower"),("Ian","Bell"),("Ian","Chappell")]
ans = remove_first_name_duplicates(names)
print(ans)
