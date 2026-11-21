from collections import Counter
def first_unique(s):
    count=Counter(s)
    for ch in s:
        if count == 1:
            return ch
    return None
print(first_unique("swiss"))