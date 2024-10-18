from flask import Flask, request, jsonify
from ast_logic import create_rule, evaluate_rule  # Ensure these functions are defined
from models import init_db, Rule, Node  # Import Node class

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    rule_ast = create_rule(rule_string)  # This should return a Node object
    # Save the rule to the database
    rule = Rule(rule_string=rule_string)
    rule.save()
    return jsonify({"message": "Rule created", "ast": rule_ast.to_dict()})  # Call to_dict() on the Node object

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    rule = Rule.get_rule_by_id(rule_id)
    
    if rule is None:
        return jsonify({"error": "Rule not found"}), 404
    
    result = evaluate_rule(rule.rule_string, data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
