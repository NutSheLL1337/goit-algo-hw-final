import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
import numpy as np

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [highlight_colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color_gradient(steps, start_color="#1296F0", end_color="#E0F7FF"):
    if steps <= 1:
        return [start_color]  # Повертаємо початковий колір, якщо steps 0 або 1
    start_rgb = np.array(to_rgb(start_color))
    end_rgb = np.array(to_rgb(end_color))
    gradient = [(to_hex((1 - i / (steps - 1)) * start_rgb + (i / (steps - 1)) * end_rgb)) for i in range(steps)]
    return gradient


def depth_first_search_visualize(root):
    stack = [root]
    visited_colors = generate_color_gradient(steps=len(stack), start_color="#1296F0", end_color="#E0F7FF")
    step = 0
    highlight_colors = {}

    while stack:
        current_node = stack.pop()
        if current_node:
            highlight_colors[current_node.id] = visited_colors[step % len(visited_colors)]
            draw_tree(root, highlight_colors)
            step += 1
            stack.extend([current_node.right, current_node.left])

def breadth_first_search_visualize(root):
    queue = [root]
    visited_colors = generate_color_gradient(steps=len(queue), start_color="#1296F0", end_color="#E0F7FF")
    step = 0
    highlight_colors = {}

    while queue:
        current_node = queue.pop(0)
        if current_node:
            highlight_colors[current_node.id] = visited_colors[step % len(visited_colors)]
            draw_tree(root, highlight_colors)
            step += 1
            queue.extend([current_node.left, current_node.right])

# Приклад дерева
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# Візуалізація обходу в глибину
depth_first_search_visualize(root)

# Візуалізація обходу в ширину
breadth_first_search_visualize(root)
