
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": "%.2f" %amount, "description": description })

    def withdrow(self, amount, description):
        if self.check_funds(float(amount)):
            self.ledger.append({"amount": -float(amount) , "description": description})
        else:
            return False
        # return True 

    def get_balance(self):
        balance = 0.0
        for item in self.ledger:
            balance += float(item["amount"])
        return balance

    def transfer(self, amount,des_category):
        self.check_funds(amount) 
        self.withdrow(amount, f"Transfer To {des_category.name}")
        des_category.deposit(amount, f"Transfer From {self.name}")

    def check_funds (self, amount):
        if float(amount) > self.get_balance():
            return False
        else : return True

    #get the sum of withdrowls for single category
    def calc_withdrowls(self):
        self_withdrowls = 0
        for item in self.ledger:
            if float(item["amount"]) < 0:
                self_withdrowls += item["amount"]
        return round(self_withdrowls, 2)

   #Formatting object to print
    # @staticmethod
    def object_decoration(self):
        print(f'{"*"*13}{self.name}{"*"*13}')
        for item in self.ledger:
            print(item["description"][:23].ljust(23, " "), end="")
            print(str("%.2f" %float(item["amount"])).rjust(7," "))
        print("Total:",self.get_balance())


#Create four categories
food = Category("Food")
clothes = Category("Clothing")
auto = Category("Auto")
intertainment = Category("Intertainment")

food.deposit(1000.00, "Initial")
food.withdrow(10.15, "Groceries")
food.withdrow(15.89, "Restaurant and more food")
food.transfer(50.00, clothes)

#printing Food object 
food.object_decoration()

clothes.withdrow(10.00, "festival" )
clothes.transfer(15.00, auto )

auto.withdrow(15.00, "fuel" )

# intertainment.withdrow(00.00, "netflex" )


# //getting Percentage to nearest ten
total_withdrowls = food.calc_withdrowls() + clothes.calc_withdrowls()+ auto.calc_withdrowls()
food_percent = (food.calc_withdrowls() * 100 / total_withdrowls)//10 *10
clothes_percent = (clothes.calc_withdrowls() * 100 / total_withdrowls)//10 *10
auto_percent = (auto.calc_withdrowls() * 100 / total_withdrowls)//10 *10
# intertainment_percent = (intertainment.calc_withdrowls() * 100 / total_withdrowls)//10 *10

#formatting The "bars" in the bar chart (Categories Percentages)
def format_percentage(percent):
    percent_len = percent
    percent_list=[]
    for i in range(0, 110,10):
        if i > percent_len: percent_list.append(" ") 
        else: percent_list.append("o")

    return percent_list
#Formatting names of categories 
def verticle_names(cat_list):
    max_length = 0
    for i in range(len(cat_list)):
        if len(cat_list[i].name) > max_length:
            max_length = len(cat_list[i].name)
    new_cat_list =[]
    for i in map(lambda l: l.name.ljust(max_length, " "), cat_list):
        new_cat_list.append(i)
    print("    ", end="")
    for letter in range(max_length):
        for i in range(len(new_cat_list)):
            print(f" {new_cat_list[i][letter]} ", end="")
        print("\n    ", end="")

def create_spend_chart(categories):
    print("Percentage spent by category")
    food_percentage_list = format_percentage(round(food_percent,))
    clothes_percentage_list = format_percentage(round(clothes_percent,))
    auto_percentage_list = format_percentage(round(auto_percent,))
    # intertainment_percentage_list = format_percentage(round(intertainment_percent,))
    for i in range(100,-10,-10):
        print(f"{str(i).rjust(3,' ')}|",end="")
        print(f" {food_percentage_list[i//10]} ", end="")
        print(f" {clothes_percentage_list[i//10]} ", end="")
        print(f" {auto_percentage_list[i//10]} ")
        # print(f" {intertainment_percentage_list[i//10]} ", end="")

    print("    "+"-"*(3*len(categories) +1))

    verticle_names(categories)
    
create_spend_chart([food, clothes, auto])
