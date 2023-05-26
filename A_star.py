import heapq


class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0  # Cost from initial state to current node
        self.h = 0  # Heuristic estimate of cost from current node to goal state
        self.f = 0  # Total estimated cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))


class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = []
        self.goal_node = None

    def solve(self):
        open_list = []
        closed_set = set()

        # Create the initial node
        initial_node = PuzzleNode(self.initial_state)
        initial_node.h = self._calculate_heuristic(initial_node.state)
        initial_node.f = initial_node.g + initial_node.h
        
        

        # Add the initial node to the open list
        heapq.heappush(open_list, initial_node)

        while open_list:
            # Get the node with the lowest f value
            current_node = heapq.heappop(open_list)

            # Check if the current node is the goal state
            if current_node.state == self.goal_state:
                self.goal_node = current_node
                break

            # Generate the child nodes
            child_nodes = self._generate_child_nodes(current_node)

            for child_node in child_nodes:
                if child_node in closed_set:
                    continue

                child_node.g = current_node.g + 1
                child_node.h = self._calculate_heuristic(child_node.state)
                child_node.f = child_node.g + child_node.h
                child_node.parent = current_node

                heapq.heappush(open_list, child_node)

            closed_set.add(current_node)

        if self.goal_node:
            # Build the moves list by backtracking from the goal node
            current = self.goal_node
            while current.parent:
                self.moves.append(current.move)
                current = current.parent
            self.moves.reverse()

        return self.moves

    def _calculate_heuristic(self, state):
        # Missing tiles heuristic
        h = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    h += 1
        return h

    def _generate_child_nodes(self, parent_node):
        child_nodes = []
        state = parent_node.state
        i, j = self._find_empty_space(state)

        # Move the empty space left if possible
        if j > 0:
            new_state = self._swap(state, i, j, i, j - 1)
            child_node = PuzzleNode(new_state, parent_node, "L")
            child_nodes.append(child_node)

        # Move the empty space right if possible
        if j < 2:
            new_state = self._swap(state, i, j, i, j + 1)
            child_node = PuzzleNode(new_state, parent_node, "R")
            child_nodes.append(child_node)

        # Move the empty space up if possible
        if i > 0:
            new_state = self._swap(state, i, j, i - 1, j)
            child_node = PuzzleNode(new_state, parent_node, "U")
            child_nodes.append(child_node)

        # Move the empty space down if possible
        if i < 2:
            new_state = self._swap(state, i, j, i + 1, j)
            child_node = PuzzleNode(new_state, parent_node, "D")
            child_nodes.append(child_node)

        return child_nodes

    @staticmethod
    def _find_empty_space(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    @staticmethod
    def _swap(state, i1, j1, i2, j2):
        new_state = [row[:] for row in state]
        new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
        return new_state


# Usage
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

puzzle = EightPuzzle(initial_state, goal_state)
moves = puzzle.solve()

if moves:
    print("Solution found in", len(moves), "moves:")
    for move in moves:
        print(move)
else:
    print("No solution found.")
