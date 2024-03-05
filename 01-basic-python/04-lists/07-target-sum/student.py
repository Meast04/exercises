# Write your code here
def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if x == y:
                return True
    return False
