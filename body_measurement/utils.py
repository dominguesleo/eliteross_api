import math

def cm_to_inches(cm):
    return cm / 2.54

def kg_to_lbs(kg):
    return kg * 2.20462

def siri(body_density=None):
    if body_density:
        return 495 / body_density - 450
    return None

def central_adiposity_index(subscapular_skf=None, suprailiac_skf=None):
    if subscapular_skf and suprailiac_skf:
        return subscapular_skf * suprailiac_skf
    return None

def peripheral_adiposity_index(triceps_skf=None, biceps_skf=None):
    if triceps_skf and biceps_skf:
        return triceps_skf + biceps_skf
    return None

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

def waist_height_ratio(waist, height):
    if waist and height:
        return waist / height
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

def petroski(gender=None, age=None, triceps_skf=None, subscapular_skf=None, suprailiac_skf=None, calf_skf=None):
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

def faulkner(gender=None, triceps_skf=None, subscapular_skf=None, suprailiac_skf=None, abdomen_skf=None):
    if not gender:
        return None
    skf_values = [triceps_skf, subscapular_skf, suprailiac_skf, abdomen_skf]
    if any(value is None for value in skf_values):
        return None

    if gender == "Male":
        return 5.783 + (0.153 * sum(skf_values))
    return None

def sloan(gender=None, subscapular_skf=None, thigh_skf=None, triceps_skf=None, suprailiac_skf=None):
    if not gender:
        return None

    if gender == "Male" and subscapular_skf and thigh_skf:
        return 1.1043 - (0.001327 * thigh_skf) - (0.00131 * subscapular_skf)
    if gender == "Female" and triceps_skf and suprailiac_skf:
        return 1.0764 - (0.00081 * suprailiac_skf) - (0.00088 * triceps_skf)
    return None

def guedes(gender=None, triceps_skf=None, abdomen_skf=None, suprailiac_skf=None, thigh_skf=None, subscapular_skf=None):
    if not gender:
        return None

    male_skf_values = [triceps_skf, abdomen_skf, suprailiac_skf]
    female_skf_values = [thigh_skf, subscapular_skf, suprailiac_skf]
    if gender == "Male" and all(value is not None for value in male_skf_values):
        return 1.1714 - (0.0671 * math.log10(sum(male_skf_values)))
    if gender == "Female" and all(value is not None for value in female_skf_values):
        return 1.1665 - (0.0706 * math.log10(sum(female_skf_values)))
    return None

def jackson_pollock(gender=None, age=None, chest_skf=None, abdomen_skf=None, thing_skf=None, mid_axillary_skf=None, triceps_skf=None, suprailiac_skf=None, subscapular_skf=None):
    if not gender or not age:
        return None

    male_skf_values = [chest_skf, abdomen_skf, thing_skf, mid_axillary_skf, triceps_skf, suprailiac_skf, subscapular_skf]
    female_skf_values = [triceps_skf, suprailiac_skf, abdomen_skf, thing_skf]
    if gender == "Male" and all(values is not None for values in male_skf_values):
        return 1.112 - (0.00043499 * sum(male_skf_values)) + (0.00000077 * (sum(male_skf_values)**2)) - (0.00028826 * age)
    if gender == "Female" and all(values is not None for values in female_skf_values):
        return 1.096095 - (0.0006952 * sum(female_skf_values)) + (0.0000011 * (sum(female_skf_values)**2)) - (0.0000714 * age)
    return None

def weltman(gender=None, abdomen_circ=None, weight=None, height=None):
    if not gender:
        return None

    if gender == "Male" and abdomen_circ and weight:
        return (0.31457 * abdomen_circ) - (0.10969 * weight) + 10.8336
    if gender == "Female" and abdomen_circ and weight and height:
        return (0.11077 * abdomen_circ) - (0.17666 * height * 100) + (0.187 * weight) + 51.03301
    return None

def navy_body_fat(gender=None, height=None, waist_circ=None, neck_circ=None, hip_circ=None):
    if not gender or not height:
        return None
    height = cm_to_inches(height)

    if gender == "Male" and waist_circ and neck_circ:
        waist_circ = cm_to_inches(waist_circ)
        neck_circ = cm_to_inches(neck_circ)
        return 86.010 * math.log10(waist_circ - neck_circ) - 70.041 * math.log10(height) + 36.76

    if gender == "Female" and waist_circ and neck_circ and hip_circ:
        waist_circ = cm_to_inches(waist_circ)
        neck_circ = cm_to_inches(neck_circ)
        hip_circ = cm_to_inches(hip_circ)
        return 163.205 * math.log10(waist_circ + hip_circ - neck_circ) - 97.684 * math.log10(height) - 78.387
    return None

def ymca(gender=None, weight=None, waist_circ=None):
    if not gender or not weight or not waist_circ:
        return None
    if gender == "Male" or gender == "Female":
        return (4.15 * math.log10(cm_to_inches(waist_circ))) - (0.082 * math.log10(kg_to_lbs(weight))) - (98.42 if gender == "Male" else 76.76)
    return None

def deurenberg(gender=None, age=None, weight=None, height=None):
    if not gender or not age or not weight or not height:
        return None
    if gender == "Male" or gender == "Female":
        return (1.2 * imc(weight, height)) + (0.23 * age) - (10.8 * 1 if gender == "Male" else 0) - 5.4
    return None
