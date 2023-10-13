#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    score_times_weight = 0
    if not my_list:
        return 0
    for score, weight in my_list:
        total_weight += weight
        score_times_weight += score * weight
    if total_weight == 0:
        return 0
    average = score_times_weight / total_weight
    return average
