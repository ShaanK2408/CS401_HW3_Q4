"""
Group Members:
  - Victoria Rossi
  - Hristian Tountchev
  - Shaan Kohli
"""

import math

# TODO: implement this function
def min_length(n):
  """
  Args:
    n: an integer

  Returns:
    the fewest number of 1's in an expression involving only +,*,1,(, and ) which is equal to n, 
    or -1 if no such expression is possible.
  """

  # Anything smaller than 1 is impossible to get so we return -1
  if n < 1:
    return -1
  
  # Initialize array where dp[i] is the minimum number of 1's to obtain i
  dp = [float("inf")] * (n + 1)

  # Base case: 1 only needs a single 1
  dp[1] = 1

  # Fill array using + operator
  for i in range(2, n + 1):
    # Try all possible pairs (j, i -j) where j < i
    for j in range(1, int(math.sqrt(i)) + 1):
      dp[i] = min(dp[i], dp[j] + dp[i - j])

  # Fill array using * operator
  for i in range(2, n + 1):
    # Try all possible pairs (j, k) where j * k = i
    for j in range(1, int(math.sqrt(i) + 1)):
      if i % j == 0:
        k = i // j
        dp[i] = min(dp[i], dp[j] + dp[k])

  # Returns minimum number as long as the result has changed. Otherwise, return -1
  return dp[n] if dp[n] != float("inf") else -1

if __name__ == "__main__":
  # this should print out 5
  print(min_length(6))