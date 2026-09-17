def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [1, 2, 2, 3, 4, 4, 5]

new_list = remove_duplicates(numbers)

print(new_list)