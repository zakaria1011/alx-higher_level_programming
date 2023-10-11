#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_student = next(iter(a_dictionary))
    best_score = a_dictionary[best_student]
    for student, score in a_dictionary.items():
        if score > best_score:
            best_score = score
            best_student = student
    return best_student
