from calendar import MONDAY


def mean(value):
    if isinstance(value, dict):
        # if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


monday_temperatures = [4, 5, 6, 5, 3, 1]
student_grades = {"Marry": 9.2, "Tudos": 7.8, "Anlen": 8.9}

print(mean(student_grades))
