import sqlite3

def init_db():
    conn = sqlite3.connect('rule.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, rule_string TEXT)''')
    conn.commit()
    conn.close()

class Rule:
    def __init__(self, rule_string):
        self.rule_string = rule_string

    def save(self):
        conn = sqlite3.connect('rule.db')
        c = conn.cursor()
        c.execute('INSERT INTO rules (rule_string) VALUES (?)', (self.rule_string,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_rule_by_id(rule_id):
        conn = sqlite3.connect('rule.db')
        c = conn.cursor()
        c.execute('SELECT * FROM rules WHERE id = ?', (rule_id,))
        rule = c.fetchone()
        conn.close()
        return Rule(rule[1]) if rule else None  # Return None if rule is not found

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    # Method to serialize Node into a dictionary
    def to_dict(self):
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }
