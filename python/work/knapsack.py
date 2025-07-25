from typing import List

def knapsack(profits: List[int], weights: List[int], capacity: int) -> int:
    ROWS = len(profits)+1
    COLS = capacity+1
    dp = [[0]*COLS for _ in range(ROWS)]
    for i in range(1, ROWS):
        for w in range(1, COLS):
            exclude = dp[i-1][w]
            if w-weights[i-1] >= 0:
                include = dp[i-1][w-weights[i-1]] + profits[i-1]
            else:
                include = 0
            dp[i][w] = max(exclude, include)
    return dp[ROWS-1][COLS-1]