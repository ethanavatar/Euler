# https://projecteuler.net/problem=4

palindromes = []
for i in range(899):
    for j in range(899):
        if str((999-i) * (999-j)) == str((999-i) * (999-j))[::-1]:
            palindromes.append((999-i) * (999-j))
print(max(palindromes))