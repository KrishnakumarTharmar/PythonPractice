# Input Format

# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Output Format

# Output the total number of distinct country stamps on a single line.

# Sample Input

# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 
# Sample Output

# 5
# Explanation

# UK and France repeat twice. Hence, the total number of distinct country stamps is  5(five).

n = int(input())
contries = set()

for i in range(n):
    contries.add(input())

print(len(contries))