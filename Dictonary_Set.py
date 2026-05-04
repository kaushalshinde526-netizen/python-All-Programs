# =========================================
# PYTHON DICTIONARY + SET (FULL PRACTICE)
# =========================================

# -----------------------------------------
# 🔹 WHY DICTIONARY?
# -----------------------------------------
# Dictionary is used to store data in key-value pairs
# Fast lookup (O(1)) → useful in real-world apps like:
# - user data
# - API response
# - JSON data handling

# =========================================
# 1. BASIC DICTIONARY
# =========================================
student = {
    "name": "Kaushal",
    "age": 23,
    "course": "MCA"
}

print("Student:", student)


# =========================================
# 2. ACCESS VALUES
# =========================================
# [] → error if key not present
# get() → safe access (returns None if not found)

print(student["name"])
print(student.get("age"))


# =========================================
# 3. UPDATE / ADD
# =========================================
student["age"] = 24   # update
student["city"] = "Kalyan"  # add new key

print("Updated:", student)


# =========================================
# 4. DELETE
# =========================================
del student["city"]        # delete by key
student.pop("course")      # remove & return value

print("After delete:", student)

# student.clear()  # removes everything


# =========================================
# 5. LOOPING
# =========================================
# Used in real apps to process data

for key, value in student.items():
    print(key, ":", value)


# =========================================
# 6. IMPORTANT METHODS
# =========================================
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# =========================================
# 7. DICTIONARY COMPREHENSION 🔥
# =========================================
# Used for quick transformations

squares = {x: x*x for x in range(1, 6)}
print("Squares:", squares)


# =========================================
# 8. MERGE DICTIONARIES
# =========================================
d1 = {"a": 1}
d2 = {"b": 2}

merged = d1 | d2
print("Merged:", merged)


# =========================================
# 9. FREQUENCY COUNT (INTERVIEW)
# =========================================
# Used in text processing, analytics

data = [1, 2, 2, 3, 3, 3]

freq = {}
for i in data:
    freq[i] = freq.get(i, 0) + 1

print("Frequency:", freq)


# =========================================
# 10. SORT DICTIONARY
# =========================================
d = {"a": 3, "b": 1, "c": 2}

sorted_by_key = dict(sorted(d.items()))
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))

print("Sort by key:", sorted_by_key)
print("Sort by value:", sorted_by_value)


# =========================================
# 11. REVERSE DICTIONARY
# =========================================
# Swap key ↔ value

rev = {v: k for k, v in d.items()}
print("Reversed:", rev)


# =========================================
# 12. WORD FREQUENCY (REAL USE 🔥)
# =========================================
text = "python is easy python is powerful"

words = text.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Word Frequency:", freq)



# 🔹 WHY SET?
# -----------------------------------------
# Set stores unique values (no duplicates)
# Fast operations (union, intersection)
# Used in:
# - removing duplicates
# - membership checking
# - mathematical operations



# 13. BASIC SET
s = {1, 2, 3, 3, 4}

print("Set:", s)  # duplicates removed automatically



# 14. ADD / REMOVE
s.add(5)          # add element
s.remove(2)       # remove element (error if not exist)
s.discard(10)     # safe remove (no error)

print("Updated Set:", s)



# 15. LOOPING SET

for i in s:
    print("Element:", i)


# 16. SET OPERATIONS (IMPORTANT)
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)           # combine
print("Intersection:", a & b)    # common
print("Difference:", a - b)      # only in a
print("Symmetric Diff:", a ^ b)  # not common



# 17. REMOVE DUPLICATES FROM LIST
data = [1, 2, 2, 3, 4, 4]

unique = list(set(data))
print("Unique List:", unique)


# 18. CHECK MEMBERSHIP
# Very fast (O(1))

if 3 in a:
    print("3 exists in set")



# 19. FROZENSET (IMMUTABLE SET)
# Used when data should not change

fs = frozenset([1, 2, 3])
print("FrozenSet:", fs)


