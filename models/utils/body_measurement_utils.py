import math

def imc(weight=None, height=None):
    if weight and height:
        return weight / (height ** 2)
    return None

def rcq(waist, hip):
    if waist and hip:
        return waist / hip
    return None

def ic(waist, weight, height):
    if waist and weight and height:
        return waist / (0.109 * math.sqrt(weight/height))
    return None

def pollock_3(gender=None, age=None ,chest_skf=None, abdomen_skf=None,triceps_skf=None, suprailiac_skf=None,thigh_skf=None):
    if not gender or not age:
        return None
    if gender == "Male" and age and chest_skf and abdomen_skf and thigh_skf:
        sum_skf = chest_skf + abdomen_skf + thigh_skf
        return (1.10938 - (0.0008267 * sum_skf) + (0.0000016 * (sum_skf)**2 - (0.0002574 * age)))
    if gender == "Female" and age and triceps_skf and suprailiac_skf and thigh_skf:
        sum_skf = triceps_skf + suprailiac_skf + thigh_skf
        return (1.0994921 - (0.0009929 * sum_skf) + (0.0000023 * (sum_skf)**2 - (0.0001392 * age)))
    return None

def pollock_7(gender=None, age=None, chest_skf=None, mid_axillary_skf=None, subscapular_skf=None, triceps_skf=None, abdomen_skf=None, thigh_skf=None, suprailiac_skf=None):
    if not gender or not age:
        return None
    skf_values = [chest_skf, mid_axillary_skf, subscapular_skf, triceps_skf, abdomen_skf, thigh_skf, suprailiac_skf]
    if any(value is None for value in skf_values):
        return None

    sum_skf = sum(skf_values)
    if gender == "Male":
        return 1.112 - (0.00043499 * sum_skf) + (0.00000055 * (sum_skf)**2 - (0.00028826 * age))
    if gender == "Female":
        return 1.097 - (0.00046971 * sum_skf) + (0.00000056 * (sum_skf)**2 - (0.00012828 * age))
    return None

def petroski_4(gender=None, age=None, triceps_skf=None, subscapular_skf=None, suprailiac_skf=None, calf_skf=None):
    if not gender or not age:
        return None
    skf_values = [triceps_skf, subscapular_skf, suprailiac_skf, calf_skf]
    if any(value is None for value in skf_values):
        return None

    sum_skf = sum(skf_values)
    if gender == "Male":
        return 1.10726863 - (0.00081201 * sum_skf) + (0.00000212 *(sum_skf)**2 - (0.00041761 * age))
    if gender == "Female":
        return 1.1954713 - (0.07513507 * math.log10(sum_skf)) - (0.00041072 * age)
    return None



