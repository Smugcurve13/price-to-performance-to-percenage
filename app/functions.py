def is_valid_input(value):
    # check if the value is an positive integer
    return isinstance(value, int) and value > 0


def get_valid_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if is_valid_input(num):
                return num
            else:
                print("Please enter a valid positive integer")
        except ValueError:
            print("Invalid input , please enter a number.")


def ptp_calculator(ptp_list):

    ptp_name = []

    # print (ptp_list)
    for i in ptp_list:
        pc_name = ptp_name[i]
        pc_price = ptp_list[i]
        pc_performance = ptp_list[i]

        price_to_performance = pc_price/pc_performance
        ptp_list.append(price_to_performance)

        #print(f"The {pc_name} with {pc_price}$ of price and the price to performance is {price_to_performance} ")

    # print(ptp_list)

    best_ptp = max(ptp_list)
    best_pc_index = ptp_list.index(best_ptp)
    best_pc_name = ptp_list[best_pc_index + 1]['name']

    print(f"{best_pc_name} has the best price-to-performance ratio: {round(best_ptp,4)}")

    for ptp in range(len(ptp_list)):
        if ptp != best_pc_index:
            difference = best_ptp - ptp_list[ptp]
            percentage_difference = (difference / ptp_list[ptp]) * 100 if ptp_list[ptp] != 0 else 0
            shortened_number = round(percentage_difference,2)
            
            print (f"{best_pc_name}'s price-to-performance ratio is {shortened_number}% higher than {ptp_list[ptp + 1]['name']}.")

    if __name__=="__main__":
        ptp_calculator(ptp_list)

    # Final Output
    # PC3 has the best price-to-performance ratio: 0.0160
    # PC1's price-to-performance ratio is 31.25% lower than PC3.
    # PC2's price-to-performance ratio is 12.50% lower than PC3.


def ptp_calculator_test(pcs_dict):

    ptp_list = []

    for i in range(len(pcs_dict)):
        pc_name = pcs_dict[i]['name']
        pc_price = pcs_dict[i]['price']
        pc_performance = pcs_dict[i]['performance']

        price_to_performance = pc_price/pc_performance
        ptp_list.append(price_to_performance)

    best_ptp = max(ptp_list)
    best_pc_index = ptp_list.index(best_ptp)
    best_pc_name = pcs_dict[best_pc_index]['name']
   

    print(f"{best_pc_name} has the best price-to-performance ratio: {round(best_ptp,4)}")

    for ptp in range(len(ptp_list)):
        if ptp != best_pc_index:
            difference = best_ptp - ptp_list[ptp-1]
            percentage_difference = (difference / ptp_list[ptp]) * 100 if ptp_list[ptp] != 0 else 0
            shortened_number = round(percentage_difference,2)
            
            print (f"{best_pc_name}'s price-to-performance ratio is {shortened_number}% higher than {pcs_dict[ptp]['name']}.")

def input_your_own_pc(num_of_pcs):
    
    pcs_dict = {}

    for i in range(1,num_of_pcs + 1):
        name = input(f"Enter your pc {i} name: ")
        price = get_valid_input(f"Enter your price of pc {i} : ")
        performance = get_valid_input(f"Enter your performance of pc {i} : ")
        
        pcs_dict[i] = {'name' : name , 'price' : price , 'performance' : performance}  # iterating over a nested dictionary to get individual pcs metadata
    
    print(pcs_dict)