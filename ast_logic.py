class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type
        self.left = left
        self.right = right
        self.value = value

from models import Node

def create_rule(rule_string):
    # Implement your own logic to parse the rule_string
    # This is a simple example; replace with your actual parsing logic
    return Node("operator", Node("operand", value="age > 30"), Node("operand", value="salary > 50000"))

def evaluate_rule(rule_string, data):
    # Implement your own rule evaluation logic here
    # This is just a placeholder for demonstration
    return True  # Change this based on actual evaluation logic

