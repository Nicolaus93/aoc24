
def count_compositions(main_string: str, smaller_strings: set[str]) -> int:

    # dp[i] stores the number of ways to compose the prefix main_string[:i] using the smaller strings
    dp = [0] * (len(main_string) + 1)
    dp[0] = 1  # Base case: one way to compose an empty string

    # Iterate over all positions in main_string
    # For each position i, check all substrings main_string[j:i] (from index j to i) to see if they exist in the set
    # of smaller strings.
    for i in range(1, len(main_string) + 1):
        for j in range(i):
            substring = main_string[j:i]
            if substring in smaller_strings:
                dp[i] += dp[j]  # Add the count from dp[j]

    return dp[len(main_string)]


ll = open("d19.txt", 'r').read().splitlines()
ptt = {i for i in ll[0].split(", ")}
comps = ll[2:]
print(sum(1 for c in comps if count_compositions(c, ptt)))
print(sum(count_compositions(c, ptt) for c in comps))
