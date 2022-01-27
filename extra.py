# Stocks list
manufacturer_a = [16, 5, 11, 9, 6, 8, 98, 100, 54]
manufacturer_b = [24, 21, 18, 23, 34, 17, 190, 2, 91, 88, 189, 187]
manufacturer_c = [32, 23, 42, 18, 21, 7, 44, 92, 33, 33]
manufacturer_d = [3, 24, 68, 19, 242, 6, 67, 982, 543, 123, 543, 876, 555]
manufacturer_z = [4, 16, 96, 42, 68, 21, 1, 100]

# =============Finding duplication=======================
# Adding all the manufactures's list in one variable
duplication_list = (manufacturer_a + manufacturer_b + manufacturer_c
                    + manufacturer_d + manufacturer_z)


# Function for duplication
def duplication_check(seq):
    value = set()
    value_add = value.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    value_twice = set(x for x in seq if x in value or value_add(x))
    # turn the set into a list (as requested)
    return list(value_twice)


check = duplication_check(duplication_list)

print('The duplicate values are:', check)


# =============Minimum & Maximum value for each Manufactures=============

# Function
def min_max_value(list):
    min_num = list[0]
    max_num = list[0]

    for i in list:
        if i <= min_num:
            min_num = i
        if i >= max_num:
            max_num = i
    return min_num, max_num


print("The minimum and maximum tire strength for Manufacture A is:",
      min_max_value(manufacturer_a))
print("The minimum and maximum tire strength for Manufacture B is:",
      min_max_value(manufacturer_b))
print("The minimum and maximum tire strength for Manufacture C is:",
      min_max_value(manufacturer_c))
print("The minimum and maximum tire strength for Manufacture D is:",
      min_max_value(manufacturer_d))
print("The minimum and maximum tire strength for Manufacture Z is:",
      min_max_value(manufacturer_z))

# ================Highest and lowest value ===============

# highest and lowest value from all manufactures's

highest_lowest_a = min_max_value(manufacturer_a)
highest_lowest_b = min_max_value(manufacturer_b)
highest_lowest_c = min_max_value(manufacturer_c)
highest_lowest_d = min_max_value(manufacturer_d)
highest_lowest_z = min_max_value(manufacturer_z)

high_low_list = (highest_lowest_a + highest_lowest_b + highest_lowest_c
                 + highest_lowest_d + highest_lowest_z)

print("List of all manufactures's highest and lowest car tire strength",
      high_low_list)


# Insert sorting

def insert_sorting(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor




if __name__ == '__main__':
    a = (5, 100, 2, 190, 7, 92, 3, 982, 1, 100)
    insert_sorting(a)
    print(a)
