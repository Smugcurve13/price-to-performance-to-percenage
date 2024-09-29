# from functions import get_valid_input


# # def p2p():
# while True:
#     try:
#         number_of_pcs = get_valid_input("how many pcs: ")

#         if number_of_pcs<2:
#             print("Enter a Number equal or more than 2")
#         else:
#             break

#     except ValueError:
#         print("enter a valid integer")

# name_list = []
# price_list = []
# performance_list = []

# for i in range(number_of_pcs):
#     name = input("Enter name: ")
#     name_list.append(name)
#     price = int(get_valid_input("enter price: "))
#     price_list.append(price)
#     performance = int(get_valid_input("enter performance: "))
#     performance_list.append(performance)

# print(name_list,price_list,performance_list)

# price_to_performance_list = []

# for price,performance in zip(price_list,performance_list):
#     price_to_performance = price / performance
#     price_to_performance_list.append(price_to_performance)

# print(price_to_performance_list)


# pc = 0
# for ptp in price_to_performance_list:
#     if ptp > pc:
#         pc = ptp
    
# print(f"{pc} is the highest score")