from functools import cache

@cache
def count_subs(main_string: str):
    if main_string == '': return 1
    return sum(count_subs(main_string[len(s):]) for s in patterns if main_string.startswith(s))

lines = open("d19.txt", 'r').read().splitlines()
patterns = {i for i in lines[0].split(", ")}
print(sum(count_subs(c) > 0 for c in lines[2:]))
print(sum(count_subs(c) for c in lines[2:]))