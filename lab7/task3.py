def rule_sequence(s, rules):
    for rule in rules:
    s = rule(s)
    if s == None: break
return s


def rule_sequence_recurse(s, rules):
    rule = rules.pop()
    s = rule(s)
    if s == None: return s
    rule_sequence_recurse(s, rules)