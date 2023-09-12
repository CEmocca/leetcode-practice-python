from .tree import TreeNode
from typing import Optional

# root -> left -> right
def print_tree_pre_order(root: Optional[TreeNode]):
    if not root:
        return
    
    print(root.val)
    print_tree_pre_order(root.left)
    print_tree_pre_order(root.right)

# left -> root -> right
def print_tree_in_order(root: Optional[TreeNode]):
    if not root:
        return

    print_tree_pre_order(root.left)
    print(root.val)
    print_tree_pre_order(root.right)

# left -> right -> root    
def print_tree_post_order(root: Optional[TreeNode]):
    if not root:
        return

    print_tree_pre_order(root.left)
    print_tree_pre_order(root.right)
    print(root.val)

def create_binary_tree(elements: list[int]) -> Optional[TreeNode]:
    root_node = TreeNode(elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if not x:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

# code from: https://leetcode.com/discuss/interview-question/1954462/pretty-printing-binary-trees-in-python-for-debugging
def print_pretty_binary_tree(root):
    lines, *_ = _display_aux(root)
    for line in lines:
        print(line)

def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % self.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _display_aux(self.left)
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _display_aux(self.right)
        s = '%s' % self.val
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(self.left)
    right, m, q, y = _display_aux(self.right)
    s = '%s' % self.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2