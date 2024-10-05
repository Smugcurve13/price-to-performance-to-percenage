import csv
import pandas as pd

file = 'data.csv'
df = pd.read_csv(file, usecols=['name','price','performance'])

num_of_pcs = int(input("How many pcs to compare: "))

pc_choice = input("Enter 1 for search and 2 for input: ")

match pc_choice:
    case '1':
        print(df)
        pc_brand = input("\nEnter 1 for Intel and 2 for AMD: ")
        if pc_brand == '1' :
            for name in (df['name']):
                filtered_data = df[df['name'].str.startswith('Intel')]
                filtered_data = filtered_data.reset_index(drop=True)
                filtered_data.index = filtered_data.index + 1
                print(filtered_data)
                selected_index = int(input("\nEnter the number of the PC you want to select from the list: "))
                selected_pc = filtered_data.iloc[selected_index-1]
                print(selected_pc)
                break
        elif pc_brand == '2':
            for name in (df['name']):
                filtered_data = df[df['name'].str.startswith('AMD')]
                filtered_data = filtered_data.reset_index(drop=True)
                filtered_data.index = filtered_data.index + 1
                print(filtered_data) 
                selected_index = int(input("\nEnter the number of the PC you want to select from the list"))
                selected_pc = filtered_data.iloc[selected_index-1]
                print(selected_pc)           
                break
        else:
            print("Choose from above options")
            
    case _:
        print("Enter Valid Option")
