def edit_text(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, m + 1):
        dp[0][i] = i
    for i in range(1, n + 1):
        dp[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[n][m]


word_a = input()
word_b = input()
print(edit_text(word_a, word_b))


# def edit_text(wordA, wordB):
#     n = len(wordA)
#     m = len(wordB)

#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     for i in range(1, m + 1):
#         dp[0][i] = i
#     for i in range(1, n + 1):
#         dp[i][0] = i

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if wordA[i - 1] == wordB[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

#     return dp[n][m]


# word_a = input()
# word_b = input()
# print(edit_text(word_a, word_b))

# def edit_dist(str1, str2):
#     n = len(str1)
#     m = len(str2)

#     dp = [[0] * (m + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         dp[i][0] = i

#     for j in range(1, m + 1):
#         dp[0][j] = j

#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

#     return dp[n][m]

# str1 = input()
# str2 = input()

# print(edit_dist(str1, str2))
