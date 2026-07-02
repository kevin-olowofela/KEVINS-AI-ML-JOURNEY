def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def find_first_occurrence(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    result = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            result = mid_index
            right_index = mid_index - 1      
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return result


def find_last_occurrence(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    result = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            result = mid_index
            left_index = mid_index + 1       
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return result


def find_all_occurrences(numbers_list, number_to_find):
    first = find_first_occurrence(numbers_list, number_to_find)

    if first == -1:
        return []

    last = find_last_occurrence(numbers_list, number_to_find)

    return list(range(first, last + 1))


if __name__ == "__main__":
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    index = binary_search(numbers, number_to_find)
    print(f"Binary search found {number_to_find} at index {index}")

   
    indices = find_all_occurrences(numbers, number_to_find)
    print(f"Indices of occurrences of {number_to_find} are {indices}")