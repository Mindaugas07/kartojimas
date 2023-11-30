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
# names = ['Alice', 'Bob', 'Charlie', 'David'] 
# ages = [25, 30, 35, 40]

# new_dictionary = {name: ages[index] for index, name in enumerate(names) if len(name) > 4}
# print(new_dictionary)

# Create a function calculate_total_salary that takes in the base salary and additional bonuses (as keyword arguments) for an employee. The function should consider
# a default bonus of 0 if none is provided. Use *args for handling multiple additional bonuses.

# Test cases
# print(calculate_total_salary(50000))  # Test with only base salary
# print(calculate_total_salary(50000, 2000, 3000))  # Test with base salary and additional bonuses
# print(calculate_total_salary(50000, 2000, 3000, health_insurance=1000, travel_allowance=1500))  # Test with kwargs

# def calculate_total_salary(base_salay: int, *args, **kwargs) -> int:
#     bonuses = 0
#     if args != None:
#         for arg in args:
#             bonuses += arg
#     if kwargs != None:
#         for kwarg in kwargs:
#             bonuses += kwargs[kwarg]
#     net_salary = base_salay + bonuses
#     return net_salary

# print(calculate_total_salary(50000))
# print(calculate_total_salary(50000, 2000, 3000))
# print(calculate_total_salary(50000, 2000, 3000, health_insurance=1000, travel_allowance=1500))







# Create a function generate_shopping_list that accepts a title for the list, defaulting to "My Shopping List," and any number of items using *args.
#  The function should return a formatted shopping list with the title and items.

# def generate_shopping_list(*args, title: str = "My Shopping List:", **kwargs) -> str:
#     list_of_products = [title]
#     for arg in args:
#         list_of_products.append(arg)
#     return list_of_products
   
# print(generate_shopping_list("milk", "bread", "eggs"))

# def domain_name(url):
#     replaces = ["http://", "www.", "https://"]
#     for replace_one in replaces:
#         url= url.replace(replace_one, "")
#     url = url.split(".")
#     return url[0]

# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]

# print(domain_name("http://github.com/carbonfive/raygun"))

# def make_readable(seconds: int) -> str:
#     hours = seconds // 3600
#     if hours < 10:
#         hours = "0" + str(hours)
#     minutes = seconds % 3600 // 60
#     if minutes < 10:
#         minutes = "0" + str(minutes)
#     seconds_format = seconds % 60
#     if seconds_format < 10:
#         seconds_format = "0" + str(seconds_format)
#     return f"{hours}:{minutes}:{seconds_format}"

# print(make_readable(35956))

# Create class that woud repesent weather. This class takes several parameters (wind speed (km/hour) and temperature(F))
# This class should be able to return weather conditions:
# 1) Weather temperature in K , C , F 
# 2) Wind speed in m/s , km/k , miles/h
# 3) Weather conditions : good (wind speed < 5m/s,  temp > 0C < 25 C) ,nommal (wind speed < 10m/s,  temp > -15C < 28 C), bad (wind speed > 10m/s,  temp < -15C or > 30 C) , savere (wind speed > 15m/s,  temp < -25C or > 40 C)

# Use inheritance, private/protected methods/attributes if needed.


# import logging
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# class Weather:

#     def __init__(self, wind_speed_kmph: float, temperature_fahr: float) -> None:
#         self.wind_speed_kmph: float = wind_speed_kmph
#         self.temperature_fahr: float = temperature_fahr

#     def get_temperature_in_kelvin(self) -> float:
#         k_temperature: float = 5 * (self.temperature_fahr - 32)/9 + 273.15
#         return round(k_temperature, 2)

#     def get_temperature_in_celcius(self) -> float:
#         c_temperature: float = 5 / 9 * (self.temperature_fahr - 32)
#         return round(c_temperature, 2)

#     def get_temperature_in_fahrenheit(self) -> float:
#         return self.temperature_fahr
    
#     def get_wind_speed_mps(self) -> float:
#         mps_speed: float = (self.wind_speed_kmph * 1000)/3600
#         return round(mps_speed, 2)
    
#     def get_wind_speed_kmph(self) -> float:
#         return self.wind_speed_kmph

#     def get_wind_speed_milesph(self) -> float:
#         milesph: float = 0.6214 * self.wind_speed_kmph
#         return round(milesph, 2)

#     def weather_conditions(self) -> str:
#         if self.get_wind_speed_mps() < 5.0 and 0.0 < self.get_temperature_in_celcius() < 25.0:
#             return f"Weather conditions are good"
#         elif self.get_wind_speed_mps() < 10.0 and -15.0 < self.get_temperature_in_celcius() < 28.0:
#             return f"Weather conditions are normal"
#         elif self.get_wind_speed_mps() > 10.0 and ((-25.0 < self.get_temperature_in_celcius() < -15.0) or (40.0 > self.get_temperature_in_celcius() > 30.0)):
#             return f"Weather conditions are bad"
#         elif self.get_wind_speed_mps() > 15.0 and (-25.0 > self.get_temperature_in_celcius() or self.get_temperature_in_celcius() > 40.0):
#             return f"Weather conditions are severe"



# measures_one = Weather(120, 150)


# print(measures_one.get_temperature_in_kelvin())
# print(measures_one.get_temperature_in_celcius())
# print(measures_one.get_wind_speed_mps())
# print(measures_one.get_wind_speed_milesph())
# print(measures_one.weather_conditions())


# Basic Banking System Challenge

#  Define a class called Account with the following attributes and methods:
#  - Attributes: account_number, account_holder, balance
#  - Methods: display_account_info() - prints information about the account

#  Create two subclasses, SavingsAccount and CheckingAccount, that inherit from Account.
#  Each subclass should have its own unique method, for example, earn_interest() for SavingsAccount
#  and deduct_fees() for CheckingAccount.

# class Account:
#     def __init__(self, account_number: str, account_holder: str, balance: float) -> None:
#         self.account_number: int = account_number
#         self.account_holder: str = account_holder
#         self.balance: float = balance

#     def display_account_info(self) -> str:
#         return f"Account {self.account_number} belongs to {self.account_holder} and has a balance of {self.balance}"

# class SavingAccount(Account):
#     def __init__(self, interest_percent: float, account_number: str, account_holder: str, balance: float) -> None:
#         super().__init__(account_number, account_holder, balance)
#         self.interest_percent = interest_percent

#     def earn_interests(self) -> float:
#         return f"With interest rate {self.interest_percent} and a balance {self.balance} you will earn {round(self.balance * self.interest_percent, 2)} each year."

# class CheckingAccount(Account):
#     def __init__(self, fee: float, account_number: str, account_holder: str, balance: float) -> None:
#         super().__init__(account_number, account_holder, balance)
#         self.fee: float = fee

#     def deduct_fees(self) -> float:
#         return f"{self.fee} will be deducted from your account each month and with balance {self.balance} it will be {self.balance * self.fee}."
    

# jonas_account = SavingAccount(0.1, "LT10232465400", "Jonas Jogailaitis", 45687.08)
# inga_account = CheckingAccount(0.01, "LT780215465465", "Inga Sninga", 12.0)

# print(jonas_account.display_account_info())
# print(inga_account.display_account_info())
# print(jonas_account.earn_interests())
# print(inga_account.deduct_fees())

# import subprocess

# lis = [5, 6, 7, 8, 9]
# i = 0

# print(lis[i])

# while True:
#     user_input = input()
#     if user_input == ">":
#         i += 1
#         try:
#             print(lis[i])
            
#         except IndexError as err:
#             i = len(lis) - 1
#             print(f"End of the list: {lis[i]}")
            
#     elif user_input == "<":
#         i -= 1
#         try:
#             if i > -1:
#                 print(lis[i])
#             else:
#                 i += 1  
#                 print (f"End of the list: {lis[i]}")
                          
#         except IndexError as err:
#             print(f"End of the list: {lis[i]}")
#     elif user_input == "q":
#         break

# Write a function that takes a list of integers and returns their average. Raise a TypeError if the input is not
# a list or if any element in the list is not an integer. Provide a solution that addresses this error.

# from typing import List

# list_of_integers: List[int] = [45, 12, [9, 7], 46]

# def average_from_list(list: List[int]) -> float:
#     try:
#         return sum(list) / len(list)
#     except TypeError as err:
#         print("Input is not a list or element in the list is not an integer")
#         # print(err)

# average_from_list(list_of_integers)

# Create a function that reads a file and returns its contents. Raise a FileNotFoundError if
# the file does not exist. Provide a solution that handles this error.

# def read_from_file(file_name: str):
#     if type(file_name) != str:
#         raise TypeError
#     with open(file_name) as f:
#         contents = f.read()
#         print(contents)


# try: 
#     read_from_file(5)
# except FileNotFoundError as err:
#     print("File does not exist!")
# except TypeError:
#     print("Not string was provided!")

# numbers = [5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562]
# numbers_not = [5, 47, 6, 485, 1, "a", 8, 184, 1, 7, 5, 52, 562]
# numbers_not_again = "5, 47, 6, 485, 1, 521, 8, 184, 1, 7, 5, 52, 562"
# def calculate_average(numb: list) -> float:
#     if type(numb) is not list or not numb:
#         raise TypeError("Not a list or is empty list")
#     numb_check = [x for x in numb if type(x) == int]
#     # print(numb_check)
#     if numb_check != numb:
#         raise TypeError("Not all items of the list are integers")
#     return round((sum(numb) / len(numb)), 2)
# def try_calculate_averages(*args: list) -> list:
#     averages = []
#     for arg in args:
#         try:
#             averages.append(calculate_average(arg))
#         except TypeError as e:
#             if str(e) == "Not a list or is empty list":
#                 print("Not a list or is empty list")
#             elif str(e) == "Not all items of the list are integers":
#                 print("Not all items of the list are integers")
#                 try:
#                     fixed_list = [int(x) for x in arg]
#                     averages.append(calculate_average(fixed_list))
#                 except ValueError:
#                     print("Unable to quickfix your problem!")
#         except Exception as e:
#             print(f"Unexpected problem {e}")
#     return averages
# print(try_calculate_averages(numbers, numbers_not, numbers_not_again))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    

