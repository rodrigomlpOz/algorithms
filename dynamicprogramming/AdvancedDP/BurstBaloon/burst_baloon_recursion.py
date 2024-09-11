def maxCoins(nums: list[int]) -> int:
    # Step 1: Add boundary balloons with value 1 on both sides
    nums = [1] + nums + [1]
    n = len(nums)

    # Recursive function to calculate the maximum coins from bursting balloons in the range (left, right)
    def burst(left, right):
        # Base case: no balloons to burst in this range
        if left + 1 == right:
            return 0
        
        max_coins = 0
        # Step 2: Try bursting each balloon in the range (left, right)
        for i in range(left + 1, right):
            # Burst balloon i last in this subarray, and calculate the coins obtained
            coins = nums[left] * nums[i] * nums[right]
            coins += burst(left, i) + burst(i, right)
            # Update the maximum coins we can collect
            max_coins = max(max_coins, coins)
        
        return max_coins
    
    # Step 3: Call the recursive function for the entire range (0, n-1)
    return burst(0, n - 1)

# Example usage
print(maxCoins([3, 1, 5, 8]))  # Output: 167
