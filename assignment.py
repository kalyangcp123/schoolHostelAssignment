def schoolHostelAssignment(class_max_size, AV, BV, ANV, BNV, NA):

    id = input("enter the roll number:")
    if len(id) != 4:
        raise Exception('id must be 4 digits')  # roll number should be 4 digits

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
    while i < n:
        schoolHostelAssignment(class_max_size, AV, BV, ANV, BNV, NA)
        i = i+1
    print("final output is")
    print("AV:", AV)
    print("BV:", BV)
    print("ANV:", ANV)
    print("BNV:", BNV)
    print("NA:", NA)




