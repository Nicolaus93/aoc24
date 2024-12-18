from operator import floordiv
from utils import progressbar
from private_input import PROGRAM, REGISTER_A


def solve(program, registers):
    ans = ""
    combo_ops = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: lambda: registers['A'],
        5: lambda: registers['B'],
        6: lambda: registers['C'],
        7: lambda: registers[42],  # will raise an Error
    }
    combo = lambda y: combo_ops[y]() if callable(combo_ops[y]) else combo_ops[y]

    def adv(x):
        registers['A'] = floordiv(registers['A'], 2**combo(x))
        return 2

    def bxl(x):
        registers['B'] = registers['B'] ^ x
        return 2

    def bst(x):
        registers['B'] = combo(x) % 8
        return 2

    def jnz(x):
        nonlocal pointer
        if registers['A'] == 0: return 2
        pointer = program[pointer + 1]
        return 0

    def bxc(x):
        registers['B'] = registers['B'] ^ registers['C']
        return 2

    def out(x):
        nonlocal ans
        output = combo(x) % 8
        ans += f"{output},"
        return 2

    def bdv(x):
        registers['B'] = floordiv(registers['A'], 2 ** combo(x))
        return 2

    def cdv(x):
        registers['C'] = floordiv(registers['A'], 2 ** combo(x))
        return 2

    instructions = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }
    
    pointer = 0
    history = []
    for _ in range(10000):
        next_op = instructions[program[pointer]]
        history.append((registers.copy(), next_op.__name__, program[pointer + 1], combo(program[pointer + 1])))
        val = next_op(program[pointer + 1])
        pointer += val
        if pointer >= len(program):
            return ans[:-1], history

    raise ValueError(f"No solution found")


def debug_instructions(program):
    str_program = ",".join(str(i) for i in program)

    it = [i for i in range(0, 1500000)]

    # collect starting points that lead to similar final result (similar = contained in desired result)
    all_res = dict()
    for i in progressbar(it):
        register = dict(A=i, B=0, C=0)
        part_1_res, reg_history = solve(program, register)
        if part_1_res.endswith(str_program[-6:]):
            all_res.setdefault(part_1_res, []).append((i, reg_history))

    # check history for useful results
    for pos, k in enumerate(sorted(all_res.keys())):
        res_for_k = all_res[k]
        for a_start, history in res_for_k:
            print(a_start, str_program)
            for record in history:
                print(record)
        if pos > 100:
            break


def debug_fast(to_match):
    str_to_match = "".join(str(i) for i in to_match)
    it = [i for i in range(0, 1500000)]

    # collect starting points that lead to output ending like program to match
    all_res = []
    for i in progressbar(it):
        out = get_output(i)
        str_out = "".join(str(j) for j in out)
        if all(c1 == c2 for c1, c2 in zip(str_out[::-1], str_to_match[::-1])):
            all_res.append((i, out))

    for i in all_res:
        print(i)


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

    starts = [2284, 2499, 2500, 2539, 2540]
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


# print(solve(prg, reg)[0])
# print(debug(prg))
# debug_fast(prg)
print(get_output(REGISTER_A))
print(search(PROGRAM))
