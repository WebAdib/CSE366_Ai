import heapq

# Define the goal state
goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

# Define the initial state
initial_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 14, 15], [11, 12, 13, 0]]

# Define the dimensions of the puzzle
n = 4  # 3x3 puzzle

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def AbsGoalMinIni(state):
    count = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != goal_state[i][j]:
                count = abs(goal_state[i][j] - state[i][j])
    return count

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def get_neighbors(state):
    x, y = None, None
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                x, y = i, j
                break

    neighbors = []
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            new_state = [row[:] for row in state]  # Copy the state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def solve_puzzle(initial_state, goal_state):
    open_list = [(AbsGoalMinIni(initial_state), 0, initial_state)]  # Added a move count
    closed_set = set()

    while open_list:
        _, moves_count, current_state = heapq.heappop(open_list)
        if current_state == goal_state:
            return moves_count, current_state

        if tuple(map(tuple, current_state)) in closed_set:
            continue

        closed_set.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in closed_set:
                h = AbsGoalMinIni(neighbor)  # Misplaced tiles heuristic
                f = h + moves_count + 1  # Update the total cost
                heapq.heappush(open_list, (f, moves_count + 1, neighbor))

    return None

result = solve_puzzle(initial_state, goal_state)

if result:
    moves_count, solution = result
    print("Solution (Using Misplaced Tiles) found in {} moves:".format(moves_count))
    for row in solution:
        print(row)
else:
    print("No solution found.")
