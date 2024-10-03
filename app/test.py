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

'''
Adding Feature to program which allows allows user to choose between user input and pre defined pcs
'''

import csv

with open('data.csv','r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
print(data)

num_of_pcs = int(input("enter how many pcs you want to compare: "))
names = []
prices = []
performances = []

pcs_dict = {}

for i in range(1,num_of_pcs + 1):
    name = input(f"Enter your pc {i} name: ")
    price = int(input(f"Enter your price of pc {i} : "))
    performance = int(input(f"Enter your performance of pc {i} : "))
    
    pcs_dict[i] = {'name' : name , 'price' : price , 'performance' : performance}  # iterating over a nested dictionary to get individual pcs metadata


# def ptp_calculator(pcs_dict):

ptp_list = []

# print (pcs_dict)
for i in pcs_dict:
    pc_name = pcs_dict[i]['name']
    pc_price = pcs_dict[i]['price']
    pc_performance = pcs_dict[i]['performance']

    price_to_performance = pc_price/pc_performance
    ptp_list.append(price_to_performance)

    #print(f"The {pc_name} with {pc_price}$ of price and the price to performance is {price_to_performance} ")

# print(ptp_list)

best_ptp = max(ptp_list)
best_pc_index = ptp_list.index(best_ptp)
best_pc_name = pcs_dict[best_pc_index + 1]['name']

print(f"{best_pc_name} has the best price-to-performance ratio: {round(best_ptp,4)}")

for ptp in range(len(ptp_list)):
    if ptp != best_pc_index:
        difference = best_ptp - ptp_list[ptp]
        percentage_difference = (difference / ptp_list[ptp]) * 100 if ptp_list[ptp] != 0 else 0
        shortened_number = round(percentage_difference,2)
        
        print (f"{best_pc_name}'s price-to-performance ratio is {shortened_number}% higher than {pcs_dict[ptp + 1]['name']}.")

# if __name__=="__main__":
#     ptp_calculator(pcs_dict)

# Final Output
# PC3 has the best price-to-performance ratio: 0.0160
# PC1's price-to-performance ratio is 31.25% lower than PC3.
# PC2's price-to-performance ratio is 12.50% lower than PC3.
