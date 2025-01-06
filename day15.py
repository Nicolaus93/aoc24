
import pathlib

from utils import P2d, RIGHT, LEFT, UP, DOWN, print_grid


MOVES = {'v': DOWN, '^': UP, '>': RIGHT, '<': LEFT}


def move(pos, vec, grid):
    next_pos = grid.get(pos + vec)
    if next_pos == '#':
        can_move = False
    elif next_pos == '.':
        can_move = True
    else:
        _, can_move = move(pos + vec, vec, grid)

    if can_move:
        grid[pos + vec] = grid[pos]
        grid[pos] = '.'
        return pos + vec, True
    return pos, False


def move_robot(pos, vec, grid):
    if vec in (LEFT, RIGHT):
        return move(pos, vec, grid)[0]

    next_head = grid.get(pos + vec)
    all_moves = {pos}
    if '#' == next_head:
        can_move = False
    elif next_head == '.':
        can_move = True
    else:
        # [, ]
        if next_head == '[':
            can_move = move_boxes(pos + vec, vec, grid, all_moves)
        elif next_head == ']':
            can_move = move_boxes(pos + LEFT + vec, vec, grid, all_moves)
        else:
            raise ValueError(f"Invalid grid positions")

    if can_move:
        all_pos = sorted(all_moves, key=lambda p: p.x if vec == UP else -p.x)
        for pos in all_pos:
            grid[pos + vec] = grid[pos]
            grid[pos] = '.'
        return pos + vec
    return pos


def move_boxes(pos, vec, grid, all_moves):
    if vec in (LEFT, RIGHT):
        return move(pos, vec, grid)

    # vertical (up or down) move
    head_value = grid.get(pos)
    if head_value == '[':
        head = pos
        tail = pos + RIGHT
    elif head_value == ']':
        head = pos + LEFT
        tail = pos
    else:
        raise ValueError('Invalid move')

    next_head = grid.get(head + vec)
    next_tail = grid.get(tail + vec)
    if '#' in (next_head, next_tail):
        can_move = False
    elif next_head == next_tail == '.':
        can_move = True
    else:
        # [], ]., ][, .[
        if next_head == '[' and next_tail == ']':
            can_move = move_boxes(head + vec, vec, grid, all_moves)
        elif next_head == ']' and next_tail == '.':
            can_move = move_boxes(head + vec + LEFT, vec, grid, all_moves)
        elif next_head == ']' and next_tail == '[':
            can_move = move_boxes(head + vec + LEFT, vec, grid, all_moves) and move_boxes(tail + vec, vec, grid, all_moves)
        elif next_head == '.' and next_tail == '[':
            can_move = move_boxes(tail + vec, vec, grid, all_moves)
        else:
            raise ValueError(f"Invalid grid positions")

    if can_move:
        all_moves.add(head)
        all_moves.add(tail)
        return True
    return False


def solve(grid, moves, part_2=False):
    for rob_pos in grid:
        if grid[rob_pos ] == '@':
            break

    # move_fun = move_2 if part_2 else move
    for pos, m in enumerate(moves):
        if part_2:
            rob_pos = move_robot(rob_pos, MOVES[m], grid)
        else:
            rob_pos, _ = move(rob_pos, MOVES[m], grid)

    # print_grid(grid)
    ans = sum(100 * box_pos.x + box_pos.y for box_pos, value in grid.items() if value in 'O[')
    return ans


def read_input(lines):
    grid = dict()
    moves = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if len(lines[i]) != len(lines[0]):
                for m in lines[i].strip():
                    moves.append(m)
                break
            grid[P2d(i, j)] = lines[i][j]

    return grid, moves


def transform(lines):
    grid, moves = read_input(lines)
    new_grid = dict()
    for pos, value in grid.items():
        if value in ('#', '.'):
            new_grid[P2d(pos.x, 2 * pos.y)] = value
            new_grid[P2d(pos.x, 2 * pos.y + 1)] = value
        elif value == 'O':
            new_grid[P2d(pos.x, 2 * pos.y)] = '['
            new_grid[P2d(pos.x, 2 * pos.y + 1)] = ']'
        else:
            new_grid[P2d(pos.x, 2 * pos.y)] = '@'
            new_grid[P2d(pos.x, 2 * pos.y + 1)] = '.'
    return new_grid, moves


ll = pathlib.Path('d15.txt').read_text().splitlines()
print(solve(*read_input(ll)))
print(solve(*transform(ll), part_2=True))
