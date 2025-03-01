import random

class GridNode:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DepthFirstSearch:
    def __init__(self):
        self.directions = [(1, 0, "Down"), (-1, 0, "Up"), (0, 1, "Right"), (0, -1, "Left")]
        self.size = 0
        self.start = None
        self.end = None
        self.found = False
        self.solution_path = []
        self.node_order = []

    def create_grid(self):
        self.size = random.randint(4, 7)
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def find_valid_position(self, grid):
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if grid[x][y] == 1:
                return x, y

    def start_search(self):
        grid = self.create_grid()
        print("\nGenerated Grid:")
        for row in grid:
            print(" ".join(map(str, row)))

        start_x, start_y = self.find_valid_position(grid)
        end_x, end_y = self.find_valid_position(grid)
        self.start = GridNode(start_x, start_y, 0)
        self.end = GridNode(end_x, end_y, float("inf"))

        print(f"\nStart: ({self.start.x}, {self.start.y})")
        print(f"End: ({self.end.x}, {self.end.y})\n")

        visited = [[False] * self.size for _ in range(self.size)]
        self.solution_path = []
        self.node_order = []
        self.found = False

        print("DFS Traversal:")
        self.execute_dfs(grid, self.start, visited, [])

        if self.found:
            print("\nPath Discovered!")
            print("Steps Taken:", self.end.depth)
            print("Node Traversal Order:", self.node_order)
        else:
            print("\nNo Path Found.")

    def execute_dfs(self, grid, node, visited, current_path):
        if self.found:
            return

        visited[node.x][node.y] = True
        current_path.append((node.x, node.y))
        self.node_order.append((node.x, node.y))

        if node.x == self.end.x and node.y == self.end.y:
            self.found = True
            self.end.depth = node.depth
            print("\nDFS Solution Path:")
            print(" → ".join([f"({x},{y})" for x, y in current_path]))
            return

        for dx, dy, direction in self.directions:
            nx, ny = node.x + dx, node.y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and grid[nx][ny] == 1 and not visited[nx][ny]:
                print(f"{direction} → ({nx},{ny})")
                self.execute_dfs(grid, GridNode(nx, ny, node.depth + 1), visited, current_path[:])
                if self.found:
                    return

        visited[node.x][node.y] = False


def main():
    dfs_runner = DepthFirstSearch()
    dfs_runner.start_search()

if __name__ == "__main__":
    main()
