while True:
    try:
        number_of_pcs = int(input("how many pcs: "))

        if number_of_pcs<2:
            print("Enter a Number equal or more than 2")
        else:
            break

    except ValueError:
        print("enter a valid integer")
        



name_list = []
price_list = []
performance_list = []

for i in range(number_of_pcs):
    name = input("Enter name: ")
    name_list.append(name)
    price = int(input("enter price: "))
    price_list.append(price)
    performance = int(input("enter performance: "))
    performance_list.append(performance)

print(name_list,price_list,performance_list)