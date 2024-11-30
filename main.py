def longest_common_subsequence():
    # ToDo 
    def lcs(X, Y):
   
    m, n = len(X), len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
  
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Match found
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # No match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  
    lcs_string = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # Characters match
            lcs_string.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

   
    lcs_string.reverse()

    return dp[m][n], ''.join(lcs_string)


if __name__ == "__main__":
    string1 = input()
    string2 = input()
    length, subsequence = longest_common_subsequence(string1, string2)
    print(length)
  
