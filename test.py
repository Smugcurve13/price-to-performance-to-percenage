#checking number of pcs to know how many times the the loop should be

# while True:
#     try:
#         number_of_pcs = int(input("how many pcs: "))

#         if number_of_pcs<2:
#             print("Enter a Number equal or more than 2")
#         else:
#             break

#     except ValueError:
#         print("enter a valid integer")

# pc1_price = get_valid_input("enter the price of pc1: ")
# pc2_price = get_valid_input("enter the price of pc2: ")

# pc1_performance = get_valid_input("Enter performace metric of pc1: ")
# pc2_performance = get_valid_input("Enter performace metric of pc2: ")

# pc1_name = "Intel Core i9-14900F"
# pc2_name = "Intel Core i9-13900KF"


# pc1_price = 524 
# pc2_price = 570

# pc1_performance = 36660         # using cpu prices and cinebench multi scores as
# pc2_performance = 39012         # placeholder values


# prices = [pc1_price,pc2_price]
# performances = [pc1_performance,pc2_performance]

# name_list = []
# price_list = []
# performance_list = []

# for i in range(number_of_pcs):
#     name = input("Enter name: ")
#     name_list.append(name)
#     price = int(input("enter price: "))
#     price_list.append(price)
#     performance = int(input("enter performance: "))
#     performance_list.append(performance)

# print(name_list,price_list,performance_list)

name = input("Enter your pc name: ")
price = int(input("Enter your price: "))
performance = int(input("Ener your performance: "))

pcs_dict = {1:{'name' :name ,'price': price ,'performance' : performance}}
print (pcs_dict)

pc_name = pcs_dict[1]['name']
pc_price = pcs_dict[1]['price']
pc_performance = pcs_dict[1]['performance']

price_to_performance = pc_price/pc_performance

print(f"The {pc_name} with {pc_price}$ of price and the price to performance is {price_to_performance} ")

# Final Output
# PC3 has the best price-to-performance ratio: 0.0160
# PC1's price-to-performance ratio is 31.25% lower than PC3.
# PC2's price-to-performance ratio is 12.50% lower than PC3.
