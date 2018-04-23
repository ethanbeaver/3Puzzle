def calculate_complex_heuristic(board):
    total = 0
    for i in range(0, 4):
        total = total + 2 if i + int(board[i] or 0) == 3 else 1
    return total

def calculate_simple_heuristic(board):
    return int(board[0] != 1) + int(board[1] != 2) + int(board[2] != 3) + int(board[3] is not None)


class ThreePuzzle_Node:
    def __init__(self, board=[3, 1, 2, None], depth=0, heuristic=0):
        self.board = board
        self.children = []
        self.depth = depth
        self.heuristic = heuristic

    def __str__(self):
        return str(self.board)

    def generate_children(self, parent_map, complex_heuristic=False):
        blank_location = self.board.index(None)
        for i in range(0, 4):
            if i != 3 - blank_location and i != blank_location:
                new_board = self.board[:]
                new_board[blank_location], new_board[i] = new_board[i], new_board[blank_location]
                child = ThreePuzzle_Node(new_board, self.depth+1)
                if complex_heuristic:
                    child.heuristic = self.depth + calculate_complex_heuristic(child.board)
                else:
                    child.heuristic = self.depth + calculate_simple_heuristic(child.board)
                if not ThreePuzzle_Node.state_in_previous(parent_map, child):
                    self.children.append(child)
                    parent_map[child] = self


    @staticmethod
    def state_in_previous(parent_map, node):
        return any(
            node.board == existing.board
            for existing in parent_map
        )


def BFS_Solution(root_node):
    to_visit = [root_node]
    parent_map = {root_node: None}
    while to_visit:
        node = to_visit.pop()
        node.generate_children(parent_map)
        to_visit = node.children + to_visit
        if node.board == [1,2,3,None]:
            solution = []
            while node is not None:
                solution = [node] + solution
                node = parent_map[node]
            return solution
    return None

def Branch_Bound_Solution(root_node):
    to_visit = [root_node]
    parent_map = {root_node: None}
    while(to_visit):
        node = to_visit.pop()
        if node.board == [1,2,3,None]:
            solution = []
            while node is not None:
                solution = [node] + solution
                try:
                    node = parent_map[node]
                except:
                    for x in parent_map:
                        if parent_map[x] is not None and node.board == x.board:
                            node = parent_map[x]
            return solution
        node.generate_children(parent_map)
        to_visit = node.children + to_visit
        to_visit.sort(key=lambda x: x.depth, reverse=True)
    return None

def Branch_Bound_Simple_Heuristic_Solution(root_node):
    to_visit = [root_node]
    parent_map = {root_node: None}
    while(to_visit):
        node = to_visit.pop()
        if node.board == [1,2,3,None]:
            solution = []
            while node is not None:
                solution = [node] + solution
                try:
                    node = parent_map[node]
                except:
                    for x in parent_map:
                        if parent_map[x] is not None and node.board == x.board:
                            node = parent_map[x]
            return solution
        node.generate_children(parent_map)
        to_visit = node.children + to_visit
        to_visit.sort(key=lambda x: x.heuristic, reverse=True)
    return None

def Branch_Bound_Complex_Heuristic_Solution(root_node):
    to_visit = [root_node]
    parent_map = {root_node: None}
    while(to_visit):
        node = to_visit.pop()
        if node.board == [1,2,3,None]:
            solution = []
            while node is not None:
                solution = [node] + solution
                try:
                    node = parent_map[node]
                except:
                    for x in parent_map:
                        if parent_map[x] is not None and node.board == x.board:
                            node = parent_map[x]
            return solution
        node.generate_children(parent_map, complex_heuristic=True)
        to_visit = node.children + to_visit
        to_visit.sort(key=lambda x: x.heuristic, reverse=True)
    return None


if __name__ == "__main__":
    root = ThreePuzzle_Node([3,1,2,None])
    solution = BFS_Solution(root)
    print("BFS solution = [", end='')
    for i in solution:
        print(i, '\b, ', end='')
    print("\b\b]")

    solution = Branch_Bound_Solution(root)
    print("Branch and Bound solution = [", end='')
    for i in solution:
        print(i, '\b, ', end='')
    print("\b\b]")

    solution = Branch_Bound_Simple_Heuristic_Solution(root)
    print("Branch and Bound Simple Heuristic solution = [", end='')
    for i in solution:
        print(i, '\b, ', end='')
    print("\b\b]")

    solution = Branch_Bound_Complex_Heuristic_Solution(root)
    print("Branch and Bound Complex Heuristic solution = [", end='')
    for i in solution:
        print(i, '\b, ', end='')
    print("\b\b]")
