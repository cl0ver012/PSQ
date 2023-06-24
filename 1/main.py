# To solve this problem step by step, we'll use a dynamic programming approach. 
# We'll create a two-dimensional table dp, where dp[i][j] will represent the probability of having exactly j rainy days within the first i days. 
# The table will have dimensions (365+1) x (365+1), since we have 365 days and we want the probability of having at least n rainy days.

from typing import Sequence

def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:
    days = len(p)
    
    # Initialize the dp table
    dp = [[0.0 for _ in range(n+1)] for _ in range(days+1)]
    
    # Base case: There is a 100% chance of having 0 rainy days in the first 0 days
    dp[0][0] = 1.0
    
    # Fill the dp table
    for i in range(1, days+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j] * (1-p[i-1]) # Probability of not raining on day i
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * p[i-1] # Probability of raining on day i
    
    # Calculate the probability of having at least n rainy days
    result = 1 - sum(dp[days][:n])
    
    return result