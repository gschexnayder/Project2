import math

def final_grade_calc(current_grade, desired_grade, final_weight):
    """Calculate grade needed for the final project/exam"""
    return (desired_grade - (1 - final_weight) * current_grade) / final_weight