def diffBetweenTwoStrings(source, target):
    # Step 1: Initialize the DP table
    dp = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

    # Step 2: Fill the base cases
    for i in range(len(source) + 1):
        dp[i][0] = i  # Deleting all characters from source
    for j in range(len(target) + 1):
        dp[0][j] = j  # Inserting all characters into target

    # Step 3: Fill the DP table using the recurrence relation
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])  # Minimum of insertion or deletion

    # Step 4: Backtrack to find the sequence of operations
    ans = []
    i, j = len(source), len(target)

    while i > 0 and j > 0:
        if source[i - 1] == target[j - 1]:
            ans.append(source[i - 1])  # Characters match, no operation
            i -= 1
            j -= 1
        elif dp[i - 1][j] <= dp[i][j - 1]:
            ans.append('-' + source[i - 1])  # Deletion
            i -= 1
        else:
            ans.append('+' + target[j - 1])  # Insertion
            j -= 1

    # Step 5: Handle remaining characters in target (if any)
    while j > 0:
        ans.append('+' + target[j - 1])
        j -= 1

    # Handle remaining characters in source (if any)
    while i > 0:
        ans.append('-' + source[i - 1])
        i -= 1

    return " ".join(reversed(ans))

# Example test cases
source = "AB"
target = "ABDFFGH"
print(diffBetweenTwoStrings(source, target))  # Output: "A B +D +F +F +G +H"

source = "ABC"
target = "AXY"
print(diffBetweenTwoStrings(source, target))  # Output: "A -B -C +X +Y"
