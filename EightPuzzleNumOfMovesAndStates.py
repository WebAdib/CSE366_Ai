import heapq

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the initial state
initial_state = [[1, 7, 5], [3, 6, 2], [8, 0, 4]]

# Define the dimensions of the puzzle
n = 3  # 3x3 puzzle

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def manhattan_distance(state):
    distance = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, n)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

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
    open_list = [(manhattan_distance(initial_state), 0, initial_state, [])]  # Added a move count and a path list
    closed_set = set()

    while open_list:
        _, moves_count, current_state, path = heapq.heappop(open_list)
        if current_state == goal_state:
            return moves_count, path  # Return both the move count and the path

        if tuple(map(tuple, current_state)) in closed_set:
            continue

        closed_set.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in closed_set:
                f = manhattan_distance(neighbor) + moves_count + 1  # Update the total cost
                new_path = path + [current_state]  # Add the current state to the path
                heapq.heappush(open_list, (f, moves_count + 1, neighbor, new_path))

    return None

result = solve_puzzle(initial_state, goal_state)

if result:
    moves_count, path = result
    print("Solution (Using Manhattan Distance) found in {} moves:".format(moves_count))
    print("\nInitial State :")
    for i, state in enumerate(path):
        for row in state:
            print(row)
        print(f"\nMove {i + 1}:")
    for row in goal_state:
        print(row)
else:
    print("No solution found.")

