def schoolHostelAssignment(class_max_size, AV, BV, ANV, BNV, NA, students):

    id = input("enter the roll number:")
    if len(id) != 4:
        raise Exception('id must be 4 digits')  # roll number should be 4 digits

    if id in students:
        return

    students.append(id)

    section = input("enter the class:")
    if section != 'A' and section != 'B':
        raise Exception('invalid class')  # invalid class

    food_pref = input("enter the food:")
    if food_pref != 'V' and food_pref != 'NV':
        raise Exception('invalid food preference')  # invalid food preferences

    if section == 'A' and food_pref == 'V' and len(AV) < class_max_size:
        AV.append(id)
    elif section == 'B' and food_pref == 'V' and len(BV) < class_max_size:
        BV.append(id)
    elif section == 'A' and food_pref == 'NV' and len(ANV) < class_max_size:
        ANV.append(id)
    elif section == 'B' and food_pref == 'NV' and len(BNV) < class_max_size:
        BNV.append(id)
    else:
        NA.append(id)


if __name__ == "__main__":
    n = int(input("enter no of students:"))  # get number of students
    class_max_size = int(n/4)
    i = 0
    AV = []
    BV = []
    ANV = []
    BNV = []
    NA = []
    students = []
    while i < n:
        schoolHostelAssignment(class_max_size, AV, BV, ANV, BNV, NA, students)
        i = i+1
    print("############ final output is #############")
    print("BV:", '[%s]' % ', '.join(map(str, BV)))
    print("AV:", '[%s]' % ', '.join(map(str, AV)))
    print("BNV:", '[%s]' % ', '.join(map(str, BNV)))
    print("ANV:", '[%s]' % ', '.join(map(str, ANV)))
    print("NA:", '[%s]' % ', '.join(map(str, NA)))





