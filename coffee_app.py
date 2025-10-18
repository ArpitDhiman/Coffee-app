from math import ceil
print("\nWelcome to Coffee App!")
name = input("Enter Your Name Please: ")

menu_items = {
    "Espresso        $": 5.99,
    "Cappuccino      $": 4.76,
    "Americano       $": 5.64,
    "Latte           $": 2.57,
    "Black Coffee    $": 2.99,
    "Foam White      $": 3.90,
    "Hot Chocolate   $": 2.36,
    "Vanilla Coffee  $": 4.56,
    "Dalgona Coffee  $": 10.00,}

cart_items = []
cart_price = []

def menu():
    print("\nHere is our menu:")
    i = 1
    for key, value in menu_items.items():
        print(f'{i}. {key} {value}')
        i += 1

    print(f'{i}. Check Out')
    print(f'{i+1}. EXIT')

while True:
    menu()
    value = v = int(input("Enter a value: "))
    coffees = list(menu_items.keys())
    prices = list(menu_items.values())

    if value in range(1, len(menu_items)+1):
        print(f"The price of the {coffees[value-1]}{prices[value-1]}")
        cups = int(input("How many cups? "))
        cart_items.append(coffees[value-1])
        cart_price.append(prices[value-1]*cups)
        print(f'Your oder has been added to your cart')
        bill = dict(zip(cart_items, cart_price))

    elif value == len(menu_items) + 1:                                          #Check-Out

        if len(cart_price) == 0:
            print("You haven't order anything yet! \nKindly order somethng to access this section")

        else:
            check_out = input("Do you want to Check out?[yes/no] ").lower()
            if check_out == "yes":
                print("\nHere is your bill:")                                   #Shows Bill
                for key, price, in bill.items():
                    print(f'{key}{price}')

                print(f'Your total is ${ceil(sum(cart_price))} [inclusive of GST]\n')

                with open("order.txt", "a") as file:
                    file.write(f'{name}\n')
                    file.write(f'{bill}\n')
                    file.write(f'Total Amount Paid: ${ceil(sum(cart_price))} [with GST] ')

                print("How would you like to pay?")
                payment_option = ["card", "cash", "upi"]
                for items in payment_option:
                    print(items)

                pay = input("Kindly choose an option for payment: ").lower()

                if pay in payment_option:
                    cart_price.clear()
                    cart_items.clear()
                    bill.clear()
                    print("Payment Successful")
                
                    with open("order.txt", "a") as file:
                        file.write(f'-------with {pay} \n\n')

                else:
                    print("Choose from the given options")

            elif check_out == "no":
                print("No problem!")

            else:
                print("Error")
    
    elif value == len(menu_items) + 2:                                          #Exit
        if len(cart_price) == 0:
            print("Exiting the app")
            print("Author - Arpit Dhiman")
            break
        
        else:
            print(f"You haven't paid our ${ceil(sum(cart_price))} yet!")
            print(f"Kindly choose {len(menu_items)+1} for payment")
    
    else:
        print("Kindly select from the menu!")