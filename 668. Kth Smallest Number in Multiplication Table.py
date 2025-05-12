class Solution:
  def findKthNumber(self, m: int, n: int, k: int) -> int:
    """
    Finds the k-th smallest number in an m x n multiplication table.
    The multiplication table has mat[i][j] = i * j (1-indexed).
    """

    # Helper function to count elements <= val_candidate in the multiplication table.
    # m_iter_limit is the number of rows to iterate through (effectively min(original_m, original_n)).
    # n_col_limit is the limit on columns for each row (effectively max(original_m, original_n)).
    def get_count_le_val(val_candidate: int, m_iter_limit: int, n_col_limit: int) -> int:
        count = 0
        for i in range(1, m_iter_limit + 1):
            # Number of elements in row 'i' that are <= val_candidate
            # Elements in conceptual row 'i' are i*1, i*2, ..., i*n_col_limit
            # We need i*j <= val_candidate  => j <= val_candidate / i
            # So, j can be 1, 2, ..., floor(val_candidate / i)
            # Also, j must be <= n_col_limit
            num_in_row = min(n_col_limit, val_candidate // i)
            
            # Optimization: if num_in_row is 0, it means val_candidate < i.
            # For any subsequent row i' > i, val_candidate will also be < i'.
            # So, val_candidate // i' will also be 0. We can stop early.
            if num_in_row == 0:
                break
            count += num_in_row
        return count

    # Ensure m_eff is the smaller dimension for loop optimization in get_count_le_val.
    # The actual table content is symmetric for (m,n) and (n,m).
    m_eff, n_eff = m, n
    if m > n:
        m_eff, n_eff = n, m # m_eff is min(original_m,n), n_eff is max(original_m,n)

    low = 1  # Smallest possible value in the table (1*1)
    high = m * n  # Largest possible value in the table (m*n)

    # Binary search for the smallest value 'ans_val' such that 
    # get_count_le_val(ans_val) >= k.
    # This 'ans_val' will be the k-th smallest number.
    ans = high # Initialize ans. It's guaranteed to be updated because
               # get_count_le_val(m*n) will be m*n, which is >= k (since k <= m*n).

    while low <= high:
        mid = low + (high - low) // 2
        # mid is always >= 1 because low starts at 1.
        
        # Count how many numbers in the table are less than or equal to 'mid'.
        # We use m_eff for the iteration limit to optimize.
        current_count = get_count_le_val(mid, m_eff, n_eff)
        
        if current_count >= k:
            # 'mid' is a potential answer. It might be THE k-th smallest,
            # or an even smaller number could also be the k-th smallest.
            # Store 'mid' as the current best answer and try to find smaller.
            ans = mid
            high = mid - 1 
        else: # current_count < k
            # 'mid' is too small. The k-th smallest must be larger.
            low = mid + 1
            
    return ans
