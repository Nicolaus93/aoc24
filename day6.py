

def simulate(current_pos, grid):
    visited = {current_pos}
    vec = (-1, 0)
    for _ in range(len(grid) * len(grid[0])):
        ii = current_pos[0] + vec[0]
        jj = current_pos[1] + vec[1]
        if -1 >= ii or ii >= len(grid) or -1 >= jj or jj >= len(grid[0]):
            return len(visited)
        elif grid[ii][jj] == "#":
            vec = (vec[1], -vec[0])
        else:
            current_pos = (ii, jj)
            visited.add(current_pos)
    raise ValueError


def solve(lines):
    for i, line in enumerate(lines):
        for j, cc in enumerate(line):
            if cc == '^':
                current_pos = (i, j)
                break

    ans = simulate(current_pos, lines)
    print("part1:", ans)

    ans_2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                lines[i][j] = '#'
                try:
                    simulate(current_pos, lines)
                except ValueError:
                    ans_2 += 1
                lines[i][j] = '.'
    print("part2:", ans_2)


if __name__ == "__main__":
    with open("d6.txt", "r") as f:
        ll = []
        for line in f:
            ll.append([c for c in line.strip()])

    solve(ll)
