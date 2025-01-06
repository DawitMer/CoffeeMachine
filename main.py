#import the menu
from menu import MENU
#TODO: 0 show menu

RESOURCE = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

#TODO: 1 print report of coffee machine
def report():
    """DISPLAY THE STORE INFORMATION"""
    for stock in RESOURCE:
        if stock == "water" or stock == "milk":
            print(f"{stock.title()}: {RESOURCE[stock]}ml")
        elif stock == "coffee":
            print(f"{stock.title()}: {RESOURCE[stock]}gm")
        else:
            print(f"{stock.title()}: ${RESOURCE[stock]}")



#TODO: 2 when ordered check resource
def check_stock(drink):
    """Take the drink as an input (Customer_order) and check if te resource is available return True or Else """
    for menu_info in drink:
        if RESOURCE[menu_info] < drink[menu_info]:
            print(f"Sorry there is not enough {menu_info}.")
            return False
    return True



#TODO: 3 check the coin paid and return change

def price_check(drink_price, quarter, dime, nickle, pennie):
    """CHECK THE CUSTOMER ORDER WITH THE PRICE AND GIVE BACK CHANGE IF
    THERE IS AND WILL ALSO RETURN TRUE IS THE IF THE MONEY PAID IS SUFFICIENT BY THE CUSTOMER"""
    total_cash = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01)
    if drink_price < total_cash:
        change = round(total_cash - drink_price, 2)
        print(f"Here is ${change} in change.")

        return True
    return False


def payment(drink_price):
    """WILL TAKE THE CUSTOMER ORDER AND TAKE INPUT FROM THE CUSTOMER TO FORWARD IT
     TO FUNCTION price_check(customer_order, quarter, dime, nickle, pennie)
     IT ALSO RETURNS THE price_check(customer_order, quarter, dime, nickle, pennie)
     """
    quarters = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickle?: "))
    pennies = int(input("How many nickle?: "))
    return price_check (drink_price, quarters, dime, nickle, pennies)



#TODO: 4 update the resource
def update_resource(drink_resource, customer_payment):
    """TAKE THE CUSTOMER ORDER AND UPDATE THE STOCK ACCORDINGLY AND PUT THE CASH IN REGISTER"""
    for menu_info in drink_resource:
        RESOURCE[menu_info] -= drink_resource[menu_info]
    RESOURCE["money"] += customer_payment



def coffee_machine():
    """THIS IS THE COFFEE MACHINE CONTAINING ALL THE FUNCTIONALITIES"""
    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "report":
            report()
        elif order == "off":
            is_on = False
        else:
            #check stock
            drink_resource = MENU[order]["ingredients"]
            if check_stock(drink_resource):
                #check the money
                price = MENU[order]["cost"]
                if payment(price):
                    update_resource(drink_resource, price)
                    # TODO: 5 give the the order to the customer
                    print("Here is your latter ☕️ Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")




coffee_machine()

