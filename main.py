# def is_valid_input(value):
#     # check if the value is an positive integer
#     return isinstance(value, int) and value > 0


# def get_valid_input(prompt):
#     while True:
#         try:
#             price = int(input(prompt))
#             if is_valid_input(price):
#                 return price
#             else:
#                 print("Please enter a valid positive integer")
#         except ValueError:
#             print("Invalid inout , please enter a number.")



# pc1_price = get_valid_input("enter the price of pc1: ")
# pc2_price = get_valid_input("enter the price of pc2: ")

# pc1_performance = get_valid_input("Enter performace metric of pc1: ")
# pc2_performance = get_valid_input("Enter performace metric of pc2: ")

pc1_name = "Intel Core i9-14900F"
pc2_name = "Intel Core i9-13900KF"


pc1_price = 524 
pc2_price = 570

pc1_performance = 36660         # using cpu prices and cinebench multi scores as
pc2_performance = 39012         # placeholder values


prices = [pc1_price,pc2_price]
performances = [pc1_performance,pc2_performance]

price_to_performance_list = []

for price,performance in zip(prices,performances):
    price_to_performance = price / performance
    price_to_performance_list.append(price_to_performance)
    
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



