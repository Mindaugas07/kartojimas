# Challenge: Tax Calculation System

# Create a base class called `Income` with the following attributes:
#  - income_type (string): representing the type of income (e.g., salary, business, investment)
#  - amount (float): representing the amount of income

#  Create three derived classes: `Salary`, `Business`, and `Investment`, each inheriting from the `Income` class.
#  Each derived class should have an additional attribute:
#  - salary_grade (int) for `Salary`
#  - business_type (string) for `Business`
#  - investment_type (string) for `Investment`

#  Create a class called `TaxCalculator` with the following methods:
#  - calculate_tax(income): takes an `Income` object as a parameter and calculates the tax based on the income type.

#  Implement the tax calculation as follows:
#  - For `Salary` income, the tax is 20% of the amount.
#  - For `Business` income, the tax is 15% of the amount.
#  - For `Investment` income, the tax is 10% of the amount.

#  Create instances of each income type and calculate the tax using the `TaxCalculator`.

#  Bonus:
#  Create a class called `Person` with attributes:
#  - name (string)
#  - age (int)
#  - income (Income object)

#  Add a method to the `Person` class called `display_info` that prints the person's name, age, income type, and tax amount.

#  Create instances of the `Person` class and demonstrate the tax calculation and display information.

# class Income:
    
#     def __init__(self, income_type: str, amount: float) -> None:
#         self.income_type: str = income_type
#         self.amount: float = amount


# class Salary(Income):
    
#     def __init__(self, income_type: str, amount: float, salary_grade: int) -> None:
#         super().__init__(income_type, amount)
#         self.salary_grade: int = salary_grade


# class Business(Income):
    
#     def __init__(self, income_type: str, amount: float, business_type: str) -> None:
#         super().__init__(income_type, amount)
#         self.business_type: str = business_type


# class Investment(Income):
    
#     def __init__(self, income_type: str, amount: float, investment_type: str) -> None:
#         super().__init__(income_type, amount)
#         self.investment_type = investment_type


# class TaxCalculator:

#     def calculate_tax(self, income: "Income") -> float:
        
#         if income.income_type == "Salary":
#             return income.amount * 0.2
#         elif income.income_type == "Business":
#             return income.amount * 0.15
#         elif income.income_type == "Investment":
#             return income.amount * 0.10
        
# class Person:

#     def __init__(self, name: str, age: int, income: "Income") -> None:
#         self.name: str = name
#         self.age: int = age

#     def display_info(self, tax: "TaxCalculator", income: "Income") -> str:

#         return f"{self.name} is {self.age} years old, receives income as {income.income_type} and gets taxed for {tax.calculate_tax(income)}"


# income_salary = Salary(income_type="Salary", amount=45000, salary_grade=8)
# income_business = Business(income_type="Business", amount=110000, business_type="Some Business")
# income_investment = Investment(income_type="Investment", amount=2000, investment_type="Some great investment")

# income_tax = TaxCalculator()
# person_one = Person(name="Vytautas Kestutaitis", age=48, income=income_salary)
# person_two = Person(name="Jogaila Algirdas", age=13, income=income_investment)
# print(income_tax.calculate_tax(income_salary))
# print(income_tax.calculate_tax(income_business))
# print(income_tax.calculate_tax(income_investment))
# print(person_one.display_info(income_tax, income_salary))
# print(person_two.display_info(income_tax, income_investment))



        





# Online Shopping System:
#  - Define a class Product with the following attributes and methods:
#    - Attributes: name, price
#    - Method: display_info() - prints information about the product

#  - Define two classes, ElectronicProduct and ClothingProduct, that inherit from Product.
#   - Add additional attributes and methods specific to each class.
#   - For ElectronicProduct: brand
#   - For ClothingProduct: size

# - Define a class ShoppingCart that contains a list of Product objects and has the following methods:
#  - add_to_cart(product) - adds a product to the shopping cart
#  - display_cart() - displays the contents of the shopping cart
#  - calculate_total() - calculates and displays the total price of items in the shopping cart

# When you launch the program, you should display options which category to choose (electronics or Clothing) and Shoping
# Cart with all info and the sum off all items. Within every category there should be at least 5 different items to choose and
# action to `buy` or `return` to main categories selection.
# P.S Create instances of ElectronicProduct and ClothingProduct, add them to the ShoppingCart, and display the cart.

class Product:
    
    def __init__(self, name: str, price: int) -> None:
        self.name: str = name
        self.price: int = price

    def display_info(self) -> str:
        return f"Product: {self.name} costs {self.price} $"
    

class ElectronicProduct(Product):

    def __init__(self, name: str, price: int, brand: str) -> None:
        super().__init__(name, price)
        self.brand: str = brand


class ClothingProduct(Product):

    def __init__(self, name: str, price: int, size: int) -> None:
        super().__init__(name, price)
        self.size = size


class ShoppingCart():
    pass