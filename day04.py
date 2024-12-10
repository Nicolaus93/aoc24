
import re


def part_1(lines):
    ans = 0
    pattern1 = r'XMAS'
    pattern2 = r'SAMX'
    for line in lines:
        ans += len(re.findall(pattern1, line)) + len(re.findall(pattern2, line))

    # transpose
    transposed = list(map(''.join, zip(*lines)))
    for line in transposed:
        ans += len(re.findall(pattern1, line)) + len(re.findall(pattern2, line))

    reverse = [line[::-1] for line in lines]
    for mat in (lines, reverse):
        # upper diagonal
        for i in range(len(mat[0])):
            row = 0
            col = i
            diag = ''
            while row < len(mat) and col < len(mat[0]):
                diag = diag + mat[row][col]
                row += 1
                col += 1
            ans += len(re.findall(pattern1, diag)) + len(re.findall(pattern2, diag))

        # lower diagonal
        for i in range(1, len(mat)):
            row = i
            col = 0
            diag = ''
            while row < len(mat) and col < len(mat[0]):
                diag = diag + mat[row][col]
                row += 1
                col += 1
            ans += len(re.findall(pattern1, diag)) + len(re.findall(pattern2, diag))

    print("part1:", ans)


def part_2(lines):

    ans = 0
    n, m = len(lines), len(lines[0])
    matches = {"MAS", "SAM"}
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 'A':
                if 1 <= i <= n - 2 and 1 <= j <= m - 2:
                    diag1 = lines[i - 1][j - 1] + 'A' + lines[i + 1][j + 1]
                    diag2 = lines[i - 1][j + 1] + 'A' + lines[i + 1][j - 1]
                    if diag1 in matches and diag2 in matches:
                        ans += 1

    print("part2:", ans)


if __name__ == "__main__":
    with open("d4.txt", 'r') as f:
        ll = [line.strip() for line in f]

    part_1(ll)
    part_2(ll)
