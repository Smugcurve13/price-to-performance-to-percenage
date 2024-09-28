from functions import get_valid_input

while True:
    try:
        number_of_pcs = get_valid_input("how many pcs: ")

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
    price = int(get_valid_input("enter price: "))
    price_list.append(price)
    performance = int(get_valid_input("enter performance: "))
    performance_list.append(performance)

print(name_list,price_list,performance_list)

price_to_performance_list = []

for price,performance in zip(price_list,performance_list):
    price_to_performance = price / performance
    price_to_performance_list.append(price_to_performance)

print(price_to_performance_list)

pc1_ptp , pc2_ptp = price_to_performance_list

if pc1_ptp > pc2_ptp:
    difference = pc1_ptp - pc2_ptp
    percentage_difference = (difference / pc2_ptp) * 100
    shortened_number = round(percentage_difference,2)
    print(f"PC1's price-to-performance ratio is {shortened_number} times higher per dollar")
else:
    difference = pc2_ptp - pc1_ptp
    percentage_difference = (difference / pc1_ptp) * 100
    shortened_number = round(percentage_difference,2)
    print(f"PC2's price-to-performance ratio is {shortened_number} times higher per dollar")



