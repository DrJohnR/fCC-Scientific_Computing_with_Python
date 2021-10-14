class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # f string formatting: [fill][align][width]
        title = f"{self.name:*^30}\n"
        items = ""
        balance = 0
        for entry in self.ledger:
            items += f'{entry["description"][0:23]:23}{entry["amount"]:>7.2f}\n'
            balance += entry["amount"]
        cat_string = title + items + 'Total: ' + f'{balance:.2f}'
        return cat_string

    def check_funds(self, amount):
        funds = 0
        for entry in self.ledger:
            funds += entry["amount"]
        return funds >= amount

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount" : amount, "description" : description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount" : -amount, "description" : description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


# ----- constructing a spending chart -----
def create_spend_chart(categories):
    spends_list = []
    for category in categories:
        cat_spend = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                cat_spend += -entry["amount"]
            else:
                pass
        spends_list.append({"cat_name": category.name, "cat_spend": cat_spend})
    total_spend = sum( [dict["cat_spend"] for dict in spends_list] )

    name_list = []
    prop_list = []
    for dict in spends_list:
        # Note: prop --> proportion (of total_spend)
        name_list.append(dict["cat_name"])
        dict["cat_prop"] = int(dict["cat_spend"]/total_spend*100)/100
        prop_list.append(dict["cat_prop"])

    title = 'Percentage spent by category\n'
    bars = ''
    p = 100
    while p >= 0:
        bar = ' '
        for prop in prop_list:
            if prop*100 >= p:
                bar += 'o' + 2*' '
            else:
                bar += 3*' '
        bars += f'{p:3}|{bar}\n'
        p -= 10
    dashes = 4*' ' + '-' + 3*'-'*len(prop_list) + '\n'

    maxLength = max([len(name) for name in name_list])
    names = 4*' '
    for rowIndex in range(maxLength):
        for name in name_list:
            if rowIndex >= len(name):
                names += 3*' '
            else:
                names += ' ' + name[rowIndex] + ' '
        if rowIndex == maxLength - 1:
            names += ' '
        else:
            names += ' ' + '\n' + 4*' '

    chart = title + bars + dashes + names
    print(chart)
    return chart



# test outputs
food = Category("Food")
bills = Category("Bills")
fun = Category("Fun")
food.deposit(100, "Food_deposit_1")
food.deposit(80, "Food_deposit_2")
food.deposit(20, "Food_deposit_3")
food.transfer(120, bills)
food.withdraw(30.99, "Yum")
bills.withdraw(70, "Bill_1")
fun.deposit(50, "Fun_deposit_1")
fun.withdraw(25, "Yay")

print(f'{food}\n')
print(f'{bills}\n')
print(f'{fun}\n')

categories = [food, bills, fun]
create_spend_chart(categories)
