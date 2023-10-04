class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BSPNode:
    def __init__(self, line):
        self.line = line
        self.left = None
        self.right = None

def bsp(lines, start_index):
    if not lines or start_index < 0 or start_index >= len(lines):
        return None

    median_index = start_index
    median_line = lines[median_index]

    node = BSPNode(median_line)

    left_lines = []
    right_lines = []

    for i, line in enumerate(lines):
        if i != median_index:
            if intersects(median_line, line):
                left_lines.append(line)
                right_lines.append(line)
            elif direction(line.start, median_line):
                left_lines.append(line)
            else:
                right_lines.append(line)

    node.left = bsp(left_lines, 0)
    node.right = bsp(right_lines, 0)

    return node

def intersects(line_a, line_b):
    return (direction(line_a.start, line_b) != direction(line_a.end, line_b)) and \
           (direction(line_b.start, line_a) != direction(line_b.end, line_a))

def print_tree(node):
    if node is None:
        return

    print(f"Line: ({node.line.start.x},{node.line.start.y}) ,({node.line.end.x},{node.line.end.y})")
    print_tree(node.left)
    print_tree(node.right)

def in_order_traversal(node):
    if node is None:
        return

    in_order_traversal(node.left)
    print(f"Line: ({node.line.start.x},{node.line.start.y}) , ({node.line.end.x},{node.line.end.y})")
    in_order_traversal(node.right)

def direction(point, line):
    vector1_x = line.end.x - line.start.x
    vector1_y = line.end.y - line.start.y
    vector2_x = point.x - line.start.x
    vector2_y = point.y - line.start.y

    cross_product = (vector1_x * vector2_y) - (vector1_y * vector2_x)

    return cross_product > 0

if __name__ == "__main__":
    lines = [
        Line(Point(5, 0), Point(5, 10)),  # Head Node (Root)
        Line(Point(2, 0), Point(2, 5)),  # Leaf 1
        Line(Point(8, 0), Point(8, 5)),  # Node
        Line(Point(1, 0), Point(1, 3)),  # Leaf 2
        Line(Point(4, 0), Point(4, 3)),  # Node
        Line(Point(6, 0), Point(6, 3)),  # Node
        Line(Point(9, 0), Point(9, 3)),  # Leaf 3
        Line(Point(0, 0), Point(0, 1)),  # Leaf 4
        Line(Point(3, 0), Point(3, 1)),  # Node
        Line(Point(7, 0), Point(7, 1)),  # Node
        Line(Point(10, 0), Point(10, 1)),  # Leaf 5
        Line(Point(2, 1), Point(2, 3)),  # Node
        Line(Point(4, 1), Point(4, 3)),  # Node
        Line(Point(6, 1), Point(6, 3)),  # Leaf 6
        Line(Point(8, 1), Point(8, 3)),  # Node
        Line(Point(1, 1), Point(1, 2)),  # Leaf 7
        Line(Point(9, 1), Point(9, 2))  # Leaf 8
    ]


    start_index = 0

    root = bsp(lines, start_index)

    print("\nIn-order traversal of the BSP tree:")
    in_order_traversal(root)
    print("BSP Tree:")
    print_tree(root)
