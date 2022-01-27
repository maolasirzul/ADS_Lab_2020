# Importing file
import time

from bigO import BigO

start_time = time.time()

# Stocks list
manufacturer_a = [16, 5, 11, 9, 6, 8, 98, 100, 54]
manufacturer_b = [24, 21, 18, 23, 34, 17, 190, 2, 91, 88, 189, 187]
manufacturer_c = [32, 23, 42, 18, 21, 7, 44, 92, 33, 33]
manufacturer_d = [3, 24, 68, 19, 242, 6, 67, 982, 543, 123, 543, 876, 555]
manufacturer_z = [4, 16, 96, 42, 68, 21, 1, 100]

# =============Finding duplication=======================
# Adding all the manufactures's list in one variable
duplication_list = manufacturer_a + manufacturer_b + manufacturer_c + manufacturer_d + manufacturer_z


# Function for duplication
def duplication_check(seq):
    value = set([])
    value_add = value.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    value_twice = set(x for x in seq if x in value or value_add(x))
    return set(value_twice)


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


print("Manufacturer A minmum and maximum value:", min_max_value(manufacturer_a))
print("Manufacturer B minmum and maximum value:", min_max_value(manufacturer_b))
print("Manufacturer C minmum and maximum value:", min_max_value(manufacturer_c))
print("Manufacturer D minmum and maximum value:", min_max_value(manufacturer_d))
print("Manufacturer Z minmum and maximum value:", min_max_value(manufacturer_z))

# ================Highest and lowest value ===============

# highest and lowest value from all manufacturer's

highest_lowest_a = min_max_value(manufacturer_a)
highest_lowest_b = min_max_value(manufacturer_b)
highest_lowest_c = min_max_value(manufacturer_c)
highest_lowest_d = min_max_value(manufacturer_d)
highest_lowest_z = min_max_value(manufacturer_z)

high_low_list = highest_lowest_a + highest_lowest_b + highest_lowest_c + highest_lowest_d + highest_lowest_z

print("List of all manufacturer's highest and lowest car tire strength",
      high_low_list)


# Insert sorting

def insert_sorting(numbers):
    """ This function will
  compare with each number to swap"""

    for i in range(1, len(numbers)):
        anchor = numbers[i]  # calling the number in a variable
        j = i - 1  # one less then current number
        while j >= 0 and anchor < numbers[j]:
            numbers[j + 1] = numbers[j]  # swapping from left to right
            j = j - 1
        numbers[j + 1] = anchor  # terminated loop


list_a = [5, 100, 2, 190, 7, 92, 3, 982, 1, 100]
insert_sorting(list_a)
print("The sorted list is:", list_a)
# the minimum and maximum value from the sorted list
print("The minimum and maximum value from all manufacturer is:",
      min_max_value(list_a))


# Index position of minimum and maximum vale from the array
def index_search(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            return i
    return -1


iteam_small = index_search([4, 16, 96, 42, 68, 21, 1, 100], 1)
print("The index value of 1 is:", iteam_small)
iteam_larg = index_search([3, 24, 68, 19, 242, 6, 67, 982, 543, 123, 543, 876, 555], 982)
print("The index value of 982 is:", iteam_larg)

end_time = time.time()

print("Time taken for the solution is:", end_time - start_time, "seconds")

# ============BigO===========
lib = BigO()
complexity = lib.test(insert_sorting, "random")
complexity = lib.test(, "random")
