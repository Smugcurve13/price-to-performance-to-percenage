import streamlit as st
import pandas as pd



def ptp_calculator(pcs_dics):

    st.info
    ptp_list = []

    # print (pcs_dic)
    for i in pcs_dic:
        pc_name = pcs_dic[i]['name']
        pc_price = pcs_dic[i]['price']
        pc_performance = pcs_dic[i]['performance']
        

        price_to_performance = pc_price/pc_performance
        ptp_list.append(price_to_performance)

        #print(f"The {pc_name} with {pc_price}$ of price and the price to performance is {price_to_performance} ")

    # print(ptp_list)

    best_ptp = max(ptp_list)
    best_pc_index = ptp_list.index(best_ptp)
    best_pc_name = pcs_dic[best_pc_index + 1]['name']

    print("test")
    return(f"{best_pc_name} has the best price-to-performance ratio: {round(best_ptp,4)}")

    for ptp in range(len(ptp_list)):
        if ptp != best_pc_index:
            difference = best_ptp - ptp_list[ptp]
            percentage_difference = (difference / ptp_list[ptp]) * 100 if ptp_list[ptp] != 0 else 0
            shortened_number = round(percentage_difference,2)
            
            return (f"{best_pc_name}'s price-to-performance ratio is {shortened_number}% higher than {pcs_dic[ptp + 1]['name']}.")

if __name__ == '__main__':
    pass

st.title("Price to Performance to Percentage")
st.write("This Tool provide you how much performance your dollars will net you")

num_of_pcs = st.text_input(label="how many pcs you want to compare?")
try:
    num_of_pcs = int(num_of_pcs)
    name=[]
    price=[]
    performance=[]

    pcs_dic = {}

    for num in range(1,num_of_pcs+1):
        name = st.text_input(label=f"enter name of PC {num}")
        price = int(st.text_input(label=f"enter price of PC {num}"))
        performance = int(st.text_input(label=f"enter performance of PC {num}"))

        pcs_dic[f"PC {num}"] = {'name' : name , 'price' : price , 'performance' : performance}
except ValueError:
    pass
try:
    df=pd.DataFrame(pcs_dic)
    print(df)
    price_to_performance=st.write(df)

    calculate = st.button('Calculate')

    if calculate:
        st.write("Hello , This is working")
        result = ptp_calculator(pcs_dic)
        st.write("The rsults is :-"+ result)
except (NameError, ValueError,KeyError):
    pass



# st.button(label="Calculate",on_click=ptp_calculator(pcs_dic))

st.button("Reset", type="primary")

print(st.session_state)
# display table of pcs after finish entering
# then also add Calculate button
# Then output in different