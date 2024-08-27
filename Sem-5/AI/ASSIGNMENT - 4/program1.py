class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self):
        self.diagnosis = []
        for rule in self.rules:
            if all(fact in self.facts for fact in rule['if']):
                self.diagnosis.append(rule['then'])

# Example rules for a simple car diagnosis system
rules = [
    {'if': ['engine_noise', 'oil_leak'], 'then': 'engine_issue'},
    {'if': ['brake_noise', 'brake_fade'], 'then': 'brake_problem'},
    {'if': ['battery_light', 'slow_start'], 'then': 'battery_issue'},
    {'if': ['overheating', 'coolant_leak'], 'then': 'cooling_system_issue'},
]

# Create knowledge base and add facts and rules
kb = KnowledgeBase()
kb.add_rule(rules[0])
kb.add_rule(rules[1])
kb.add_rule(rules[2])
kb.add_rule(rules[3])

# Add facts (symptoms)
kb.add_fact('engine_noise')
kb.add_fact('oil_leak')
kb.add_fact('brake_noise')

# Perform inference
kb.infer()

# Print inferred facts (diagnosis)

print("Facts (symptoms):")
for fact in kb.facts:
    print(fact)

print("Inferred facts (diagnosis):")
for d in kb.diagnosis:
    print(d)
