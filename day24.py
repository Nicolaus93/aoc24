
from operator import xor, or_, and_

OPS = {
    "XOR": xor,
    "OR": or_,
    "AND": and_
}

def read():
    lines = open("d24.txt", 'r').read().splitlines()
    graph = dict()
    operations = []
    for line in lines:
        if ":" in line:
            node, value = line.split(":")
            graph[node] = int(value)
        elif "->" in line:
            v1, op, v2, _, res = line.split(" ")
            operations.append((v1, op, v2, res))

    while operations:
        for i in range(len(operations)):
            v1, op, v2, node = operations[i]
            if v1 in graph and v2 in graph:
                graph[node] = OPS.get(op)(graph[v1], graph[v2])
                break
        operations.pop(i)

    MAX_Z = 46
    z = [graph[f'z{i}'] if i >= 10 else graph[f'z0{i}'] for i in range(MAX_Z)]
    res = sum(value * 2**pos for pos, value in enumerate(z))
    print(res)

    x = [graph[f'x{i}'] if i >= 10 else graph[f'x0{i}'] for i in range(MAX_Z - 1)]
    y = [graph[f'y{i}'] if i >= 10 else graph[f'y0{i}'] for i in range(MAX_Z - 1)]
    # print(''.join(str(i) for i in x[::-1]))
    # print(''.join(str(i) for i in y[::-1]))
    # print(''.join(str(i) for i in z[::-1]))
    # print()
    # print("01101100011011011111000000100111110111101011000")
    # print([i for i in range(11, 36)])
    print(x)
    print(y)
    print(z)
    # 11 -> 1, 1 instead of 0, 1
    # 15 -> 1, 1 instead of 1, 0

    # 31 -> 1, 1 instead of 1, 0
    # 38 -> 1, 0 instead of 1, 1
    return x, y, z


def sum_binary_numbers(x, y, z):
    result = []
    carry = 0

    z[12] = 0  # hfh, jdt
    z[18] = 0  # ddq, hhm
    z[32] = 0  # dtf, vjq
    z[38] = 0  # bvk, trm
    z[39] = 0  # vnt, dvq
    z[40] = 0  # dmf, nwb

    z[11] = 1  # dvh, hnn
    z[15] = 1  # dck, ctg
    z[16] = 1  # wmb, vsd
    z[17] = 1  # rmd, jws
    z[31] = 1  # x31, y31
    z[41] = 1  # twb, jgm

    # Perform bit-wise addition
    for i in range(len(x)):
        n1 = x[i]
        n2 = y[i]
        n3 = z[i]
        total = n1 + n2 + carry
        assert n3 == total % 2, f"at position {i}, {n1} + {n2} + {carry} = {n3}"
        result.append(total % 2)  # Append the sum bit (0 or 1)
        carry = total // 2       # Update carry (0 or 1)

    # If there's a carry left at the end, append it
    if carry:
        result.append(carry)

    return result


a, b, c = read()
sum_binary_numbers(a, b, c)
