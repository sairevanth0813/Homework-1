def edit_distance(s, t, sub_cost=1, ins_cost=1, del_cost=1):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = i * del_cost
    for j in range(n+1):
        dp[0][j] = j * ins_cost
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1] + sub_cost, # substitution
                    dp[i][j-1] + ins_cost,   # insertion
                    dp[i-1][j] + del_cost    # deletion
                )
    return dp[m][n]

s1, s2 = "Sunday", "Saturday"

print("Model A (Sub=1, Ins=1, Del=1):", edit_distance(s1, s2, 1, 1, 1))
print("Model B (Sub=2, Ins=1, Del=1):", edit_distance(s1, s2, 2, 1, 1))

reflection = """
Model A distance = 3, Model B distance = 4.
Model A uses substitutions effectively, while Model B prefers insertions/deletions.
For spell checking, substitutions are natural (typo correction).
For DNA alignment, insertions/deletions are more realistic.
"""
print("\nReflection:", reflection)