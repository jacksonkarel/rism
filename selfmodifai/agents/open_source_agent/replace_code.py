import ast
import astunparse


def create_mapping(tree):
    """
    Traverse an AST and create a mapping for classes, functions, and simple variable assignments based on their names.
    """
    mapping = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            mapping[node.name] = node
        elif isinstance(node, ast.Assign):
            # Handle simple variable assignments
            for target in node.targets:
                if isinstance(target, ast.Name):
                    mapping[target.id] = node
    return mapping


def replace_nodes(original_tree, replacement_mapping):
    """
    Replace nodes in the original_tree with nodes in replacement_mapping.
    """

    class NodeReplacer(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            return replacement_mapping.get(node.name, node)

        def visit_ClassDef(self, node):
            return replacement_mapping.get(node.name, node)

        # Add more visit_ methods for other node types (e.g., Assign) if needed

    replacer = NodeReplacer()
    return replacer.visit(original_tree)


def replace_code(revised_code):
    gpt_dev_train_path = "gpt-dev/train.py"
    # Load and parse both files into ASTs
    with open(gpt_dev_train_path, "r") as file:
        original_code = file.read()
        original_tree = ast.parse(original_code)

    revised_tree = ast.parse(revised_code)

    # Create mapping from the revised file
    replacement_mapping = create_mapping(revised_tree)

    # Replace nodes in the original tree
    new_tree = replace_nodes(original_tree, replacement_mapping)

    # Convert the modified AST back into code
    new_code = astunparse.unparse(new_tree)

    # Write the modified code back to a file
    with open(gpt_dev_train_path, "w") as file:
        file.write(new_code)
