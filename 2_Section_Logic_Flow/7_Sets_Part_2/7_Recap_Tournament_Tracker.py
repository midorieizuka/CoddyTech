"""
In a competitive gaming tournament, players participate in different matches.
Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:

match1: Players who participated in Match 1
match2: Players who participated in Match 2
match3: Players who participated in Match 3

Your task is to:

Find players who participated in all three matches
Identify players who participated in exactly two matches
Determine players who participated in only one match
Count the total number of unique players in the tournament
Find players who participated in Match 1 but not in Match 2 or Match 3

Print the results in the following format:

Use sorted(list(set_name)) to display players in alphabetical order
Print the exact output format shown in the example

Example Input:
{"Alice", "Bob", "Charlie", "Diana"}
{"Charlie", "Diana", "Eve", "Frank"}
{"Alice", "Diana", "Frank", "George"}

Example Output:
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']
"""

# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
all_matches = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
one_two = match1 & match2
two_three = match2 & match3
one_three = match1 & match3
two_matches_total = one_two | two_three | one_three
two_matches = two_matches_total - all_matches

# 3. Find players who participated in only one match
only_one_match_total = match1 ^ match2 ^ match3
only_one_match = only_one_match_total - all_matches

# 4. Count total unique players
players = match1 | match2 | match3
unique_players = len(list(players)) #len conta a quantidade correta, não como a contagem de index

# 5. Find players in Match 1 only
match1_only = match1 - match2 - match3

# Print results in the specified format
print(f"Players in all matches: {sorted(list(all_matches))}")
print(f"Players in exactly two matches: {sorted(list(two_matches))}")
print(f"Players in only one match: {sorted(list(only_one_match))}")
print(f"Total unique players: {unique_players}")
print(f"Players in Match 1 only: {sorted(list(match1_only))}")
