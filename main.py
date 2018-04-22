class ThreePuzzle_Node:
    def __init__(self, board=[3, 1, 2, None]):
        self.board = board
        self.children = []

    def __str__(self):
        return str(self.board)

    def generate_children(self, parent_map):
        blank_location = self.board.index(None)
        for i in range(0, 4):
            if i != 3 - blank_location and i != blank_location:
                new_board = self.board[:]
                new_board[blank_location], new_board[i] = new_board[i], new_board[blank_location]
                child = ThreePuzzle_Node(new_board)
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


if __name__ == "__main__":
    root = ThreePuzzle_Node([3,1,2,None])
    solution = BFS_Solution(root)
    print("BFS solution = [", end='')
    for i in solution:
        print(i, '\b, ', end='')
    print("\b\b]")
