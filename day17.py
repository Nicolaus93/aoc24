from private_input import PROGRAM, REGISTER_A


def get_output(start: int):
    r = [start, 0, 0]
    ans = []
    while r[0] != 0:
        r[1] = r[0] % 8
        r[1] = r[1] ^ 4
        r[2] = r[0] // 2**r[1]
        r[1] = r[1] ^ r[2]
        r[1] = r[1] ^ 4
        ans.append(r[1] % 8)
        r[0] = r[0] // 8
    return ans


def search(prog):
    starts = [2284]
    while starts:
        s = starts.pop(0)
        for i in range(8):
            n = s * 8 + i
            out = get_output(n)
            if len(out) == len(prog) and all(c1 == c2 for c1, c2 in zip(out, prog)):
                    return n
            if all(c1 == c2 for c1, c2 in zip(out[::-1], prog[::-1])):
                # partial solution
                if n not in starts:
                    starts.append(n)
    raise ValueError(f"No solution found")


print(get_output(REGISTER_A))
print(search(PROGRAM))
