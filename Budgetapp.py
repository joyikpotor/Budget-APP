# BUDGET CLASS
class Budget:
    categories = {}

    def __init__(self, initial_balance=0):
        self.free_balance = initial_balance  

    def add_funds(self, amount):
        self.free_balance += amount  #money after allocation to categories - free balance

    def new_category(self, title):
        category = Category(title)
        self.categories[title] = category  #dict of categories
        return category

    def get_category(self, title):
        if title in self.categories:              
            return self.categories[title]
        else:
            return None

    def add_funds_to_category(self, category_title, amount):   
        if self.get_category(category_title) is not None:  #if said category exists, do code
            if self.free_balance >= amount:   #if there's enough money after previous allocations or during initial allocation, greater than or equal to amount we want to allocate, proceed
                self.get_category(category_title).balance += amount
                self.free_balance -= amount
                return True
            else:
                print(f"Error: you need {amount - self.free_balance} more in your "
                      f"budget to allocate this amount to {category_title}")
                return False
        else:
            print(f"Error: category {category_title} not in budget")
            return False

    def withdraw_funds_from_category(self, category_title, amount):
        if self.get_category(category_title) is not None:
            if self.get_category(category_title).balance >= amount:
                self.get_category(category_title).balance -= amount
                self.free_balance += amount
                return True
            else:
                print(f"Error: you can't withdraw more than {self.get_category(category_title).balance} "
                      f"from category: {category_title}")
                return False
        else:
            print(f"Error: category {category_title} not in budget")
            return False

    # Allocated balance stands for money in
    # budget allocated to it's categories
    def get_allocated_balance(self):
        bal = 0
        for i in self.categories:
            bal += self.categories[i].balance
        return bal

    def transfer_funds(self, from_category_title, to_category_title, amount):
        if from_category_title != to_category_title: 
            if (self.get_category(from_category_title).balance  >= amount):
                self.get_category(from_category_title).balance -= amount
                self.get_category(to_category_title).balance +=amount
                print(f'transferred funds successfully {self.get_category(from_category_title).balance} {self.get_category(to_category_title).balance}')

            else:
                print(f'You need {amount - self.get_category(from_category_title).balance} more for your transfer')
        else: 
            print("Cannot send money to same destination")





# CATEGORY CLASS
class Category:
    balance = 0

    def __init__(self, title):
        self.title = title

# MAIN
#TEST CODE
def main():
    budget = Budget(1000)
    print(f"Total budget balance: { budget.free_balance}")

     # print(f"All categories {budget.categories}")
    food_category = budget.new_category("food")
    clothing_category = budget.new_category("clothing")
    entertainment_category = budget.new_category("entertainment")

    print(food_category.title)
    print(food_category.balance)
    print(clothing_category.title)
    print(clothing_category.balance)
    print(entertainment_category.title)
    print(entertainment_category.balance)

    budget.add_funds_to_category("food", 200)
    print(food_category.title)
    print(food_category.balance)

    budget.add_funds_to_category("clothing", 500)
    print(clothing_category.title)
    print(clothing_category.balance)

    
    budget.add_funds_to_category("entertainment", 52)
    print(entertainment_category.title)
    print(entertainment_category.balance)

    budget.add_funds_to_category("clothing", 5000)
    budget.add_funds_to_category("entertainment", 5000)


    print(f"Free budget balance: {budget.free_balance}")
    print(f"Allocated budget balance: {budget.get_allocated_balance()}")

    budget.withdraw_funds_from_category("food", 150)
    print(food_category.title)
    print(food_category.balance)

    print(f"Free budget balance: {budget.free_balance}")
    print(f"Allocated budget balance: {budget.get_allocated_balance()}")

    budget.withdraw_funds_from_category("clothing", 5000)

    budget.transfer_funds("food", 'clothing', 50)
    budget.transfer_funds("clothing", 'clothing', 5000)
    budget.transfer_funds("entertainment", 'food', 510)
    
    

if __name__ == "__main__":
    main()