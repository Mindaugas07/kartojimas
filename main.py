# from typing import Dict, List
 
 
# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"]
# }
 
# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"]
# }
 
# people = [person, person1]
 


# def get_most_popular_language(people: List[Dict]) -> str:
#     # create dictionary with language counts
#     # for person in people:
#         # get persons languages
#         # for language in languages:
#             # if language is new:
#                 # add key to dictionary with language counts
#             # else if langauge is not new:
#                 # add count +1 to already existing language in dictionary with language counts
#     languages_dictionary = {}
#     for person in people:
#         languages = person.get("languages")
#         for language in languages:
#             languages_dictionary[language] = languages_dictionary.get(language, 0) + 1


#     max_key = None
#     max_value = None
#     for key, value in languages_dictionary.items():
#         if max_value == None or max_value < value:
#             max_key, max_value = key, value
#     return max_key

   
#     # return max(languages_dictionary, key=languages_dictionary.get)

# print(get_most_popular_language(people))

# dict_one = {"a": 10, "b": 15, "c": 45}
# dict_two = {"d": 11, "b": 16, "c": 55}

# def custom_dictionary_update(
#     first_dictionary: Dict, second_dictionary: Dict, overwrite: bool = True
# ) -> Dict:
#     if overwrite == True:
#         first_dictionary.update(second_dictionary)
#     else:
#         for key, value in second_dictionary.items():
#             if key not in first_dictionary:
#                 first_dictionary[key] = value
#     return first_dictionary

#     #   do not overwrite values from the first dictionary, only add new values from the second one.



# print(custom_dictionary_update(dict_one, dict_two, False))

# person = {
#     "name": "Vytautas",
#     "surname": "Sluckas",
#     "ip": "127.0.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Lithuanian", "English", "Norwegian"],
# }
 
# person1 = {
#     "name": "Tomas",
#     "surname": "BLABLABA",
#     "ip": "162.2.0.2",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }
 
# person2 = {
#     "name": "Tom",
#     "surname": "Edison",
#     "ip": "127.2.0.1",
#     "programming_language": "python",
#     "address": {"Street": "some street", "House Number": "some house number"},
#     "languages": ["Latvian", "English", "Swedish"],
# }
 
 
# Function with Return Value
# Create a function called calculate_area that takes in the length and width of a rectangle and returns its area.

# def calculate_area(length: int, width: int) -> int:
#     area: int = length * width
#     return f"The area of reactangle which has length {length} and width {width} is {area}"


# print(calculate_area(4, 8))
# print(calculate_area(1, 0))

# Function with Default Parameters
# Create a function called power_value that takes in a base and an exponent (with a default value of 2) and returns the result of the base raised to the exponent.

# def power_value(base: int, exponent=2) -> int:
#     return base ** exponent

# print(power_value(7))
# print(power_value(4, 9))


# Function with Variable Number of Arguments
# Create a function called calculate_sum that takes in any number of arguments and returns their sum.

# def calculate_sum(*args) -> int:
#     return sum(args)

# print(calculate_sum(1, 8, 9, 9))

# a = 3
# b = 3
# c = 8

# print(calculate_sum(a, b, c))

# z = 2
# x = 100

# print(calculate_sum(x, z, c))

# Create a function called factorial that takes in a number n and computes its factorial using recursion.

# def factorial(n: int) -> int:
#     if n == 1:
#        return n
#     else:
#        return n*factorial(n-1)
    
# n = 6
    
# if n < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif n == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", n, "is", factorial(n))

# from typing import List

# def highest_rank(arr: List[int]) -> int:
#     from_array_to_dict: dict = {key: arr.count(key) for key in arr}
#     # for number in arr:
#     #     # from_array_to_dict[number] = from_array_to_dict.get(number, 0) + 1
#     #     from_array_to_dict[number] = arr.count(number)
    
#     max_value = None
#     for key, value in from_array_to_dict.items():
#         if max_value == None or max_value < value:
#             max_value = value

#     keys = [k for k, v in from_array_to_dict.items() if v == max_value]
#     return max(keys)

# print(highest_rank([10, 10, 8, 12, 12, 6, 4, 10, 10]))

# Creating a list of squares of numbers from 1 to 10

# list_of_square = [number**2 for number in range(1, 11)]
# print(list_of_square)

# Filtering even numbers from a list from 1 to 10

# even_number_list = [number for number in range(1, 11) if number % 2 == 0]
# print(even_number_list)

# Write a Python program to create a dictionary where keys are numbers from 1 to 5 and values are their cubes.

# nice_dict = {key: key**3 for key in range(1, 6)}
# print(nice_dict)

# Generate a list containing the squares of numbers from 1 to 20 but exclude numbers that are divisible by both 3 and 4.

# list_of_numbers = [number**2 for number in range(1, 21) if not (number % 3 == 0 and number % 4 == 0)]
# print(list_of_numbers)


# Generate a list of tuples where each tuple contains the index and the value of the element from the original list, but exclude elements with a value less than 10.
# original_list = [5, 15, 8, 20, 12, 7, 18]
 
# list_of_tuples = [(index, value) for index, value in enumerate(original_list) if value > 10]
# print(list_of_tuples)
# # # Output: [(1, 15), (3, 20), (4, 12), (6, 18)]

# Create a dictionary where keys are the names from one list and values are the corresponding ages from another list, but only for names that have lengths greater than 4.
names = ['Alice', 'Bob', 'Charlie', 'David'] 
ages = [25, 30, 35, 40]

new_dictionary = {name: ages[index] for index, name in enumerate(names) if len(name) > 4}
print(new_dictionary)