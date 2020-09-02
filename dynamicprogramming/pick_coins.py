def maximum_revenue(coins):
    def compute_maximum_revenue_for_range(a, b):
        if a > b:
            # No coins left.
            return 0

        max_revenue_a = coins[a] + min(
            compute_maximum_revenue_for_range(a + 2, b),
            compute_maximum_revenue_for_range(a + 1, b - 1))
        max_revenue_b = coins[b] + min(
            compute_maximum_revenue_for_range(a + 1, b - 1),
            compute_maximum_revenue_for_range(a, b - 2))
        return max(max_revenue_a, max_revenue_b)

    return compute_maximum_revenue_for_range(0, len(coins) - 1)