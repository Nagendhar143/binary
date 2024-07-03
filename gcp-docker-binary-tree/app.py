# app.py
from flask import Flask, request, jsonify
from solution import Solution, TreeNode

app = Flask(__name__)

def build_tree(nodes):
    if not nodes:
        return None
    val = nodes.pop(0)
    root = TreeNode(val) if val is not None else None
    queue = [root]
    while nodes:
        node = queue.pop(0)
        if node:
            left_val = nodes.pop(0) if nodes else None
            node.left = TreeNode(left_val) if left_val is not None else None
            queue.append(node.left)
            if nodes:
                right_val = nodes.pop(0) if nodes else None
                node.right = TreeNode(right_val) if right_val is not None else None
                queue.append(node.right)
    return root

@app.route('/max_path_sum', methods=['POST'])
def max_path_sum():
    data = request.get_json()
    root = build_tree(data['root'])
    solution = Solution()
    result = solution.maxPathSum(root)
    return jsonify({'max_path_sum': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
